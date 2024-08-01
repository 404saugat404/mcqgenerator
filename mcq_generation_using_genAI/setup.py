from setuptools import find_packages, setup

setup(
    name="MCQ Generation using GenAI",
    author="Saugat Thapa Chhetri",
    author_email="saugat556513@gmail.com",
    install_requires=['openai','langchain','python-dotenv','streamlit','PyPDF2'],
    packages=find_packages()

)



