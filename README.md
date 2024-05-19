# NLP Project - Resume Data Extractor

Welcome to the **Resume Data Extractor**! This project is designed to help you extract and analyze information from resumes with ease. By leveraging powerful NLP techniques, this tool can identify key information from PDF resumes and present it in a clear, organized manner.

## 🚀 Features

- **PDF Text Extraction**: Upload your resume in PDF format, and we'll take care of extracting the text.
- **Named Entity Recognition (NER)**: Automatically detect important entities such as names, dates, skills, and more using our pre-trained NLP model.
- **Visualizations**: Get a detailed look at the extracted entities and see evaluation metrics presented in an easy-to-understand format.
- **Evaluation Metrics**: Understand the performance of the NER model with metrics like accuracy, precision, recall, F1-score, and a confusion matrix.
- **Stylish UI**: Enjoy a sleek, user-friendly interface with custom styling and background images.

## 🎉 Getting Started

Follow these steps to get your Resume Data Extractor up and running:

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/yourusername/resume-data-extractor.git
    cd resume-data-extractor
    ```

2. **Install Dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Download the NLP Model**:
    - Ensure you have a pre-trained Spacy model for Named Entity Recognition. You can download one using:
    ```sh
    python -m spacy download en_core_web_sm
    ```

### Running the App

1. **Start the Streamlit App**:
    ```sh
    streamlit run app.py
    ```

2. **Upload a Resume**:
    - Open your browser and navigate to the Streamlit app URL provided.
    - Upload a PDF resume and let the magic happen!

## 🛠️ How It Works

1. **Upload a PDF**: Use the file uploader to select and upload a PDF resume.
2. **Extract Text**: The app reads the PDF and extracts the text content.
3. **Analyze Text**: The extracted text is processed using a Spacy NLP model to identify named entities.
4. **Display Results**: The identified entities and evaluation metrics are displayed in a visually appealing format.

## 🖼️ Custom Styling

The app features custom styling, including a background image and themed UI elements to enhance user experience. You can customize the appearance by editing the CSS in the `app.py` file.

## 🔗 LinkedIn Profiles

Want to connect with the developers? Check out our LinkedIn profiles:
- [Mahad Zubair](www.linkedin.com/in/mahad-zubair-a07709223)
- [Shanze Malik](https://www.linkedin.com/in/shanze-malik-4a04b3256/)

## 🤝 Contributing

We welcome contributions! Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🌟 Acknowledgements

- Special thanks to the Spacy team for their awesome NLP library.
- Thanks to the Streamlit team for making web app development fun and easy.

---

Happy extracting! 🎉🚀

For any queries or support, feel free to open an issue or contact us directly through our LinkedIn profiles. Let's make resume analysis smarter and more fun together!
