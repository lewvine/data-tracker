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

# Returns the first JSON object in the collection:
for m in video_games_dict:
    video_game = VideoGame.video_game_decoder(m)
    video_games_list.append(video_game)


def rank(game):
    return game.rank


top_ten = sorted(video_games_list, key=rank)


@bp.route('/', methods=('GET', 'POST'))
def index():
    return render_template("video_games/index.html", video_games=top_ten)


@bp.route('/display', methods=('GET', 'POST'))
def display():
    search_for_title = request.args['search_for_title']
    this_game_list = []
    for v in video_games_list:
        if v.name == search_for_title:
            this_game_list.append(v)
        else:
            continue
    if len(this_game_list) != 0:
        return render_template("video_games/display.html", video_game=this_game_list[0], this_game_list=this_game_list)


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


@bp.route('/consoles')
def console_sales():
    ds_sales = 0
    x360_sales = 0
    ps3_sales = 0
    ps4_sales = 0
    labels = ["3DS", "Xbox 360", "PS3", "PS4"]
    for v in video_games_list:
        if v.year is None:
            continue
        else:
            if v.platform == '3DS' and v.year >= 2013:
                ds_sales += v.global_sales
            elif v.platform == 'X360' and v.year >= 2013:
                x360_sales += v.global_sales
            elif v.platform == 'PS3' and v.year >= 2013:
                ps3_sales += v.global_sales
            elif v.platform == 'PS4' and v.year >= 2013:
                ps4_sales += v.global_sales
    values = [ds_sales, x360_sales, ps3_sales, ps4_sales]

    return render_template("video_games/consoles.html", labels=labels, values=values)

