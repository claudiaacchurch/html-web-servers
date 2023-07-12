from lib.artist import Artist

def test_artist_constructs():
    artist = Artist(1, 'ABBA', 'pop')
    assert artist.id == 1
    assert artist.name == "ABBA"
    assert artist.genre == "pop"

def test_eq_method():
    artist = Artist(1, 'ABBA', 'pop')
    artist2 = Artist(1, 'ABBA', 'pop')
    assert artist == artist2

def test_repr_method():
    artist = Artist(1, 'ABBA', 'pop')
    assert str(artist) == "Artist(1, ABBA, pop)"