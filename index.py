from flask import Flask, request, jsonify
import os, sys, platform, json
app = Flask(__name__)
import jwt

@app.route("/")
def home():

    token1 =  request.headers.get('x-ms-token-aad-id-token')
    token2 =  request.headers.get('x-ms-token-aad-access-token')

    print("Token 1:" + token1)
    print("Token 2:" + token2)

    token_decoded = jwt.decode(token1)

    return token_decoded

if __name__ == '__main__':
    app.run(host='0.0.0.0')