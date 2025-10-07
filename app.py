import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="AI Text Generator", page_icon="🧠")

st.title("🧠 AI Text Generator — Sentiment Aware")
st.write("Enter a prompt, and the app generates text matching its sentiment!")

@st.cache_resource
def load_models():
    sentiment_model = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
    generator = pipeline("text-generation", model="distilgpt2")
    return sentiment_model, generator

sentiment_model, generator = load_models()

prompt = st.text_area("✏️ Enter your prompt:")
manual = st.selectbox("Manual sentiment override:", ["Auto Detect", "Positive", "Negative", "Neutral"])
length = st.slider("Output length (approx. words)", 10, 300, 100, 10)
btn = st.button("🚀 Generate")

def detect_sentiment(text):
    res = sentiment_model(text)[0]
    label = res['label'].lower()
    score = res['score']
    if score < 0.6:
        return "neutral", score
    return ("positive" if label == "positive" else "negative"), score

if btn:
    if not prompt.strip():
        st.warning("Please enter a prompt.")
    else:
        if manual == "Auto Detect":
            sentiment, conf = detect_sentiment(prompt)
            st.write(f"**Detected Sentiment:** {sentiment.capitalize()} ({conf:.2f})")
        else:
            sentiment = manual.lower()
            st.write(f"**Manual Sentiment:** {sentiment.capitalize()}")

        text_prompt = f"Write a {sentiment} paragraph about: {prompt}\n\n"
        tokens = int(length * 1.6) + 20
        with st.spinner("Generating text..."):
            out = generator(text_prompt, max_length=tokens, do_sample=True, top_p=0.95, top_k=50)
        generated = out[0]['generated_text']
        if generated.startswith(text_prompt):
            generated = generated[len(text_prompt):].strip()

        st.subheader("📝 Generated Text")
        st.write(generated)
