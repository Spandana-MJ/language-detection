import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Load the dataset
data = pd.read_csv('Language Detection.csv',encoding='utf-8')
data = data[['Text', 'Language']]

# Split the data
X = data['Text']
y = data['Language']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Convert text to features
# Convert text to features using character n-grams
vectorizer = CountVectorizer(analyzer='char', ngram_range=(1, 3))
X_train_counts = vectorizer.fit_transform(X_train)
X_test_counts = vectorizer.transform(X_test)


# Train the model
model = MultinomialNB()
model.fit(X_train_counts, y_train)

# Predict and evaluate
y_pred = model.predict(X_test_counts)
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Model Accuracy: {accuracy * 100:.2f}%")

# Test with your own sentence
while True:
    sentence = input("\nEnter a sentence to detect language (or type 'exit' to quit): ")
    if sentence.lower() == 'exit':
        break
    sentence_transformed = vectorizer.transform([sentence])
    prediction = model.predict(sentence_transformed)
    print(f"🌐 Predicted Language: {prediction[0]}")
print(data['Language'].value_counts())




