from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask on PythonAnywhere! Welcome to your app."

if __name__ == '__main__':
    app.run()
