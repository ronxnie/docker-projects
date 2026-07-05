import os

import socket

from flask import Flask, jsonify

app = Flask(__name__)

 

@app.get("/health")

def health():

    return jsonify(status="ok", service="backend")

 

@app.get("/api/message")

def message():

    return jsonify(

        service="backend",

        container=socket.gethostname(),

        message="Hello from the backend service",

    )

 

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "5000")))