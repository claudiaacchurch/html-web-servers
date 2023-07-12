from lib.album import Album
from lib.album_repository import AlbumRepository

def test_all_returns_all(db_connection):
    db_connection.seed("seeds/album_library.sql")
    repo = AlbumRepository(db_connection)
    result = repo.all()
    assert result == [
        Album(1, 'Album one', 2023, 1),
        Album(2, 'Album two', 2000, 2),
        Album(3, 'Album three', 2011, 2)
    ]

def test_create_adds_new_album(db_connection):
    db_connection.seed("seeds/album_library.sql")
    repo = AlbumRepository(db_connection)
    repo.create("Album four", 2034, 2)
    results = repo.all()
    assert results == [
        Album(1, 'Album one', 2023, 1),
        Album(2, 'Album two', 2000, 2),
        Album(3, 'Album three', 2011, 2),
        Album(4, 'Album four', 2034, 2)
    ]