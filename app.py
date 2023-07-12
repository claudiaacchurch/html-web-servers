import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.artist_repository import ArtistRepository
# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==


# == Example Code Below ==

# GET /emoji
# Returns a smiley face in HTML
# Try it:
#   ; open http://localhost:5000/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    # We use `render_template` to send the user the file `emoji.html`
    # But first, it gets processed to look for placeholders like {{ emoji }}
    # These placeholders are replaced with the values we pass in as arguments
    return render_template('emoji.html', emoji=':)')

@app.route('/goodbye')
def say_goodbye():
    return render_template('goodbye.html')
    
# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

@app.route("/albums")
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = []
    for album in repository.all():
        albums.append(album)
    return render_template("albums.html", albums=albums)

@app.route("/albums/<id>")
def get_album(id):
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album, artist = repository.find_album_by_id(id)
    return render_template("albums2.html", album = album, artist=artist)

@app.route("/albums", methods=['POST'])
def add_new_album():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    title = request.form['title']
    release_year = request.form['release_year']
    repository.create(title, release_year, 1)
    return redirect("/albums")

@app.route("/albums/create")
def create_album():
    return render_template("create_album.html")

@app.route("/artists/<id>")
def get_artist_by_id(id):
    connection = get_flask_database_connection(app)
    repo = ArtistRepository(connection)
    artist = repo.find(id)
    return render_template("artist.html", artist=artist)

@app.route("/artists")
def get_all_artists():
    connection = get_flask_database_connection(app)
    repo = ArtistRepository(connection)
    artists = []
    for artist in repo.all():
        artists.append(artist)
    return render_template("all_artists.html", artists=artists)

@app.route("/artists", methods=['POST'])
def create_artist_post():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    name = request.form['name']
    genre = request.form['genre']
    repository.create(name, genre)
    return redirect("/artists")


@app.route("/artists/create")
def create_artist():
    return render_template('create_artist.html')

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
