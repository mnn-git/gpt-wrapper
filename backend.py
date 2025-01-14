from flask import Flask, request, jsonify

app = Flask(__name__)

def test():
    return "hello world"

if __name__ == "__main__":
    app.run(debug=True)