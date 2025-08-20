from flask import Flask, request, jsonify,render_template
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load and train model
data = pd.read_csv('Language Detection.csv', encoding='utf-8')
data = data[['Text', 'Language']]
X = data['Text']
y = data['Language']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

vectorizer = CountVectorizer(analyzer='char', ngram_range=(1, 3))
X_train_counts = vectorizer.fit_transform(X_train)
model = MultinomialNB()
model.fit(X_train_counts, y_train)

# Flask app
app = Flask(__name__)

 

app = Flask(__name__)

# This tells Flask to serve index.html when you go to "/"
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/detect', methods=['POST'])
def detect_language():
    input_text = request.json.get('text')
    if not input_text:
        return jsonify({'error': 'No text provided'}), 400
    transformed = vectorizer.transform([input_text])
    prediction = model.predict(transformed)
    return jsonify({'language': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
