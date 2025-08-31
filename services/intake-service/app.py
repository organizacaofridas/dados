from flask import Flask, jsonify
app = Flask(__name__)
@app.get("/health")
def health(): return jsonify(ok=True)
@app.get("/")
def root(): return jsonify(msg="Fridas Cloud Run is up!")
