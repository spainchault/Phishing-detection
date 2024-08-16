# Phishing Email Classifier

This project is a phishing email classifier built using Python and Streamlit. The classifier uses a Naive Bayes model to identify phishing emails based on the presence of certain spam words. The model is trained on a dataset of labeled emails and uses TF-IDF vectorization for text processing.

## Features

- **Spam Word Detection**: Identifies if an email contains spam words from a predefined list.
- **Machine Learning Model**: Utilizes a Naive Bayes classifier for predicting phishing emails.
- **Interactive Web Interface**: Built with Streamlit for an interactive user experience.

## Installation

To run this project, you need to have Python installed. It is recommended to use a virtual environment. Follow these steps to set up your environment:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/spainchault/phishingdetection.git
   cd phishingdetection
   python -m venv venv

# Windows
.\venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

Install the required packages:

bash
Copy code
pip install -r requirements.txt
Download or place the dataset and spam word list:

Place your dataset file (Nazario_5.csv) in the project directory.
Ensure you have a spam_wordlist.txt file with one spam word per line.
Usage


Install the required packages:

bash
Copy code
pip install -r requirements.txt
Download or place the dataset and spam word list:

Place your dataset file (Nazario_5.csv) in the project directory.
Ensure you have a spam_wordlist.txt file with one spam word per line.
Usage
To start the Streamlit app, run:

bash
Copy code
streamlit run app.py
This will open a new tab in your default web browser with the Phishing Email Classifier app.

Files
app.py: The main script for running the Streamlit app.
Nazario_5.csv: The dataset containing email bodies and labels (phishing or not).
spam_wordlist.txt: A text file containing spam words, one per line.
requirements.txt: List of Python packages required for the project.
Code Overview
contains_spam_words(email_body, spam_wordlist): Checks if an email body contains any spam words from the spam_wordlist.
__main__(): Main function to configure the Streamlit app, load data, train the model, and display results.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
This project uses the scikit-learn library for machine learning and the Streamlit library for building the web interface.
The dataset and spam word list should be appropriately sourced and formatted for accurate results.
Contact
For any questions or issues, please contact Your Name.

javascript
Copy code

### Notes

- **Replace Placeholder URLs**: Make sure to replace `https://github.com/yourusername/phishing-email-classifier.git` with the actual URL of your repository and `[Your Name](mailto:your-email@example.com)` with your actual contact details.
- **`requirements.txt`**: If you don’t have a `requirements.txt` file yet, you can create one with the following command after installing the packages:
  ```bash
  pip freeze > requirements.txt