#!/bin/bash
workon songsteal1
a= 0
if [$# > $a]; then
  python SongSteal.py $*
else
  python SongSteal.py
fi
