class Artist:
    """class that re present the artist its self
    
    Attr : 
        _name (str) = artist name
        albumsList (list) = artist albums list that contain album object

    Method :
        addAlbum (object) = artist can add his albums by her ownself
    """

    def __init__(self, name: str):
        self._name = name
        self.albumsList = []

    def addAlbum(self, album: object):
        self.albumsList.append(album)

class Album:
    """Class for each Album
    
    Attr : 
        _name (str) = albums name
        _artist (object) = album his own authors, contain object
        _year (int) = the album year information
        songsList = songs list that contain song object

    Methods :
        addSongs (object) = albums can add his own song list
    """
    def __init__(self, name: str, year: int, artist: object=None):
        self._name = name
        if artist is  None:
            self.artist = Artist("Various Artist")
        else:
            self.artist = artist
        self._year = year
        self.songsList = []

    def addSongs(self, song: object, position: int=0):
        # self.songsList.append(song)  # I made a mistake here !!!
        if position is None:
            self.songsList.append(song)
        else:
            self.songsList.insert(position, song)


class Song:
    """Class that contain each song information 
    
    Attr : 
        _name (str) = song name
        _artist (object) = song's his own artist
        _duration (int) = song's duration

    Methods : -
    """
    def __init__(self, name: str, artist: object, duration: int=0):
        self._name = name
        self._artist = artist
        self._duration = duration


def checkItem(checkitem, listItem: list):
    """Check list engine"""
    for item in listItem:
        if item._name == checkitem:
            return item
    return None


def writeText(listToWrite: list):
    with open("checkFinalFile.txt", "w") as finalFile:
        for artist in listToWrite:
            for album in artist.albumsList:
                for song in album.songsList:
                    print("{0._name} {1._name} {1._year} {2._name}".format(artist,album,song), file=finalFile)


def loadSongs() -> list:
    newArtist = None
    newAlbum = None
    artistList = []

    # testData = []
    with open("albums.txt", "r") as data:
        # for line in data:
        #     testData.append(line)
        for line in data:
            artistData, albumsData, yearData, songData = tuple(line.strip("\n").split("\t"))
            # print(f"{artistData} :: {albumsData} ::  {yearData} :: {songData}")

            # =============== begin scan ===============
            if newArtist == None:
                newArtist = Artist(artistData)
                artistList.append(newArtist)
            elif newArtist._name != artistData:
                newArtist = checkItem(artistData, artistList)
                if newArtist == None:
                    newArtist = Artist(artistData)
                    artistList.append(newArtist)
                newAlbum = None

            # ============== begin scan each album ============
            if newAlbum == None:
                newAlbum = Album(albumsData, newArtist._name, yearData)
                newArtist.addAlbum(newAlbum)
            elif newAlbum._name != albumsData:
                newAlbum = checkItem(albumsData, newArtist.albumsList)
                if newAlbum == None:
                    newAlbum = Album(albumsData, newArtist._name, yearData)
                    newArtist.addAlbum(newAlbum)

            newSong = Song(songData, newArtist)
            newAlbum.addSongs(newSong)

    return artistList
        

    # print(testData)

def main():
    """songsRemake.py main engine"""
    print(f"There is : {len(loadSongs())} artist")
    writeText(loadSongs())


if __name__ == "__main__":
    main()