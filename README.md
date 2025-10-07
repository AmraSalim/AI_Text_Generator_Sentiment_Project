# AI Text Generator with Sentiment Alignment

AI Text Generator with Sentiment Alignment, an intelligent system that generates AI-written text - paragraphs or short essays, reflecting the sentiment of a user-provided prompt: Positive, Negative, or Neutral. It combines sentiment analysis with natural language generation to produce coherent, context-aware content.

## Objective

The main goal of this project is to:

- Detect the sentiment of a given user prompt.
- Generate meaningful text aligned with the detected sentiment.
- Offer a user-friendly frontend interface for seamless interaction.

## Key Features

- Sentiment Detection: Automatically classify user input as Positive, Negative, or Neutral using NLP models.
- AI Text Generation: Generate coherent text that reflects the detected or selected sentiment.
- Interactive Frontend: Streamlit-based UI for easy user input and instant output.
- Customizable: Users can manually select sentiment and adjust word limits.

## Tech Stack

- Language: Python
- NLP & Text Generation: Hugging Face Transformers
- Frontend: Streamlit
- Model Backend: PyTorch / TensorFlow
- Development Environment: Google Colab
- Testing & Deployment: Ngrok (for sharing Colab apps)

## Usage

- Enter a prompt in the text input field.
- Either: Allow automatic sentiment detection, or Manually select the sentiment.
- Set a word limit.
- Click Generate to receive AI-generated text aligned with the selected sentiment.
