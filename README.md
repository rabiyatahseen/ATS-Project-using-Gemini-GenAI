
# 📄 ATS Project using Gemini GenAI

**Application Tracking System**

---

## 📌 Overview

An **Applicant Tracking System (ATS)** is a software application used by organizations to automatically screen resumes and match them against job descriptions.

This project implements a **mini ATS platform** using **Flask, PDF parsing, and Google Gemini Generative AI**.
It simulates how modern recruitment systems analyze resumes and provide structured feedback.

The system accepts:

* A **resume (PDF format)**
* A **job description (text input)**

And produces:

* Parsed resume details
* Parsed job description details
* ATS evaluation with strengths, gaps, and suggestions

---

## 🎯 Objective

The goal of this project is to:

* Automate resume screening
* Reduce manual effort in recruitment
* Demonstrate a real-world **GenAI use case**
* Build an end-to-end ATS-style workflow

---

## ⚙️ System Workflow

1. User uploads a **resume PDF**
2. User enters a **job description**
3. Backend extracts text from the PDF
4. Gemini GenAI parses resume content
5. Gemini GenAI parses job description
6. ATS logic compares both
7. Results are rendered on a **result UI page**

---

## 🛠️ Technology Stack

* **Python**
* **Flask**
* **HTML / CSS**
* **PyPDF2** – PDF text extraction
* **Google Gemini GenAI**
* **Jinja2 Templates**

---

## 📂 Project Structure

```
ATS_Project/
│
├── app.py                 # Flask backend
├── uploads/               # Temporary resume storage
│
├── templates/
│   ├── index.html         # Resume upload UI
│   └── result.html        # ATS result page
│
├── static/
│   └── style.css          # Styling for UI
│
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---

## 🔌 API & Routing

### Routes Used

| Route      | Method | Description                      |
| ---------- | ------ | -------------------------------- |
| `/`        | GET    | Resume upload page               |
| `/analyze` | POST   | Resume analysis & ATS evaluation |

---

## 🧠 ATS Evaluation Includes

* ATS Match Percentage
* Matching skills
* Missing skills
* Strengths (Pros)
* Improvement suggestions (Cons)

All results are displayed in a **professional UI**, similar to real ATS dashboards.

---

## 📌 Sample Input

* **Resume:** `resume.pdf`
* **Job Description:**
  *Looking for a Software Developer with experience in Python, web development, APIs, and databases.*

---

## 📊 Sample Output (UI)

* Parsed Resume Section
* Parsed Job Description Section
* ATS Evaluation Section:

  * Match %
  * Strengths
  * Missing skills
  * Recommendations

---

## 🚀 How to Run the Project

### 1️⃣ Install Dependencies

```bash
pip install flask PyPDF2 werkzeug google-genai
```

---

### 2️⃣ Set Gemini API Key

#### Windows (Command Prompt)

```bash
setx GEMINI_API_KEY "YOUR_API_KEY"
```

Restart VS Code after setting the key.

---

### 3️⃣ Run the Application

```bash
python app.py
```

Server runs at:

```
http://127.0.0.1:5000
```

---

### 4️⃣ Use the Application

1. Open browser
2. Upload resume (PDF)
3. Paste job description
4. Click **Analyze Resume**
5. View ATS results on the result page

---

## 🎓 Learning Outcomes

Through this project, students gain experience in:

* Flask backend development
* Handling file uploads securely
* PDF text extraction
* Prompt engineering for GenAI
* Building ATS-style logic
* Integrating AI into real-world systems
* Designing professional UI using HTML & CSS

---

## 🌱 Future Enhancements

* Dynamic ATS score calculation
* JSON-structured AI responses
* Skill match visual charts
* Resume history storage
* Database integration
* RAG-based ATS evaluation

---

## 📌 Conclusion

This project demonstrates how **Generative AI** can be effectively combined with **backend APIs and document processing** to build a **real-world Applicant Tracking System**.

It provides strong practical exposure to:

* AI-assisted recruitment
* Enterprise-level automation
* End-to-end system design

---

## 💡 Notes

This project is intended for:

* Academic submission
* GenAI learning
* Portfolio demonstration



