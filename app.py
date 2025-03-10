import os
import streamlit as st
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.schema import StrOutputParser


chat_template = PromptTemplate.from_template("""
You are a travel assistant. Provide the best travel options between {source} and {destination}.
Include options for flights, trains, buses, and cabs with estimated costs.
""")


chat_model = ChatGoogleGenerativeAI(google_api_key='AIzaSyDS30Upcy6YBYO14ZDg4GP-BW-9SQzZdQk', model="gemini-2.0-flash-exp", temperature=1)
parser = StrOutputParser()


chain = chat_template | chat_model | parser

def get_travel_options(source, destination):
    raw_input = {"source": source, "destination": destination}
    response = chain.invoke(raw_input)
    return response


st.title("✈️ AI Travel Planner")
st.write("Find the best travel options between two cities!")


source = st.text_input("Enter Source Location")
destination = st.text_input("Enter Destination Location")

if st.button("Find Travel Options"):
    if source and destination:
        response = get_travel_options(source, destination)
        st.subheader("Travel Options:")
        st.write(response)
    else:
        st.warning("Please enter both source and destination.")