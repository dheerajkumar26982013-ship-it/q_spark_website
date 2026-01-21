from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Homepage
@app.route('/')
def home():
    # यह folder path से सारी images detect करेगा
    quotes = os.listdir("static/images")
    quotes.sort()  # alphabetical order में
    return render_template("index.html", quotes=quotes)

# Download route
@app.route('/download/<filename>')
def download(filename):
    return send_from_directory("static/images", filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
