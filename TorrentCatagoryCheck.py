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

	@classmethod
	def performAllChecks(torrentCol, targetTor):
		m = MusicTorrentCheck()
		m.checkFileNumber(torrentCol, targetTor)


class MovieTorrentCheck:
	fileFormats =["avi", "mp4"]

	def checkFileNumber(self, torrentCol, targetTor):
		return

	@classmethod
	def performAllChecks(torrentCol, targetTor):
		m = MovieTorrentCheck()
		m.checkFileNumber(torrentCol, targetTor)


class TvTorrentCheck:
	fileFormats =["avi", "mp4"]

	def checkFileNumber(self, torrentCol, targetTor):
		return

	@classmethod
	def performAllChecks(torrentCol, targetTor):
		e = EpisodeTorrentCheck()
		e.checkFileNumber(torrentCol, targetTor)

class GameTorrentCheck:
	fileFormats =["zip", "rar", "exe", "dll"]

	def checkFileNumber(self, torrentCol, targetTor):
		return

	@classmethod
	def performAllChecks(torrentCol, targetTor):
		g = GameTorrentCheck()
		g.checkFileNumber(torrentCol, targetTor)
