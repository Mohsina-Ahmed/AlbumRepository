from lib.album import *

class AlbumRepository:
    def __init__(self, db_connection):
        self._db_connection = db_connection

    def all(self):
        rows = self._db_connection.execute("SELECT * FROM albums")
        albums = []
        for row in rows:
            album = Album(row["id"], row["title"], row["release_year"], row["artist_id"])
            albums.append(album)
        return albums
    
    def find(self, album_id):
        rows = self._db_connection.execute("SELECT * FROM albums WHERE id=%s", [album_id])
        row = rows[0]
        return Album(row['id'], row['title'], row['release_year'], row['artist_id'])
    
    def create(self, album):
        self._db_connection.execute("INSERT INTO albums(id, title, release_year, artist_id) VALUES(%s, %s, %s, %s)", [album.id, album.title, album.release_year, album.artist_id])
        return None
    
    def delete(self, album_id):
        self._db_connection.execute("DELETE FROM albums WHERE id = %s", [album_id])
        return None