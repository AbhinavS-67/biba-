import streamlit as st

st.set_page_config(layout="wide")

# Remove padding (clean UI)
st.markdown("""
    <style>
    .block-container {
        padding: 0rem;
    }
    </style>
""", unsafe_allow_html=True)

# Load HTML file
with open("IBM_Damodaran_Terminal.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Render HTML
st.components.v1.html(html_content, height=1000, scrolling=True)
