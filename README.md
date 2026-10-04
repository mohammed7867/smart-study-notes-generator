# Smart Study Notes Generator

An AI-powered web application that converts lengthy paragraphs into concise summaries using a pre-trained Hugging Face Transformer model.

## Features

- Accepts paragraph/text input
- Generates an AI-powered summary
- Displays original word count
- Displays summary word count
- Calculates percentage of text reduction
- Simple and responsive web interface
- Built with Python and Flask

## Technologies Used

- Python
- Flask
- Hugging Face Transformers
- PyTorch
- HTML
- CSS
- JavaScript
- `Falconsai/text_summarization`

## How It Works

1. User enters a paragraph.
2. Flask receives the text.
3. The pre-trained Transformer model processes the text.
4. The application generates a concise summary.
5. Original and summary word counts are calculated.
6. Percentage reduction is displayed.

## Formula

Text Reduction:

\[
\text{Reduction} =
\frac{\text{Original Words} - \text{Summary Words}}
{\text{Original Words}}
\times 100
\]

## Project Structure

```text
smart-study-notes-generator/
│
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
│
└── templates/
    └── index.html
