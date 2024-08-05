MCQ Generator using OpenAI API Key
Overview

The MCQ Generator is a web application built with Streamlit that utilizes the OpenAI API and LangChain to generate multiple-choice questions (MCQs) from text or PDF files. Users can upload documents, specify the number of questions, choose the topic, and set the difficulty level. The application processes the input and generates a set of MCQs based on the provided parameters.
Features

    File Upload: Drag and drop text or PDF files for processing.
    Customization: Specify the number of MCQs, select the topic, and set the difficulty level.
    Output Generation: Automatically generate and display the MCQs based on the input criteria.

Requirements

    Python 3.7+
    OpenAI API key
    Libraries: openai, PyPDF2, streamlit, langchain

Installation

    Clone the repository:

    bash

git clone https://github.com/404saugat404/mcqgenerator.git
cd mcq-generator

Install the required libraries:

bash

pip install openai PyPDF2 streamlit langchain

Set up your OpenAI API key:

python

    import openai
    openai.api_key = 'your-api-key'

Usage

    Running the Application:

    bash

    streamlit run mcq_generator.py

    Uploading a File:
        Drag and drop a text or PDF file into the designated area of the application interface.

    Setting Parameters:
        Choose the number of MCQs you want to generate.
        Select the topic of the MCQs.
        Set the difficulty level (easy, medium, hard).

    Generating MCQs:
        Click the "Generate" button.
        The generated MCQs will be displayed on the screen.

Example

    Upload a File:
    Drag and drop sample.pdf into the application.

    Specify Parameters:
        Number of MCQs: 10
        Topic: Machine Learning
        Difficulty: Medium

    Generate Output:
    Click "Generate" to receive the MCQs.

Contributing

If you would like to contribute to this project, please follow these steps:

    Fork the repository.
    Create a new branch: git checkout -b feature-branch
    Make your changes and commit them: git commit -m 'Add some feature'
    Push to the branch: git push origin feature-branch
    Open a pull request.

Acknowledgements

    OpenAI for providing the API.
    LangChain for the language processing framework.
    Streamlit for the web application framework.
    PyPDF2 for PDF handling.

Contact

For any questions or suggestions, please open an issue on GitHub or contact me at saugat556513@gmail.com.
