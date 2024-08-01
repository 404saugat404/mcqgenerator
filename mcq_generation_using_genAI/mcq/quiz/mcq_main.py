import langchain
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

from mcq.quiz.logger import logging

from mcq.quiz.utils import read_file,get_table_data

from dotenv import load_dotenv
import os
import traceback

load_dotenv()
api_key=os.getenv("openai_api_key")
client=ChatOpenAI(api_key=api_key, model_name="gpt-3.5-turbo", temperature=0.5)


Template1="""
text:{text}
you are a mcq generator.Based on the given text, your job is to generate {number} multiple choice question for
{subject} student in {tone} tone.Make sure the questions are not repeated and check all the questions to be conforming the text as well.
Make sure the format is in RESPONSE_JSON format which is given below and use it as a guide.
Enure to make {number} MCQs

{response_json}

"""

quiz_generation_prompt=PromptTemplate(
    input_variables=['text','number','subject','tone','response_json'],
    template=Template1
)


quiz_creation_chain=LLMChain(llm=client, prompt=quiz_generation_prompt,output_key='quiz',verbose=True)



Template2="""
You are an expert english grammarian and writer. Given a Multiple Choice Quiz for {subject} students.\
You need to evaluate the complexity of the question and give a complete analysis of the quiz. Only use at max 50 words for complexity analysis. 
if the quiz is not at per with the cognitive and analytical abilities of the students,\
update the quiz questions which needs to be changed and change the tone such that it perfectly fits the student abilities
Quiz_MCQs:
{quiz}

Check from an expert English Writer of the above quiz:
"""

quiz_evaluation_prompt=PromptTemplate(
    input_variables=['subject','quiz'],
    template=Template2
)


quiz_evaluation_chain=LLMChain(llm=client, prompt=quiz_evaluation_prompt,output_key="review",verbose=True)

final_chain=SequentialChain(
    chains=[quiz_creation_chain,quiz_evaluation_chain],
    input_variables=['text','number','subject','tone','response_json'],
    output_variables=['quiz','review'],
    verbose=True
                            )