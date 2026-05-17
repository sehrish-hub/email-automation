# 🚀 AI Job Apply Button System (Streamlit + Gmail API)

An AI-powered automation system that allows users to apply for jobs with a single click.  
The system generates professional emails, attaches CVs, and sends applications using Gmail API.

---

## 📌 Project Overview

This project simplifies the job application process by automating:

- Job application email creation
- CV attachment handling
- Email sending via Gmail API
- Simple UI using Streamlit

With just a few inputs, users can instantly send professional job applications to recruiters.

---

## ✨ Features

- 📄 Upload CV (PDF format)
- 🧑‍💼 Enter Job Title / Designation
- 📧 Enter HR Email
- 🚀 One-click “Apply Now” button
- 🤖 Automated professional email generation
- 🔐 Secure Gmail API integration (OAuth 2.0)
- ⚡ Instant email delivery

---

## 🛠️ Tech Stack

- Python 🐍
- Streamlit 🎯
- Gmail API 📧
- Google OAuth 2.0 🔐
- Base64 Email Encoding

---

## 📂 Project Structure
email-automation/
│
├── app.py # Streamlit UI
├── send_email.py # Gmail API email logic
├── credentials.json # Google API credentials
├── token.json # OAuth token
├── CV.pdf # User resume
└── requirements.txt # Dependencies


---

## 🚀 How It Works

1. User opens Streamlit app  
2. Enters HR email + job title  
3. Uploads CV (PDF)  
4. Clicks **Apply Now**  
5. System:
   - Generates professional email
   - Attaches CV
   - Sends email via Gmail API

---

## ▶️ Installation & Setup

### 1. Clone Repository
```bash
git clone https://github.com/your-username/job-apply-system.git
cd job-apply-system

2. Install Dependencies
pip install -r requirements.txt

3. Setup Google Cloud (Gmail API)
Create project on Google Cloud
Enable Gmail API
Download credentials.json
Place it in project folder
4. Run Application
streamlit run app.py
📸 UI Preview

(Add screenshot here)
Example:

Job Email Input
Designation Input
CV Upload
Apply Button
💡 Use Cases
Job application automation
Freelance automation tool
HR outreach system
Portfolio project for AI Engineering
🔥 Future Improvements
AI-generated cover letters 🤖
LinkedIn job auto-apply integration
Multi-job bulk apply system
Resume builder inside app
Job tracking dashboard
👨‍💻 Author

Sehrish Shafiq

💼 AI Engineer | Python Developer
🌐 LinkedIn: https://www.linkedin.com/in/sehrish-shafiq
⭐ Support

If you like this project, please consider giving a ⭐ on GitHub.

📜 License

This project is open-source and available under the MIT License.