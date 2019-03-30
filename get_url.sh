#!/usr/bin/env bash
stream="$1"
url=$(youtube-dl -f 93 -g "$stream" | tail -n 1)
echo $url
