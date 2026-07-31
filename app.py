from flask import Flask, render_template, request, jsonify
import whisper
import cohere
import tempfile
import scipy.io.wavfile as wav
import numpy as np
import os

app = Flask(__name__)

# ======= الإعدادات =======
COHERE_API_KEY = "put your Api "
SAMPLE_RATE = 48000

# ======= تهيئة =======
print("جار تحميل Whisper...")
model = whisper.load_model("base")
co = cohere.ClientV2(COHERE_API_KEY)
print("✅ جاهز!")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/transcribe", methods=["POST"])
def transcribe():
    """يستقبل ملف صوت ويحوله لنص"""
    if "audio" not in request.files:
        return jsonify({"error": "لم يتم إرسال ملف صوت"}), 400

    audio_file = request.files["audio"]

    with tempfile.NamedTemporaryFile(suffix=".webm", delete=False) as f:
        audio_file.save(f.name)
        tmp_path = f.name

    try:
        result = model.transcribe(tmp_path, language="arabic", fp16=False)
        text = result["text"].strip()
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        os.unlink(tmp_path)

    return jsonify({"text": text})

@app.route("/chat", methods=["POST"])
def chat():
    """يرسل النص لـ Cohere ويرجع الرد"""
    data = request.get_json()
    user_text = data.get("text", "").strip()

    if not user_text:
        return jsonify({"error": "النص فارغ"}), 400

    try:
        response = co.chat(
            model="command-r7b-arabic-02-2025",
            messages=[{"role": "user", "content": user_text}]
        )
        reply = response.message.content[0].text
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
