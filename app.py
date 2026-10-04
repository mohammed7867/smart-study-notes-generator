import os
from flask import Flask, render_template, request
from huggingface_hub import InferenceClient

app = Flask(__name__)

client = InferenceClient(
    provider="hf-inference",
    api_key=os.environ.get("HF_TOKEN")
)


@app.route("/", methods=["GET", "POST"])
def home():

    original_text = ""
    summary = ""
    original_count = 0
    summary_count = 0
    reduction = 0

    if request.method == "POST":

        original_text = request.form.get("text", "").strip()

        if original_text:

            original_count = len(original_text.split())

            try:
                result = client.summarization(
                    original_text,
                    model="facebook/bart-large-cnn"
                )

                summary = result.summary_text.strip()

                summary = summary.replace(" .", ".")
                summary = summary.replace(" ,", ",")

            except Exception as e:
                app.logger.exception("Summarization failed")
                summary = "Unable to generate a summary right now. Please try again."

            summary_count = len(summary.split())

            if original_count > 0 and summary:
                reduction = (
                    (original_count - summary_count)
                    / original_count
                ) * 100

    return render_template(
        "index.html",
        original_text=original_text,
        summary=summary,
        original_count=original_count,
        summary_count=summary_count,
        reduction=round(reduction, 2)
    )


if __name__ == "__main__":
    app.run()