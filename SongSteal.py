# extra libs
#from KickassAPI import Search, Latest, CATEGORY, ORDER, Torrent

# total imports
import SongUtil
import time
import re
import math
import random

# standard imports
from sys import argv
from datetime import date


"""
#Specify category
Search("Game of thrones").category(CATEGORY.MOVIES)

#Feel free to chain these, but remember that order or category resets page to 1
Search("Game of thrones").category(CATEGORY.GAMES).order(ORDER.FILES_COUNT).next()

#Latest has the same behaviour as Search but lacks the ```category()``` method and has no query string
for t in Latest().order(ORDER.SEED):
t.lookup()

#Page, order and category can be also specified in constructor
Search("Game of thrones", category=CATEGORY.GAMES, order=ORDER.AGE, page=5)

#Get results from multiple pages
for t in Latest().order(ORDER.AGE).pages(3,6):
t.lookup()

#Get results from all pages starting with the actual page
for t in Latest().all():
t.lookup()

#Get list of torrent objects instead of iterator
Latest().list()

#pages(), all() and list() cant be followed by any other method!
"""

"""
["name", "author", "verified_author",
"category", "size", "files", "age",
"seed", "leech", "verified_torrent",
"comments", "torrent_link",
"magnet_link", "download_link"
]
"""



FITNESS_LIST = []

class FakeTorrent:
    def __init__(self, seed):
        self.name = 'Muse - The 2nd Law [2012-Preview Leak] Mp3-256 NimitMak SilverRG'
        self.author = ''
        self.verified_author = True
        #self.category = CATEGORY.MUSIC
        self.size = ''
        self.files = '20'
        self.age = '5 months'
        self.seed = seed
        self.leech = 55
        self.verified_torrent = True
        self.comments = ''
        self.torrent_link = ''
        self.magnet_link = ''
        self.download_link = 'http://torcache.net/torrent/849C56C4AC28BB84655B5AE8C423F525FCC5E0D3.torrent?title=[kickass.to]caparezza.museica.2014.rtperle'


def searchSong(song):
    #Default order is descending, you can specify ascending order:
    for i in Search(song.artist).category(CATEGORY.MUSIC).order(ORDER.SEED):
        FITNESS_LIST.append([getTorrentFitness(i, song),i])
    print("Name:%s\nVerifiedAuthor:%s\nVerifiedTorrent:%s\nFiles:%s\nAge:%s\nLink:%s\n" % (i.name, i.verified_author, i.verified_torrent, i.files, i.age, i.download_link))

def checkTorrentName(torrent, fitness, targetName):
    ## torrent has proper name check
    searchTerm = r"\b"+targetName+r"\b"
    name = re.search( searchTerm, torrent.name, re.IGNORECASE)
    name_value = 7
    if name:
        print("Name:", name.group(), " Value +",name_value)
        fitness += name_value

def checkVerifiedAuthor(torrent, fitness):
    ## verified author check
    verifiedAuthor_value = 5
    if torrent.verified_author:
        print("Verified:", torrent.verified_author, " Value +", verifiedAuthor_value)
        fitness += verifiedAuthor_value

def checkVerifiedTorrent(torrent, fitness):
    ## verified torrent check
    verifiedTorrent_value = 5
    if torrent.verified_torrent:
        print("Verified:", torrent.verified_torrent, " Value +", verifiedTorrent_value)
        fitness += verifiedTorrent_value

def checkTorrentSeeders(targetTorrent, fitness, torrentList):
    ## check relative seeder value
    seedList = []
    for torrent in torrentList:
        seedList.append(int(torrent.seed))

    cValue = int(targetTorrent.seed)
    tMax = max(seedList)
    tMedian = sum(seedList) / len(seedList)

    if tMax == cValue:
        fitness += 5

    else:




def getSeeds(torrent):
    return torrent.seed

def getTorrentFitness(torrent, song):
    fitness = 0

    # Verified? +5
    if torrent.verified_author:
        fitness += 5

    if torrent.verified_torrent:
        fitness += 5

    # \b(torrent.name)\b
    # Album name? +10
    album_values = [r'\b(torrent.name)\b', 10]

    # Album year? +5
    albumYear = 2014 # need this value
    year_values = [r'\b(19|20)\d{2}\b', 5]
    dtNumber, dtUnit = torrent.age.split(" ")
    unit = ['year', 'month', 'day']
    value = [1, 12, 365]
    for i in range(len(unit)):
        if dtUnit == unit[i]:
            if (date.today().year - round((int(dtNumber)/value[i]))) == albumYear:
                fitness += 5

    # file_type:((mp3)|(flac)), quality:(\d{3}Kbps), year:(\D|)(20\d{2})\D|(\D|)(19\d{2}\D)
    #keywords_values = [[r'(mp3)|(flac)', 3], [r"/d{3}Kbps", math.log(int(re.search(r'\b\d{3}\D', torrent.name).group()),2)], ["flac", 5]]
    # keywords?


    return fitness

if __name__ == "__main__":
    # name, artist, album
    song = SongUtil.Song("Mk Ultra", "Muse", "The Resistance")
    #searchSong(song)

    tList = []
    fitness = 0

    for i in range(10):
        tList.append(FakeTorrent(random.randint(1,100)))

    checkTorrentSeeders(tList, fitness)
