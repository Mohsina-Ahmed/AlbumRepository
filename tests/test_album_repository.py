from lib.album_repository import *
from lib.album import *

"""
When I call the #all on the AlbumRepository
I get all the albums back in a list
"""
def test_list_all_albums(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)
    result = repository.all()
    assert result[0] == Album(1, 'Doolittle', 1989, 1)
    assert result[1] == Album(2, 'Surfer Rosa', 1988, 1)
    # assert result == [
    #     Album(1, 'Doolittle', '1989', 1),
    #     Album(2, 'Surfer Rosa', '1988', 1),
    #     Album(3, 'Waterloo', '1974', 2),
    #     Album(4, 'Super Trouper', '1980', 2),
    #     Album(5, 'Bossanova', '1990', 1),
    #     Album(6, 'Lover', '2019', 3),
    #     Album(7, 'Folklore', '2020', 3),
    #     Album(8, 'I Put a Spell on You', '1965', 4),
    #     Album(9, 'Baltimore', '1978', 4),
    #     Album(10, 'Here Comes the Sun', '1971', 4),
    #     Album(11, 'Fodder on My Wings', '1982', 4),
    #     Album(12, 'Ring Ring', '1973', 2)
    # ]
''''
When I call #find on the album_repository with an Id
I get album corresponding to that Id back
'''
def test_find(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)
    result = repository.find(3)
    assert result == Album(3, 'Waterloo', 1974, 2)


'''
When I add item #create on the album_repository with Id, title, release_year
and artist_id, and I call all I see all of the items including the new insertion
'''

def test_create_album(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)
    album = Album(13, "New song", 2023, 2)
    assert repository.create(album) is None
    assert repository.all() == [
        Album(1, 'Doolittle', 1989, 1),
        Album(2, 'Surfer Rosa', 1988, 1),
        Album(3, 'Waterloo', 1974, 2),
        Album(4, 'Super Trouper', 1980, 2),
        Album(5, 'Bossanova', 1990, 1),
        Album(6, 'Lover', 2019, 3),
        Album(7, 'Folklore', 2020, 3),
        Album(8, 'I Put a Spell on You', 1965, 4),
        Album(9, 'Baltimore', 1978, 4),
        Album(10, 'Here Comes the Sun', 1971, 4),
        Album(11, 'Fodder on My Wings', 1982, 4),
        Album(12, 'Ring Ring', 1973, 2),
        Album(13, 'New song', 2023, 2)
    ]
'''
When I delete an item to the #delete on the album_repository with Id, title, release_year
and artist_id, and I call all() I should not see the deleted item
'''
def test_delete_album(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)
    repository.delete(3)
    assert repository.all() == [
        Album(1, 'Doolittle', 1989, 1),
        Album(2, 'Surfer Rosa', 1988, 1),
        Album(4, 'Super Trouper', 1980, 2),
        Album(5, 'Bossanova', 1990, 1),
        Album(6, 'Lover', 2019, 3),
        Album(7, 'Folklore', 2020, 3),
        Album(8, 'I Put a Spell on You', 1965, 4),
        Album(9, 'Baltimore', 1978, 4),
        Album(10, 'Here Comes the Sun', 1971, 4),
        Album(11, 'Fodder on My Wings', 1982, 4),
        Album(12, 'Ring Ring', 1973, 2)
    ]