import os
from flask import Flask, request, jsonify, render_template
import PyPDF2
from google import genai

# ==============================
# APP CONFIGURATION
# ==============================

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ==============================
# GEMINI CONFIGURATION (NEW API)
# ==============================

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# ==============================
# PDF TEXT EXTRACTION
# ==============================

def extract_text_from_pdf(pdf_path):
    extracted_text = ""

    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                extracted_text += page_text

    return extracted_text


# ==============================
# RESUME PARSING (LLM)
# ==============================

def parse_resume(resume_text):
    prompt = f"""
You are a resume parser.

Extract the following information:
- Skills
- Experience summary
- Education
- Tools & technologies

Resume Content:
{resume_text}

Return the output in clear bullet points.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text


# ==============================
# JOB DESCRIPTION PARSING
# ==============================

def parse_job_description(job_description):
    prompt = f"""
Extract the following from the job description:
- Required skills
- Responsibilities
- Preferred qualifications

Job Description:
{job_description}

Return the output in clear bullet points.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text


# ==============================
# ATS MATCHING LOGIC
# ==============================

def ats_match(parsed_resume, parsed_jd):
    prompt = f"""
You are an Applicant Tracking System (ATS).

Compare the resume and the job description.

Resume:
{parsed_resume}

Job Description:
{parsed_jd}

Provide:
1. Match percentage (0-100)
2. Matching skills
3. Missing skills
4. Strengths
5. Improvement suggestions

Return the result in a clear and readable format.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text


# ==============================
# ROUTES
# ==============================

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    if "resume" not in request.files:
        return jsonify({"error": "Resume PDF is required"}), 400

    resume_file = request.files["resume"]
    job_description = request.form.get("job_description")

    if not job_description:
        return jsonify({"error": "Job description is required"}), 400

    pdf_path = os.path.join(app.config["UPLOAD_FOLDER"], resume_file.filename)
    resume_file.save(pdf_path)

    resume_text = extract_text_from_pdf(pdf_path)

    parsed_resume = parse_resume(resume_text)
    parsed_jd = parse_job_description(job_description)

    ats_result = ats_match(parsed_resume, parsed_jd)

    return jsonify({
        "parsed_resume": parsed_resume,
        "parsed_job_description": parsed_jd,
        "ats_result": ats_result
    })


# ==============================
# RUN APPLICATION
# ==============================

if __name__ == "__main__":
    app.run(debug=True)
