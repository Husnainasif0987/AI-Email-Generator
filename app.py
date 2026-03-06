import streamlit as st
import openai

st.title("AI Email Generator")

api_key = st.text_input("Enter OpenAI API Key")

email_type = st.selectbox(
    "Select Email Type",
    ["Marketing Email", "Cold Outreach Email", "Customer Support Email"]
)

topic = st.text_input("Enter Email Topic")

tone = st.selectbox(
    "Select Tone",
    ["Professional", "Friendly", "Persuasive"]
)

if api_key:
    openai.api_key = api_key

if st.button("Generate Email"):

    prompt = f"""
    Write a {tone} {email_type} about {topic}.
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    st.write("### Generated Email")
    st.write(response['choices'][0]['message']['content'])
