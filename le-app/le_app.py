#!/usr/bin/env python
from flask import Flask

app = Flask(__name__)

@app.route('/.well-known/acme-request/<path:path>')
def hello(path):
    return 'Hello from Fake-LetsEncrypt @ {}!'.format(path)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
