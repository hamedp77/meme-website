from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

def get_meme():

    meme_endpoint = 'https://meme-api.com/gimme'
    response = json.loads(requests.get(meme_endpoint).text)
    meme_image = response['url']

    return meme_image

@app.route('/')
def index():
    meme = get_meme()

    return render_template('index.html', meme_pic=meme)

app.run(host='0.0.0.0', port=80)
