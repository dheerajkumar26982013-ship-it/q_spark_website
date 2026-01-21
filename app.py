import os
from flask import Flask, render_template, request, redirect, url_for

# Flask app create kar rahe hain
app = Flask(__name__)

# Example route: Home page
@app.route('/')
def home():
    return render_template('index.html')  # agar tumhara index.html templates folder me hai

# Example route: Another page
@app.route('/download')
def download_quotes():
    # yahan tumhara quotes download logic hoga
    return "Download your quotes here!"

# Aur agar aur routes hain, wo yahan add karo

# ======= Last line for Render deployment =======
if __name__ == "__main__":
    # Render ke liye host aur port setup
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

