import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# ===== Home Page =====
@app.route("/")
def home():
    # static/images folder se saari images read karo
    images_path = os.path.join(app.static_folder, "images")

    quotes = []
    if os.path.exists(images_path):
        quotes = [
            img for img in os.listdir(images_path)
            if img.lower().endswith((".jpg", ".png", ".jpeg", ".webp"))
        ]

    return render_template("index.html", quotes=quotes)


# ===== Download Image =====
@app.route("/download/<filename>")
def download(filename):
    return send_from_directory(
        directory=os.path.join(app.static_folder, "images"),
        path=filename,
        as_attachment=True
    )


# ===== Render Deployment Fix (IMPORTANT) =====
if __name__ == "__main__":
    # Render apna PORT deta hai — wahi use karna zaroori hai
    port = int(os.environ.get("PORT", 10000))

    # 0.0.0.0 zaroor likhna hota hai Render ke liye
    app.run(host="0.0.0.0", port=port, debug=False)
