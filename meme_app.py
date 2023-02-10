from flask import Flask, render_template
import requests

app = Flask(__name__)

def get_meme():
    """
    get a random meme from a random subreddit.
    returns the highest res preview of the meme.
    """

    meme_endpoint = 'https://meme-api.com/gimme'
    response = requests.get(meme_endpoint).json()
    meme_pic = response['preview'][-1]
    return meme_pic


@app.route('/')
def index():
    """rendering the homepage of the website with the meme in it"""

    meme_pic = get_meme()
    return render_template('index.html', meme_pic=meme_pic)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=443)
