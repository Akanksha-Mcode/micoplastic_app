# 🧪 Microplastic Detection Web Application

This project is a Flask-based web application that detects and counts microplastics in uploaded images using computer vision techniques. Users can upload an image, and the system analyzes it to identify microplastic particles and returns the total count along with an annotated image.

---

## 🚀 Features

- Upload images for microplastic analysis  
- Automatic detection and counting of microplastics  
- Annotated output image showing detected particles  
- Simple and user-friendly web interface  
- Gemini-powered chatbot integration  

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask  
- **Frontend:** HTML, CSS, JavaScript  
- **Image Processing:** OpenCV  
- **AI Chatbot:** Google Gemini API  
- **Version Control:** Git, GitHub  

---

## 📁 Project Structure

microplastic_app/
│── app.py
│── chatbot.py
│── detect_microplastic.py
│── templates/
│ └── index.html
│── static/
│── README.md
---

## ⚙️ Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/microplastic-app.git
   cd microplastic-app
Install required packages:

pip install flask requests opencv-python


Set the Gemini API key:

setx GEMINI_API_KEY "your_api_key_here"


Run the application:

python app.py


Open in browser:

http://127.0.0.1:5000

🧠 How It Works

The user uploads an image through the web interface

The Flask backend saves the image

The image is processed to detect microplastics

The total count and annotated image are returned to the user

⚠️ Disclaimer

This project is intended for educational and research purposes only. Detection accuracy depends on image quality and algorithm limitations.

👤 Author

Akanksha
B.Tech Student
Microplastic Detection Project

📜 License

This project is open-source and intended for educational use.


---

