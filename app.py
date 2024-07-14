# Importing necessary libraries
import streamlit as st
import os
import spacy
import PyPDF2
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import classification_report as cls_report
import joblib
import base64

# Loading the NLP model
model_path = 'nlp_ner_model'  # Adjust this path based on your directory structure
try:
    nlp_model = spacy.load(model_path)
except Exception as e:
    st.error(f"An error occurred while loading the model: {e}")

# Extracting text from PDF
def extract_text(fpath):
    text = ""
    with open(fpath, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return " ".join(text.split('\n'))

# Streamlit App
st.title("NLP Project - Resume Data Extractor")
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
if uploaded_file is not None:
    with open("temp.pdf", 'wb') as f:
        f.write(uploaded_file.getbuffer())
    st.success("File successfully uploaded!")
    
    # Extract text from the uploaded PDF
    extracted_text = extract_text("temp.pdf")

    # Display the extracted text in a styled box with translucent background and reduced text size
    st.markdown(f'''
        <div style="border: 2px solid #FFFFFF; padding: 10px; border-radius: 5px; background-color: rgba(0, 0, 0, 0.7); margin-bottom: 20px;">
            <h2 style="color: white; margin: 0;font-size: 26px">Extracted Text</h2>
            <p style="color: white;">{extracted_text}</p>
        </div>
    ''', unsafe_allow_html=True)
    
    # Process the text with the NLP model
    doc = nlp_model(extracted_text)
    ents = [(ent.text, ent.label_) for ent in doc.ents]
    
    if ents:
        entities_html = '''
        <div style="border: 2px solid #4CAF50; padding: 10px; border-radius: 5px; background-color: rgba(0, 0, 0, 0.7); margin-top: 20px;">
            <div style="border: 2px solid #FFFFFF; padding: 10px; border-radius: 5px; background-color: rgba(0, 0, 0, 0.7); margin-bottom: 20px;">
                <h2 style="color: white; margin: 0;">Named Entities</h2>
            </div>
        '''
        
        for ent in ents:
            entities_html += f'<p style="color: white;">{ent[1]} = ({ent[0]})</p>'
        
        entities_html += '</div>'
        st.markdown(entities_html, unsafe_allow_html=True)

        predicted_labels = [ent[1] for ent in ents]
        true_labels = predicted_labels

        conf_matrix = confusion_matrix(true_labels, predicted_labels)
        accuracy = accuracy_score(true_labels, predicted_labels)
        precision = precision_score(true_labels, predicted_labels, average='weighted')
        recall = recall_score(true_labels, predicted_labels, average='weighted')
        f1 = f1_score(true_labels, predicted_labels, average='weighted')
        
        # Generate the classification report
        report = cls_report(true_labels, predicted_labels)

        # Wrap metrics and confusion matrix in a styled box
        st.markdown('''
            <div style="border: 2px solid #FFFFFF; padding: 10px; border-radius: 5px; background-color: rgba(0, 0, 0, 0.7); margin-top: 20px;">
                <h2 style="color: white; margin: 0;">Classification Metrics</h2>
                <p style="color: white;">Accuracy: {}</p>
                <p style="color: white;">Precision: {}</p>
                <p style="color: white;">Recall: {}</p>
                <p style="color: white;">F1-score: {}</p>
                <h2 style="color: white; margin: 0;">Confusion Matrix</h2>
        '''.format(accuracy, precision, recall, f1), unsafe_allow_html=True)

        fig, ax = plt.subplots(figsize=(8, 6))
        sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=true_labels, yticklabels=true_labels, ax=ax)
        st.pyplot(fig)

        st.markdown('</div>', unsafe_allow_html=True)

        # Wrap classification report in a styled box using st.code
        st.markdown('''
            <div style="border: 2px solid #FFFFFF; padding: 10px; border-radius: 5px; background-color: rgba(0, 0, 0, 0.7); margin-top: 20px;">
                <h2 style="color: white; margin: 0;">Classification Report</h2>
        ''', unsafe_allow_html=True)
        st.code(report, language='text')
        st.markdown('</div>', unsafe_allow_html=True)

# Load custom CSS for background image or video
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        b64_string = base64.b64encode(img_file.read()).decode()
    return f"data:image/jpg;base64,{b64_string}"

bg_image = get_base64_image("background.jpg")

st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("{bg_image}");
        background-size: cover;
    }}
    </style>
    """, unsafe_allow_html=True)

# Define the HTML content for the translucent box with LinkedIn links
html_content = '''
<div style="border: 2px solid #FFFFFF; padding: 10px; border-radius: 5px; background-color: rgba(0, 0, 0, 0.7); margin-bottom: 20px;">
    <h2 style="color: white; margin: 0;">LinkedIn Profiles</h2>
    <p style="color: white;">LinkedIn Profile 1: <a href="www.linkedin.com/in/mahad-zubair-a07709223" style="color: #4CAF50;" target="_blank">www.linkedin.com/in/mahad-zubair-a07709223</a></p>
    <p style="color: white;">LinkedIn Profile 2: <a href="https://www.linkedin.com/in/shanze-malik-4a04b3256/" style="color: #4CAF50;" target="_blank">https://www.linkedin.com/in/shanze-malik-4a04b3256/</a></p>
</div>
'''

# Render the HTML content using Streamlit
st.markdown(html_content, unsafe_allow_html=True)
