#!/bin/bash
source venv/bin/activate
a = 0
if [$# > $a]; then
  python TorrentSteal.py $*
else
  python TorrentSteal.py
fi
