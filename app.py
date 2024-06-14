from flask import Flask, render_template, request
from utils import get_playlist_duration

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    duration = None
    if request.method == 'POST':
        playlist_url = request.form['playlist_url']
        duration = get_playlist_duration(playlist_url)
    return render_template('index.html', duration=duration)

if __name__ == '__main__':
    app.run(debug=True)
