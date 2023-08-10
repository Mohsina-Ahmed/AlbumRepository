from lib.album import *

"""
Connect to the music library database
Connect to the albums table
Create one album instance
with the id, title, release_year, artist_id
"""

def test_make_an_album():
    id = 1
    title = "Doolittle"
    release_year = 1989
    artist_id = 1
    album = Album(id, title, release_year, artist_id)
    album_copy = Album(id, title, release_year, artist_id)
    assert album == album_copy

def test_formatting():
    album = Album(1, "Doolittle", 1989, 1)
    assert str(album) == "Album(1, 'Doolittle', 1989, 1)"