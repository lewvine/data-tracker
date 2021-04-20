from flask import json, request, redirect, flash, render_template, url_for, Blueprint
from datatracker.models.video_game import VideoGame
import requests

bp = Blueprint('video_games', __name__)


@bp.route('/')
def index():
    movies_list = []
    # Returns a JSON Object from an API Request, is successful
    response = requests.get('https://api.dccresource.com/api/games')

    # Returns a single JSON object based on an HTTP GET requests content section.
    video_games_content = response.content

    # Returns an iterable list of JSON objects with a unqiue index.
    video_games_dict = json.loads(video_games_content)
    video_games = ["one game", "two games"]

    # Returns the first JSON object in the collection:
    for m in video_games_dict:
        video_game = VideoGame.video_game_decoder(m)
        movies_list.append(video_game)
    bob = ["this"]
    return render_template("video_games/index.html", video_games=movies_list)

# @bp.route('/postform', methods=('GET', 'POST'))
# def other_example():
#     response = requests.get('https://api.dccresource.com/api/games')
#     video_games_list = response.content
#
#     if request.method == 'POST':
#         page_title = request.form['title']
#         error = None
#
#         if not page_title:
#             error = 'You must enter a title'
#
#         if error is not None:
#             flash(error)
#         elif request.form['title'] == "go home":
#             return redirect(url_for('sample.index'))
#         else:
#             return render_template('sample/postform.html', page_title=page_title)
#
#     else:
#         return render_template('sample/postform.html', page_title="PostForm from Module Function")
#
