# 🌍 Language Detection using Naive Bayes  

This project is a **Language Detection Web App** that identifies the language of a given text input.  
It supports **17 languages** using a **Naive Bayes classification model** trained on a dataset of text samples.  

---

## 🚀 Features
- 🌐 Detects **17 different languages** (e.g., English, French, Spanish, Hindi, German, etc.)  
- 🎨 Simple **frontend** built with **HTML, CSS, JavaScript**  
- 🐍 **Backend API** in **Python (Flask/FastAPI)**  
- 📊 Uses **Naive Bayes algorithm** for text classification  
- ⚡ Real-time prediction on user input  

---

## 📂 Project Structure
language-detection/
│── app.py # Flask backend (API for predictions)
│── language_detection.py # ML model training & prediction
│── Language Detection.csv # Dataset (~10k samples, 17 languages)
│── templates/ # Frontend HTML files
│ └── index.html
│── static/ # CSS & JS files
│ ├── style.css
│ └── script.js
│── README.md # Project documentation


---

## 🛠️ Installation & Setup

1️⃣ Clone the repository  
```bash
git clone https://github.com/Spandana-MJ/language-detection.git
cd language-detection


2️⃣ Create a virtual environment & activate it

python -m venv .venv
source .venv/bin/activate   # for Linux/Mac
.venv\Scripts\activate      # for Windows


3️⃣ Install dependencies

pip install -r requirements.txt


4️⃣ Run the backend server

python app.py


5️⃣ Open your browser → http://127.0.0.1:5000