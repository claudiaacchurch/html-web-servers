from lib.artist_repository import ArtistRepository
from lib.artist import Artist

def test_get_all_artists(db_connection):
    db_connection.seed("seeds/artist_repository.sql")
    repo = ArtistRepository(db_connection)
    result = repo.all()
    assert result == [
        Artist(1, 'ABBA', 'pop'),
        Artist(2, 'Pixies', 'rock'),
        Artist(3, 'Taylor Swift', 'pop'),
        Artist(4, 'Nina Simone', 'r&b')
    ]

def test_create_artist(db_connection):
    db_connection.seed("seeds/artist_repository.sql")
    repo = ArtistRepository(db_connection)
    repo.create("Bob Marley", "reggae")
    result = repo.all()
    assert len(result) == 5
    assert result[-1] == Artist(5, "Bob Marley", "reggae")

def test_find_artist_by_id(db_connection):
    db_connection.seed("seeds/artist_repository.sql")
    repo = ArtistRepository(db_connection)
    result = repo.find(1)
    assert result == Artist(1, 'ABBA', 'pop')
