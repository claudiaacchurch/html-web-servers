from lib.album import Album
from lib.artist import Artist

class AlbumRepository:
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute('SELECT * FROM albums')
        albums = []
        for row in rows:
            album = Album(row['id'], row['title'], row['release_year'], row['artist_id'])
            albums.append(album)
        return albums 
    
    def create(self, title, release_year, artist_id):
        self._connection.execute("INSERT INTO albums (title, release_year, artist_id) "\
                         "VALUES (%s, %s, %s)", [title, release_year, artist_id])
    
    def find_album_by_id(self, album_id):
        rows = self._connection.execute(
            'SELECT albums.id AS album_id, albums.title, albums.release_year, albums.artist_id, artists.id, artists.name AS artist_name, artists.genre '
            'FROM albums '
            'JOIN artists ON artists.id = albums.artist_id '
            'WHERE albums.id = %s', [album_id])
        if rows:
            row = rows[0]
            album = Album(row["album_id"], row["title"], row["release_year"], row['artist_id'])
            artist = Artist(row["id"], row["artist_name"], row['genre'])
            return album, artist
        else:
            return None, None