#!/usr/bin/env python

# extra libs
from KickassAPI import Search, Latest, CATEGORY, ORDER, Torrent

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

    def setTorrent(self, i, v):
        self.tList[i] = v

    def setFitness(self, i, v):
        self.fitnessList[i] = v

    def getTorrent(self, i):
        return self.tList[i]

    def getFitness(self, i):
        return self.fitnessList[i]

    def incrFitness(self, i, v):
        self.fitnessList[i] += v

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
    def checkVerifiedAuthor(self, torrentCol, targetTor):
      for tor, fit in torrentCol.getCollection():
        ## verified author check
        verifiedAuthor_value = 5

        if tor.verified_author:
            fit += verifiedAuthor_value

    def checkVerifiedTorrent(self, torrentCol, targetTor):
      for tor, fit in torrentCol.getCollection():
        ## verified torrent check
        verifiedTorrent_value = 5

        if tor.verified_torrent:
            fit += verifiedTorrent_value

    def checkTorrentSeeders(self, torrentCol, targetTor):
        torrentSeeders_value = 5
        seed_list = [int(tor.seed) for tor,fit in torrentCol.getCollection()]
        maxSeed = float(max(seed_list))
        minSeed = float(min(seed_list))

        diffSeed = (maxSeed - minSeed)/len(seed_list)

        for incr in range(torrentSeeders_value,0,-1):
            for i in range(len(seed_list)):
                if seed_list[i] > maxSeed - (diffSeed * (abs(incr-torrentSeeders_value) + 1)):
                    torrentCol.incrFitness(i, incr)


    def performAllChecks(self, torrentCol, targetTor):
        return

if __name__ == "__main__":

    tList = []
    for i in range(10):
        temp = FakeTorrent()
        temp.setSeed(random.randint(1,100))
        tList.append(temp)
    tors = TorrentCollection(tList)

    testTarget = FakeTorrent().setSeed(55)

    test = BasicTorrentCheck()
    test.checkTorrentSeeders(tors, testTarget)
    test.checkVerifiedTorrent(tors, testTarget)
    test.checkVerifiedAuthor(tors, testTarget)
