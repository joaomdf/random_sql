from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository
from lib.database_connection import DatabaseConnection

class Application():
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/music_library.sql")

    def run(self):
        # "Runs" the terminal application.
        # It might:
        #   * Ask the user to enter some input
        #   * Make some decisions based on that input
        #   * Query the database
        #   * Display some output
        # We're going to print out the artists!
        if "2" in text:
            print("\nHere is a list of artists:")
            artist_repository = ArtistRepository(self._connection)
            artists = artist_repository.all()
            for artist in artists:
                print(f"{artist.id}: {artist.name} ({artist.genre})")
        elif "1" in text:
            print("\nHere is a list of albums:")
            album_repository = AlbumRepository(self._connection)
            albums = album_repository.all()
            for album in albums:
                print(f"* {album.id} - {album.title}")

if __name__ == '__main__':
    print("Welcome to the music library manager!\n")
    text = input("What would you like to do?\n1 - List all albums\n2 - List all artists\n")
    app = Application()
    app.run()