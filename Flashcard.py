#pip install openai pandas python-dotenv google-generativeai google-cloud-aiplatform

import os
import google.generativeai as genai 
import streamlit as st

from dotenv import load_dotenv
from GPT_Interaction_SeparateInstances import generate_flashcards_twoparts
from Strip_Formatting import strip_formatting
from Create_Anki_CSV import create_anki_csv

#import vertexai
#import csv
#from vertexai.preview.language_models import ChatModel
#from google.generativeai import protos
#from google.protobuf import struct_pb2
#from GPT_Interaction_Chat import generate_flashcards

def main(script_content, topic):
    #Access API key enviroment variable and put into gemini 
    #load_dotenv() 
    #genai.configure(api_key=os.getenv('GOOGLE_GEMINI_API_KEY')) 
    #print('successfully loaded api key...')

    #Access API key from streamlit secrets
    genai.configure(api_key=st.secrets["api_key"]) 
    print('successfully loaded api key...')

    #read script
    #with open("26_Sugammadex.txt", "r") as f:
        #script_content = f.read()
    #print('successfully loaded podcast script...')

    #generate flashcards
    flashcards = generate_flashcards_twoparts(
            script=script_content, 
            topic=topic,
            temperature=0.2,
            max_output_tokens=8000,
            revision_temperature=0.3)
    print(flashcards)

    #Strip formatting from flashcards
    flashcardsStripped = strip_formatting(flashcards)
    print(flashcardsStripped)

    #Convert flashcard output to Anki-compatible CSV format. By default the output is called anki_flashcards.csv
    create_anki_csv(flashcardsStripped) 

if __name__ == "__main__":
    main()
