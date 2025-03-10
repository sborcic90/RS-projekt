from flask import Flask, jsonify
import requests
app = Flask(__name__)  #inicijalizacija nove flask datoteke , dodjeljivanje adrese

@app.route("/service")
def get():
    r = requests.get("http://google.com")
    #print("Primjer", r.content)
    #pass    #ništa, samo vraćanje statusa
    return jsonify({"status": "OK", "length": len(r.content)})

