import streamlit as st
from mcq.quiz.logger import logging
from mcq.quiz.utils import read_file, get_table_data
import json
import traceback
from langchain.callbacks import get_openai_callback
from mcq.quiz.mcq_main import final_chain
import pandas as pd

from dotenv import load_dotenv


#loading json file:
with open('/home/saugat/Desktop/GenAI/mcq_generation_using_genAI/RESPONSE.json', "r") as file:
    RESPONSE_JSON=json.load(file)

st.title('MCQ GENERATOR')

#CREATING FORM USING st.form

with st.form('user input'):
    file_upload=st.file_uploader("upload your file here: ")

    mcq_count=st.number_input("input number of mcq you want: ", min_value=3, max_value=20)

    topic=st.text_input("input the topic on which you want to generate mcq: " , max_chars=20)

    difficulty=st.text_input('input the difficulty level: ', max_chars=20,placeholder="simple" )

    button=st.form_submit_button('click to submit: ')


    #checking if the button is clicked and the file is submitted
    if file_upload and button is not None and mcq_count and topic and difficulty:
        with st.spinner('loading....'):
            try:
                text=read_file(file_upload)
            
                with get_openai_callback() as cb:
                    #count tokens and cost of api
                    response=final_chain(
                        {
                            "text":text,
                            "number":mcq_count,
                            "subject":topic,
                            "tone":difficulty,
                            "response_json":json.dumps(RESPONSE_JSON)

                        }
                    )



            except Exception as e:
                traceback.print_exception(type(e),e,e.__traceback__)
                st.error("error")
        
            else:

                print(f"Total Tokens:{cb.total_tokens}")
                print(f"Prompt Tokens:{cb.prompt_tokens}")
                print(f"Completion Tokens:{cb.completion_tokens}")
                print(f"Total Cost:{cb.total_cost}")

                if isinstance(response,dict):
                    quiz=response.get('quiz')
                    if quiz is not None:
                        table_data=get_table_data(quiz)
                        if table_data is not None:
                            df=pd.DataFrame(table_data)
                            df.index=df.index+1
                            st.table(df)

                            #display the table in a review box as well
                            st.text_area(label="review",value=response["review"])

                        else:
                            st.error('error in table data')

                else:
                    st.write("response")



                                
                

            

# print(f"Total Tokens:{cb.total_tokens}")
#             print(f"Prompt Tokens:{cb.prompt_tokens}")
#             print(f"Completion Tokens:{cb.completion_tokens}")
#             print(f"Total Cost:{cb.total_cost}")


