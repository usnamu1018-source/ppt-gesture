from flask import Flask, request
import pyautogui

app = Flask(__name__)

@app.route("/next", methods=["POST"])
def next_slide():
    pyautogui.press('right')
    return "ok"

@app.route("/prev", methods=["POST"])
def prev_slide():
    pyautogui.press('left')
    return "ok"

if __name__ == "__main__":
    app.run(port=5000)
