#!/usr/bin/env python
from flask import Flask

app = Flask(__name__)

@app.route('/<path:path>')
def hello(path):
    return 'Hello from Flask @ {}!'.format(path)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
