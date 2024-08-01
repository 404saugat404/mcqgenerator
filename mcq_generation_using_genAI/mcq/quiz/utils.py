import os 
import PyPDF2
import traceback
import json

def read_file(file):
    if file.name.endswith('.pdf'):
        try:
            reader=PyPDF2.PdfReader(file)
            text=""
            for page in reader.pages():
                text=text+page.extract_text()

            return text

        except Exception as e:
            raise Exception('unknown error occured while reading pdf file') 

    elif file.name.endswith('.txt'):
        return file.read().decode('utf-8')

    else:
        raise Exception("file format not supported") 
    

def get_table_data(quiz_str):
    try:
        quiz_data=[]
        quiz_dict=json.loads(quiz_str)

        for key,value in quiz_dict.items():
            mcq=value['mcq']
            options=" | ".join(
                [
                    f"{option}: {option_value}"
                    for option, option_value in value["options"].items()
                ]
            )
            correct_value=value['correct']
            quiz_data.append({
                "MCQ":mcq ,
                "CHOICES":options, 
                "CORRECT ANSWER":correct_value
                      })
        return quiz_data

    except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)
            return False