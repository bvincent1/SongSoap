import xml.etree.ElementTree as ET

FILE_NAME = "song.xml"

class Song:
	def __init__(self, s_name, s_artist, s_album):
		self.name = str(s_name)
		self.artist = str(s_artist)
		self.album = str(s_album)

class Playlist:
	def __init__(self, p_name, p_songs = []):
		self.name = p_name
		self.songs = p_songs

	def add(self, p_song):
		self.songs.append(p_song)

	def add(self, p_songs):
		for i in p_songs:
			self.songs.append(i)

	def printPlaylist(self):
		print("  Playlist: %s" % self.name)
		for i in self.songs:
			print("    %s by %s from %s" % (i.name, i.artist, i.album))

DATA_FORMAT = """
 data
  playlist (name)
   song (name, artist, album)
"""

def updatePlaylist(newPlaylist):
	try:
		tree = ET.parse(FILE_NAME)
		root = tree.getroot()
	except:
		root = ET.Element('data')

	playlist = None

	for playlist in root.findall("playlist"):
		if playlist.get("name") == newPlaylist.name:
			break

	if playlist == None:
		playlist = ET.SubElement(root, "playlist")
		playlist.set("name", newPlaylist.name)

	UPDATED = False

	for song in newPlaylist.songs:
		for elem in playlist:
			if song.name == elem.get("name"):
				UPDATED = True
				break

		if not UPDATED:
			elem = ET.SubElement(playlist, "song")
		else:
			UPDATED = False


		elem.set("name", song.name)
		elem.set("artist", song.artist)
		elem.set("album", song.album)

	# write the data to the file
	tree = ET.ElementTree(root)
	tree.write(FILE_NAME)

def getPlaylist():
	tree = ET.parse(FILE_NAME)
	root = tree.getroot()

	playlistList = []
	songList = []

	for playlist in root.findall("playlist"):
		for song in playlist.findall("song"):
			songList.append(Song(song.get("name"), song.get("artist"), song.get("album")))
		playlistList.append(Playlist(playlist.get("name"), songList))

	if playlistList != []:
		return playlistList
	else:
		return None

def getPlaylist(name):
	lists = getPlaylists()
	for i in lists:
		if i.name == name:
			return i
	return None

if __name__ == "__main__":
	print("***TEST***")
	songs = Playlist("test1", [Song("test1", "test1", "test1"), Song("test2", "test2", "test2")])
	updatePlaylist(songs)

	getPlaylists()[0].printPlaylist()
