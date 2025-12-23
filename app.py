from flask import Flask, request, jsonify, render_template, send_from_directory
import os
import uuid
from detect_microplastic import detect_microplastics
from chatbot import chat_with_gemini   # ✅ ADDED

app = Flask(__name__)

# Folder to save uploaded images
UPLOAD_FOLDER = "static"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    """
    Renders the main page of the application.
    """
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    """
    Handles image upload, runs the microplastic detection,
    and returns the analysis results.
    """
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "Empty filename"}), 400

    filename = f"{uuid.uuid4().hex}.png"
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)

    try:
        count, annotated_path = detect_microplastics(filepath)
        annotated_url = f"/{annotated_path.replace(os.path.sep, '/')}"
        return jsonify({
            "summary": {
                "count": count,
                "annotated_url": annotated_url
            }
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ================= CHATBOT ROUTE (ONLY ADDITION) =================

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message")
    reply = chat_with_gemini(user_msg)
    return jsonify({"reply": reply})

# ================================================================


@app.route("/static/<path:filename>")
def serve_file(filename):
    """
    Serves static files from the UPLOAD_FOLDER.
    """
    return send_from_directory(UPLOAD_FOLDER, filename)


if __name__ == "__main__":
    app.run(debug=True)
