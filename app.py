from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask on push to corretly configured branch!  5 go go"

if __name__ == '__main__':
    app.run()
