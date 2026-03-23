# AI Resume Screening System 📄🤖

## 📌 Project Overview
The **AI Resume Screening System** is a Python-based application that automatically analyzes resumes and extracts structured information such as **personal details, skills, projects, and achievements**.  
This project uses **Natural Language Processing (NLP)** techniques to convert unstructured resume data into meaningful insights.

The system is useful for **HR teams, recruiters, and students** to quickly screen and understand resumes.

---

## 🎯 Objectives
- Accept resumes in **PDF or DOCX format**
- Extract resume text automatically
- Identify and extract:
  - Personal Details (Name, Email, Phone)
  - Skills
  - Projects
  - Achievements
- Display the extracted data in a **structured format**
- Build a beginner-friendly **AI/NLP portfolio project**

---

## 🧠 How It Works
1. User uploads a resume
2. Resume text is extracted using document parsers
3. NLP preprocessing is applied (cleaning & tokenization)
4. Information is extracted using:
   - Regular Expressions
   - Keyword matching
   - NLP techniques
5. Output is displayed as structured data (JSON / UI)

---

## 🏗️ System Architecture
Resume (PDF/DOCX)
↓
Text Extraction
↓
NLP Processing
↓
Information Extraction
↓
Structured Output

yaml
Copy code

---

## 🛠️ Technologies Used

| Category | Tools / Libraries |
|--------|------------------|
| Language | Python |
| Resume Parsing | pdfplumber, python-docx |
| NLP | NLTK, SpaCy |
| Regex | re |
| UI (Optional) | Streamlit |
| Data Output | JSON |

---

## 📁 Project Structure
resume-screening-system/
│
├── app.py # Main application file
├── resume_parser.py # Resume text extraction logic
├── skill_extractor.py # Skill extraction logic
├── section_extractor.py # Projects & achievements extraction
├── utils.py # Helper functions
├── requirements.txt # Required libraries
├── sample_resumes/ # Sample resumes for testing
└── README.md

yaml
Copy code

---

## 📥 Input
- Resume file (`.pdf` or `.docx`)

---

## 📤 Output
Structured information such as:
Name : John Doe
Email : john.doe@gmail.com
Phone : +91XXXXXXXXXX
Skills : Python, Machine Learning, SQL
Projects : Yoga Pose Classification System
Achievements: Hackathon Winner

yaml
Copy code

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/resume-screening-system.git
cd resume-screening-system
2️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
3️⃣ Run the Application
bash
Copy code
python app.py
(or streamlit run app.py if using Streamlit)

✨ Features
✔ Automatic resume parsing
✔ NLP-based information extraction
✔ Skill detection from predefined database
✔ Easy-to-understand structured output
✔ Beginner-friendly AI project

