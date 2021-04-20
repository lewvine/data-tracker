from flask import json, request, redirect, flash, render_template, url_for, Blueprint
from datatracker.models.video_game import VideoGame
import requests

bp = Blueprint('video_games', __name__)

video_games_list = []
response = requests.get('https://api.dccresource.com/api/games')

# Returns a single JSON object based on an HTTP GET requests content section.
video_games_content = response.content

# Returns an iterable list of JSON objects with a unqiue index.
video_games_dict = json.loads(video_games_content)
video_games = ["one game", "two games"]

# Returns the first JSON object in the collection:
for m in video_games_dict:
    video_game = VideoGame.video_game_decoder(m)
    video_games_list.append(video_game)


@bp.route('/', methods=('GET', 'POST'))
def index():
    return render_template("video_games/index.html", video_games=video_games_list)


@bp.route('/display', methods=('GET', 'POST'))
def display():
    search_for_title = request.args['search_for_title']
    for v in video_games_list:
        if v.name == search_for_title:
            return render_template("video_games/display.html", video_game=v)
        else:
            continue
        # render_template("video_games/index.html")

@bp.route('/postform', methods=('GET', 'POST'))
def postform():
    if request.method == 'POST':
        title = request.form['title']
        i = 0
        while i < len(video_games_list):
            if video_games_list[i].name == title:
                return render_template("video_games/index.html", video_games=video_games_list[i])
            else:
                i += 1
    else:
        return render_template('video_games/postform.html', page_title="PostForm from Module Function")

