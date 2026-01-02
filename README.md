# ATS-Project-using-Gemini-GenAI
Application tracking system
📄 GenAI-Based Applicant Tracking System (ATS)
📌 Overview

An Applicant Tracking System (ATS) is used by organizations to automatically analyze resumes and match them with job descriptions.
This project implements a mini ATS platform using Flask, PDF parsing, and Google Gemini GenAI to simulate real-world resume screening used in recruitment systems.

The system accepts a resume in PDF format and a job description, analyzes both, and generates an AI-based evaluation including match percentage and feedback.

🎯 Problem Statement

Manual resume screening is:

Time-consuming

Error-prone

Not scalable

This project aims to automate resume evaluation using a GenAI-powered backend workflow.

⚙️ System Flow

User uploads a resume PDF

Backend extracts text from the PDF

Resume content is parsed using Gemini GenAI

Job description is parsed using Gemini GenAI

ATS logic compares resume and job description

AI-generated analysis is returned as JSON

🛠 Technology Stack

Python

Flask

HTML / CSS (Frontend)

PyPDF2 (PDF text extraction)

Google Gemini GenAI

JSON

📂 Project Structure
ATS_Project/
│
├── app.py              # Flask backend
├── index.html          # Frontend UI
├── style.css           # UI styling (optional)
├── uploads/            # Temporary PDF storage
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation

📥 API Design
Endpoint
POST /analyze

Input

Resume PDF (multipart/form-data)

Job description (text)

Output (JSON)

Parsed resume data

Parsed job description

ATS evaluation result

🧠 ATS Evaluation Includes

Match Percentage (0–100)

Matching skills

Missing skills

Strengths

Improvement suggestions

📌 Sample Input

Resume: resume.pdf

Job Description:
Backend Developer with experience in Python, APIs, and database systems.

📊 Sample Output
{
  "parsed_resume": "...",
  "parsed_job_description": "...",
  "ats_result": "Match Percentage: 80% ..."
}

🚀 How to Run the Project
1️⃣ Install Required Packages
pip install flask PyPDF2 werkzeug google-genai

2️⃣ Set Gemini API Key (Environment Variable)
setx GOOGLE_API_KEY "YOUR_API_KEY"


Restart VS Code after setting the key.

3️⃣ Run the Flask App
python app.py


The server will start at:

http://127.0.0.1:5000

4️⃣ Access the Application

Open browser

Upload resume PDF

Paste job description

Click Analyze Resume

🎓 Learning Outcomes

By completing this project, students learn to:

Build a Flask-based backend application

Handle file uploads securely

Extract text from PDFs

Design GenAI prompts

Implement an ATS-style evaluation system

Understand real-world GenAI use cases in HR tech

🌱 Future Enhancements

Strict JSON output formatting

Resume and JD embeddings for semantic matching

Frontend result visualization

Database integration

RAG-based ATS system

📌 Conclusion

This project demonstrates how PDF parsing, backend APIs, and Generative AI can be combined to build a real-world ATS system.
It provides practical exposure to how AI is applied in recruitment and enterprise systems.
