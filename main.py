import streamlit as st
from scrape import (
    scrape_website,
    extract_body_content,
    clean_body_content,
    split_dom_content,
)
from parse import parse_with_gemini

st.title("Web Page Summarizer")
st.header("Author: Jesse-Paul Miracle Osemeke")
st.write("Uses AI and web scraping techniques to summarize the contents of any webpage")

url = st.text_input(label="Website URL")

if st.button("Scrape Site"):
    st.write("Working...")
    result = scrape_website(url)
    body_content = extract_body_content(result)
    clean_content = clean_body_content(body_content)

    st.session_state.dom_content = clean_content

    with st.expander("View DOM Content"):
        st.text_area("DOM Content", clean_content, height=300)


# Step 2: Ask Questions About the DOM Content
if "dom_content" in st.session_state:

    if st.button("Summarise Content"):
        # Parse the content with Ollama
        dom_chunks = split_dom_content(st.session_state.dom_content)
        summarised_result = parse_with_gemini(dom_chunks)
        st.write(summarised_result)
