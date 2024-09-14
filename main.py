import streamlit as st
from scraper import scrape_website, clean_html, clean_body_text, create_chunks
from parse import parse

st.title("Web Scraper and Parser")

# Input URL from the user
url = st.text_input("Website URL:")

# Handle URL scraping
if st.button("Scrape Site"):
    if url:
        with st.spinner("Scraping the website..."):
            try:
                html = scrape_website(url)
                body = clean_html(html)
                cleaned_body = clean_body_text(body)

                st.session_state.dom_content = cleaned_body

                st.success("Scraping and cleaning completed successfully!")

                st.write("Scraped and cleaned content:")

                with st.expander("Show Results", expanded=True):
                    st.text_area("Results", cleaned_body, height=300)

            except Exception as e:
                st.error(f"An error occurred while scraping: {e}")
    else:
        st.error("Please enter a valid URL.")

# Ensure there is content to parse
if "dom_content" in st.session_state:
    parse_description = st.text_area("Description for parsing")

    if st.button("Parse Description"):
        if parse_description:
            with st.spinner("Parsing description..."):
                try:
                    dom_chunks = create_chunks(st.session_state.dom_content)
                    result = parse(dom_chunks, parse_description)
                    st.write("Parsed Content:")
                    st.text_area("Parsed Results", result, height=300)

                except Exception as e:
                    st.error(f"An error occurred while parsing: {e}")
        else:
            st.error("Please provide a description for parsing.")
else:
    st.info("Scrape a website first to enable parsing.")
