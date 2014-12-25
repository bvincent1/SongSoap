#!/usr/bin/env python

# extra libs
from KickassAPI import Search, Latest, CATEGORY, ORDER, Torrent

# total imports
import SongUtil
import TorrentCatagoryCheck
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

class TorrentUtil:
    @staticmethod
    def printTorrent(torrent):
        print("Name: %s" % (torrent.name))
        print("Verified Author: %s" % (torrent.verified_author))
        print("Verified Torrent: %s" % (torrent.verified_torrent))
        print("Files: %s" % (torrent.files))
        print("Age: %s" % (torrent.age))
        print("Link: %s" % (torrent.download_link))

class TorrentCollection:
    def __init__(self, tList):
        self.tList = tList
        self.fitnessList = [0]*len(tList)

    def addTorrent(self,torrent):
        self.tList.append(torrent)
        self.fitnessList.append(0)

    def removeTorrent(self,position):
        self.tList = self.tList[:position] + self.tList[position+1:]
        self.fitnessList = self.fitnessList[:position] + self.fitnessList[position+1:]

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
        self.category = CATEGORY.MUSIC
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

class BasicTorrentCheck:
    def checkVerifiedAuthor(self, torrentCol, targetTor, verbose = False):
      for i in range(len(torrentCol.tList)):
        ## verified author check
        verifiedAuthor_value = 7

        if torrentCol.tList[i].verified_author:
            torrentCol.incrFitness(i, verifiedAuthor_value)
            if verbose:
                print(torrentCol.tList[i].name, torrentCol.fitnessList[i])

    def checkVerifiedTorrent(self, torrentCol, targetTor, verbose = False):
      for i in range(len(torrentCol.tList)):
        ## verified torrent check
        verifiedTorrent_value = 5

        if torrentCol.tList[i].verified_torrent:
            torrentCol.incrFitness(i, verifiedTorrent_value)
            if verbose:
                print(torrentCol.tList[i].name, torrentCol.fitnessList[i])

    def checkTorrentSeeders(self, torrentCol, targetTor, verbose = False):
        torrentSeeders_value = 5
        seed_list = [int(tor.seed) for tor,fit in torrentCol.getCollection()]
        maxSeed = float(max(seed_list))
        minSeed = float(min(seed_list))

        diffSeed = (maxSeed - minSeed)/len(seed_list)

        for incr in range(torrentSeeders_value,0,-1):
            for i in range(len(seed_list)):
                if seed_list[i] > maxSeed - (diffSeed * (abs(incr-torrentSeeders_value) + 1)):
                    torrentCol.incrFitness(i, incr)
                    if verbose:
                        print(torrentCol.tList[i].name, torrentCol.fitnessList[i])

    def performAllChecks(self, torrentCol, targetTor, verbose = False):
        self.checkVerifiedTorrent(torrentCol, targetTor, verbose)
        self.checkVerifiedAuthor(torrentCol, targetTor, verbose)
        self.checkTorrentSeeders(torrentCol, targetTor, verbose)

if __name__ == "__main__":
    tors = TorrentCollection([])
    t = Search("Muse").category(CATEGORY.MUSIC).order(ORDER.SEED)

    for i in t:
        try:
            #TorrentUtil.printTorrent(i)
            tors.addTorrent(i)
        except:
            pass

    testTarget = None

    test = BasicTorrentCheck()
    test.performAllChecks(tors, testTarget)

    print([i.seed for i in tors.tList])
    print(tors.fitnessList)
