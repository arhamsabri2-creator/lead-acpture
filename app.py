import os
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

WEBHOOK_URL = "https://hook.us2.make.com/7g2j3yts12383v1vwdqbn70z85gw0rss"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        
        data = {
            "name": name,
            "email": email
        }
        
        requests.post(WEBHOOK_URL, json=data)
        
        return render_template("index.html", success=True)
    
    return render_template("index.html", success=False)

if __name__ == "__main__":
    app.run(debug=True)
