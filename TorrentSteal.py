#!/usr/bin/env python

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
["name", "author", "verified_author",
"category", "size", "files", "age",
"seed", "leech", "verified_torrent",
"comments", "torrent_link",
"magnet_link", "download_link"
]
"""



FITNESS_LIST = []

class TorrentCollection:
  def __init__(self, tList):
    self.tList = tList
    self.fitnessList = [0]*len(tList)

  def addTorrent(self,torrent):
    self.tList.append(torrent)

  def removeTorrent(self,position):
    self.tList = self.tList[:position] + self.tList[position+1:]

  def getCollection(self):
    return zip(self.tList, self.fitnessList)

class TargetTorrent:
  def __init__(self, targetName, targetCatagory):
    self.__name = targetName
    self.__category = targetCatagory

  def getName():
    return self.__name

  def getCatagory():
    return self.__category

class FakeTorrent:
    def __init__(self):
        self.name = 'Muse - The 2nd Law [2012-Preview Leak] Mp3-256 NimitMak SilverRG'
        self.author = ''
        self.verified_author = True
        #self.category = CATEGORY.MUSIC
        self.size = ''
        self.files = '20'
        self.age = '5 months'
        self.seed = 0
        self.leech = 0
        self.verified_torrent = True
        self.comments = ''
        self.torrent_link = ''
        self.magnet_link = ''
        self.download_link = 'http://torcache.net/torrent/849C56C4AC28BB84655B5AE8C423F525FCC5E0D3.torrent?title=[kickass.to]caparezza.museica.2014.rtperle'

    def setSeed(self, newSeed):
        self.seed = newSeed


def searchSong(song):
    #Default order is descending, you can specify ascending order:
    for i in Search(song.artist).category(CATEGORY.MUSIC).order(ORDER.SEED):
        FITNESS_LIST.append([getTorrentFitness(i, song),i])
    print("Name:%s\nVerifiedAuthor:%s\nVerifiedTorrent:%s\nFiles:%s\nAge:%s\nLink:%s\n" % (i.name, i.verified_author, i.verified_torrent, i.files, i.age, i.download_link))


class BasicTorrentCheck:
    def checkTorrentName(self, torrentColl, targetTor):
      for tor, fit in torrentColl.getCollection():
        # torrent has proper name check
        searchTerm = r"\b"+targetName+r"\b"
        name = re.search( searchTerm, tor.torrent.name, re.IGNORECASE)
        name_value = 7

        if name:
            print("Name:", name.group(), " Value +",name_value)
            fit += name_value

    def checkVerifiedAuthor(self, torrentCol, targetTor):
      for tor, fit in torrentCol.getCollection():
        ## verified author check
        verifiedAuthor_value = 5

        if tor.verified_author:
            print("Verified:", tor.verified_author, " Value +", verifiedAuthor_value)
            fit += verifiedAuthor_value

    def checkVerifiedTorrent(self, torrentCol, targetTor):
      for tor, fit in torrentCol.getCollection():
        ## verified torrent check
        verifiedTorrent_value = 5

        if tor.verified_torrent:
            print("Verified:", tor.verified_torrent, " Value +", verifiedTorrent_value)
            fit += verifiedTorrent_value

    def checkTorrentSeeders(self, torrentCol, targetTor):
        for tor,fit in torrentCol.getCollection():
            ## check relative seeder value
            print(tor.name,fit)


    def performAllChecks(self, torrentCol, targetTor):
        return

if __name__ == "__main__":
    # name, artist, album
    song = SongUtil.Song("Mk Ultra", "Muse", "The Resistance")
    #searchSong(song)

    tList = []
    fitness = 0

    for i in range(10):
        temp = FakeTorrent()
        temp.setSeed(random.randint(1,100))
        tList.append(temp)
    tors = TorrentCollection(tList)

    testTarget = FakeTorrent().setSeed(55)

    test = BasicTorrentCheck()
    test.checkTorrentSeeders(tors, testTarget)
