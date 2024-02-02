import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("microsoft/phi-2", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    "microsoft/phi-2", torch_dtype="auto", device_map="auto", trust_remote_code=True
)


# Streamlit app
st.title("Fake news Generation with Transformers Microsoft phi-2")

st.image("https://raw.githubusercontent.com/noorkhokhar99/NewsGuardian/main/logo.jpeg")

# User input
prompt = st.text_area("Enter your prompt:", "This news is real or fake you get results from here NewsGuardian")

# Generate output
if st.button("Generate"):
    with torch.no_grad():
        token_ids = tokenizer.encode(prompt, add_special_tokens=False, return_tensors="pt")
        output_ids = model.generate(
            token_ids.to(model.device),
            max_new_tokens=512,
            do_sample=True,
            temperature=0.1
        )

    output = tokenizer.decode(output_ids[0][token_ids.size(1):])
    st.text("Generated Output:")
    st.write(output)
