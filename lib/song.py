class Song:

    count=0
    genres=[]
    artists=[]
    genre_count={}
    artist_count={}

    def __init__(self,name,artist,genre):
        self.name=name 
        self.artist=artist
        self.genre=genre
        Song.add_song_to_count()
        Song.add_to_genres()
        Song.add_to_artists()

    def add_song_to_count(cls):
        cls.count+=1

    def add_to_genres(cls):
        if cls.genre not in cls.genres:
            cls.genres.append(cls.genre)

        if cls.genre in cls.genre_count:
            cls.genre_count[cls.genre] += 1
        else:
            cls.genre_count[cls.genre] = 1

    def add_to_artists(cls):
        if cls.artist not in cls.artists:
            cls.artists.append(cls.artist)

        if cls.artist in cls.artist_count:
            cls.artist_count[cls.artist] += 1
        else:
            cls.artist_count[cls.artist] = 1

    def add_to_genre_count(cls):
        for genre in cls.genres:
            if genre not in cls.genre_count:
                cls.genre_count[genre]=0
        
        for song in cls:
            cls.genre_count[song.genre] += 1

    def add_to_artist_count(cls):
        for artist in cls.artists:
            if artist not in cls.artist_count:
                cls.artist_count[artist]=0

        for song in cls:
            cls.artist_count[song.artist] += 1

    
