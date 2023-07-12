from lib.album import Album

def test_album_constructs():
    album = Album(1, 'Album one', 2023, 1)
    assert album.id == 1
    assert album.title == "Album one"
    assert album.release_year == 2023
    assert album.artist_id == 1

def test_eq_method():
    album = (1, 'Album one', 2023, 1)
    album1 = (1, 'Album one', 2023, 1)
    assert album == album1

def test_repr_method():
    album = Album(1, 'Album one', 2023, 1)
    assert str(album) == "Album(1, Album one, 2023, 1)"