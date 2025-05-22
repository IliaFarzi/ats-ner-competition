import streamlit as st
import spacy
from huggingface_hub import hf_hub_download
import os

# Load spaCy model from Hugging Face
@st.cache_resource
def load_model():
    model_dir = hf_hub_download(repo_id="ISFarzi/resume-ner", filename="model-best", repo_type="model", local_dir="model-best", local_dir_use_symlinks=False)
    return spacy.load(model_dir)

nlp = load_model()

# UI
st.title("🧠 Resume NER Demo")
st.markdown("Enter a resume text below to extract **skills, job titles, universities, etc.**")

text = st.text_area("📄 Paste Resume Text", height=300)

if st.button("🔍 Analyze Entities"):
    if text:
        doc = nlp(text)
        for ent in doc.ents:
            st.markdown(f"**{ent.label_}**: {ent.text}")
    else:
        st.warning("Please enter some text first.")
