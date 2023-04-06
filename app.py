import streamlit as st
import openai
import os
from text_summarizer.functions import summarize
from text_summarizer.data_processing import data_loader
from text_summarizer.data_processing import reference_loader
from text_summarizer.rouge_score import cal_Rouge_1
from text_summarizer.rouge_score import cal_Rouge_2
from text_summarizer.rouge_score import cal_Rouge_L

openai.api_key = os.getenv('OPENAI_KEY')

st.title("Text Summarizer")

# initialize state variable 
if "summary" not in st.session_state:
  st.session_state["summary"] = ""

prompt = data_loader()
input_text =  st.text_area(label="Prompt text", value=prompt, height=250)

st.button(
    "Submit",
    on_click=summarize,
    kwargs={"prompt": input_text},
    )

output_text = st.text_area(label="Summarized text: ", value=st.session_state["summary"], height=250)

result = st.session_state["summary"]
reference = reference_loader()

gold_reference = st.text_area(label="Reference text: ", value=reference, height=250)

R1 = cal_Rouge_1(result, reference)
R2 = cal_Rouge_2(result, reference)
RL = cal_Rouge_L(result, reference)

R1_score = st.text_area(label='Rouge_1:', value=R1, height=100)
R2_score = st.text_area(label='Rouge_2:', value=R2, height=100)
RL_score = st.text_area(label='Rouge_L:', value=RL, height=100)



