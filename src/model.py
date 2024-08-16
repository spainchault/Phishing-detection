import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.metrics import classification_report
from sklearn.utils import shuffle
import streamlit as st

# Function to check if email contains any spam words
def contains_spam_words(email_body, spam_wordlist):
    words = email_body.lower().split()
    for word in words:
        if word in spam_wordlist:
            return 1
    return 0

# Streamlit app code
st.set_page_config(page_title="Phishing Email Classifier", page_icon=":email:")
st.title("Phishing Email Classifier")
st.write(" ")

# Load the dataset
data = pd.read_csv("./data/Nazario_5.csv")

# Load with spam wordList
with open("./data/spam_wordlist.txt", "r") as f:
    spam_wordlist = set(f.read().splitlines())

# Apply the function to each email body
data['contains_spam_words'] = data['body'].apply(lambda x: contains_spam_words(x, spam_wordlist))

# Shuffle the data because it is in order in the file (all non-phishing first)
data_shuffled = shuffle(data, random_state=42)

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(
    data_shuffled['body'],
    data_shuffled['label'],
    test_size=0.2,
    random_state=42
)

# Create a model pipeline for vectorizing text and training the classifier
model = make_pipeline(
    TfidfVectorizer(),
    MultinomialNB()
)

# Train the model
model.fit(x_train, y_train)

# Predict on the testing set
y_pred = model.predict(x_test)

# Generate the classification report as a dictionary
report_dict = classification_report(y_test, y_pred, output_dict=True)

# Convert the dictionary to a pandas DataFrame
report_df = pd.DataFrame(report_dict).transpose()

# Text area for user input
email_text = st.text_area('Enter the email content here:', height=250)

# Button to submit the email
if st.button('Check Email'):
    if email_text:
        # Preprocess the input email text
        processed_text = email_text.lower()
        # Predict using the model
        prediction = model.predict([processed_text])
        # Display the result
        if prediction == 1:
            st.error('This email is likely a phishing email.')
        else:
            st.success('This email is not a phishing email.')
    else:
        st.write('Please enter the email content.')

# Function to preprocess the email text (example)
def preprocess(text):
    # Add your preprocessing steps here
    return text

url = "https://security.berkeley.edu/education-awareness/phishing/phishing-examples-archive"
st.write(" ")
st.write("Enter your own email example or visit [this website](%s) which provides examples of phishing emails." % url)

# Display the model report
st.write("#")
st.subheader("Model Report")
st.write(report_df)