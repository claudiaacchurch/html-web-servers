from playwright.sync_api import Page, expect

# Tests for your routes go here

# === Example Code Below ===

"""
We can get an emoji from the /emoji page
"""
def test_get_emoji(page, test_web_address): # Note new parameters
    # We load a virtual browser and navigate to the /emoji page
    page.goto(f"http://{test_web_address}/emoji")

    # We look at the <strong> tag
    strong_tag = page.locator("strong")

    # We assert that it has the text ":)"
    expect(strong_tag).to_have_text(":)")

# === End Example Code ===

def test_goodbye(page, test_web_address):
    page.goto(f"http://{test_web_address}/goodbye")
    strong_tag = page.locator("strong")
    expect(strong_tag).to_have_text("Bye!")

def test_get_albums(page, test_web_address, db_connection):
    db_connection.seed("seeds/album_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    # testing the a href
    page.click("text=Album one")
    h1_tag = page.locator("h1")
    p_tags = page.locator("p")
    expect(h1_tag).to_have_text("Album one")
    expect(p_tags).to_have_text("Release year: 2023 Artist: ABBA")

    #testing just all albums
    '''expect(p_tags).to_have_text([
        "Title: Album one", 
        "Released: 2023",
        "Title: Album two",
        "Released: 2000",
        "Title: Album three",
        "Released: 2011"
    ])'''

def test_get_album_with_id_1(page, test_web_address, db_connection):
    db_connection.seed("seeds/album_library.sql")
    page.goto(f"http://{test_web_address}/albums/1")
    h1_tag = page.locator("h1")
    p_tags = page.locator("p")
    print(page.locator("body").inner_html())
    expect(h1_tag).to_have_text("Album one")
    expect(p_tags).to_have_text("Release year: 2023 Artist: ABBA")

def test_get_artist_with_id_1(page, test_web_address, db_connection):
    db_connection.seed("seeds/artist_repository.sql")
    page.goto(f"http://{test_web_address}/artists/1")
    p_tags = page.locator('p')
    expect(p_tags).to_have_text(["Artist: ABBA", "Genre: pop"])

def test_get_artists_returns_all_artists(page, test_web_address, db_connection):
    db_connection.seed("seeds/artist_repository.sql")
    page.goto(f"http://{test_web_address}/artists")
    h1_tags = page.locator('h1')
    p_tags = page.locator('p')
    expect(h1_tags).to_have_text([
        "ABBA",
        "Pixies",
        "Taylor Swift",
        "Nina Simone"
    ])
    expect(p_tags).to_have_text([
        "Genre: pop",
        "Genre: rock",
        "Genre: pop",
        "Genre: r&b"
    ])

def test_form_adds_new_album(page, test_web_address, db_connection):
    db_connection.seed("seeds/album_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text=Add a new album") # goes to albums/ create (GET)
    page.fill("input[name='title']", "Insane in the membrane")
    page.fill("input[name='release_year']", '1993')
    page.click("text=Create Album") # /albums
    title = page.locator(".t-title")
    expect(title).to_have_text(["Title: Album one", "Title: Album two", "Title: Album three", "Title: Insane in the membrane"])
    release_year = page.locator(".t-release-year")
    expect(release_year).to_have_text(["Released: 2023", "Released: 2000", "Released: 2011", "Released: 1993"])

"""def test_artists_create_route(page, test_web_address, db_connection):
    db_connection.seed("seeds/artist_repository.sql")
    page.goto(f"http://{test_web_address}/artists")
    page.click("text=Add new Artist")
    name = page.locator(".form-name")
    expect(name).to_have_text("")
    genre = page.locator(".form-genre")
    expect(genre).to_have_text("")"""


def test_form_adds_new_artist(page, test_web_address, db_connection):
    db_connection.seed("seeds/artist_repository.sql")
    page.goto(f"http://{test_web_address}/artists")
    page.click("text=Add a new artist") # goes to artists/ create (GET)
    page.fill("input[name='name']", "Cyrpus Hill")
    page.fill("input[name='genre']", 'hiphop')
    page.click("text=Create Artist") # /artists
    h1_tag = page.locator('h1')
    p_tags = page.locator('p')
    expect(h1_tag).to_have_text(["ABBA", "Pixies", "Taylor Swift", "Nina Simone", "Cyrpus Hill"])
    expect(p_tags).to_have_text(["Genre: pop", "Genre: rock", "Genre: pop", "Genre: r&b", "Genre: hiphop"])
