from flask import Flask, render_template
import requests

app = Flask(__name__)

def get_meme():

    meme_endpoint = 'https://meme-api.com/gimme'
    response = requests.get(meme_endpoint).json()
    meme_pic = response['preview'][-1]
    subreddit = response['subreddit']
    post_link = response['postLink']
    title = response['title']

    return meme_pic, subreddit, post_link, title

@app.route('/')
def index():
    meme_pic, subreddit, post_link, title = get_meme()

    return render_template('index.html', meme_pic=meme_pic, post_link=post_link, subreddit=subreddit, title=title)

app.run(host='0.0.0.0', port=5000)
