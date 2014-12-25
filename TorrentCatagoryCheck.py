#!/usr/bin/env python

# extra libs
from KickassAPI import CATEGORY, Torrent
import SongUtil


# standard libs
import time
import re
import math

from sys import argv
from datetime import date

class MusicTorrentCheck:
	fileFormats =["mp3","flac", "m4a", "aac", "mp4"]

	def checkFileNumber(self, torrentCol, targetTor):
		return

	def performAllChecks(self, torrentCol, targetTor):
		checkFileNumber(torrentCol, targetTor)


class MovieTorrentCheck:
	fileFormats =["avi", "mp4"]

	def checkFileNumber(self, torrentCol, targetTor):
		return

	def performAllChecks(self, torrentCol, targetTor):
		checkFileNumber(torrentCol, targetTor)


class EpisodeTorrentCheck:
	fileFormats =["avi", "mp4"]

	def checkFileNumber(self, torrentCol, targetTor):
		return

	def performAllChecks(self, torrentCol, targetTor):
		checkFileNumber(torrentCol, targetTor)

class GameTorrentCheck:
	fileFormats =["zip", "rar", "exe"]
	
	def checkFileNumber(self, torrentCol, targetTor):
		return

	def performAllChecks(self, torrentCol, targetTor):
		checkFileNumber(torrentCol, targetTor)
