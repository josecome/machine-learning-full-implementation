from app import app
from flask import jsonify

@app.route("/api")
def api():
    return 'Test!'