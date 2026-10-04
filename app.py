from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

# Pre-trained AI summarization model
summarizer = pipeline(
    "summarization",
    model="Falconsai/text_summarization"
)

print("MODEL:", summarizer.model.config._name_or_path)

@app.route("/", methods=["GET", "POST"])
def home():

    original_text = ""
    summary = ""
    original_count = 0
    summary_count = 0
    reduction = 0

    if request.method == "POST":

        original_text = request.form["text"].strip()

        if original_text:

            # Original word count
            original_count = len(original_text.split())

            # Generate short AI summary
            result = summarizer(
                original_text,
                max_length=80,
                min_length=20,
                do_sample=False
            )

            summary = result[0]["summary_text"].strip()
            summary = summary.replace(" .", ".")
            summary = summary.replace(" ,", ",")

            # Summary word count
            summary_count = len(summary.split())

            # Percentage reduction
            if original_count > 0:
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