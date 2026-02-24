import streamlit as st
from morphology import convert_to_singular, convert_to_plural, extract_root_words
from utils import read_txt, read_pdf
st.title("🔤 Large-Scale Morphological Text Processor")

mode = st.selectbox(
    "Select Operation",
    ["None", "Convert to Singular", "Convert to Plural"]
)

uploaded_file = st.file_uploader("Upload TXT or PDF", type=["txt", "pdf"])
text_input = st.text_area("Or Enter Text Manually")
if uploaded_file:
    if uploaded_file.type == "text/plain":
        text = read_txt(uploaded_file)
    else:
        text = read_pdf(uploaded_file)
else:
    text = text_input
if st.button("Process Text"):
    
    if mode == "Convert to Singular":
        result = convert_to_singular(text)
        st.subheader("Singular Output")
        st.write(result)

    elif mode == "Convert to Plural":
        result = convert_to_plural(text)
        st.subheader("Plural Output")
        st.write(result)

    roots = extract_root_words(text)
    st.subheader("Root Words")
    st.write(roots)
