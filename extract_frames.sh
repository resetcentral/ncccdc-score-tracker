#!/usr/bin/env bash
num=$(cat img/last.txt)
num=$(($num+1))
ffmpeg -i "$1" -vf fps=1 -start_number $num "img/ccdc-%05d.bmp"

last_file=$(ls img | tail -n 2 | head -n 1)
num=$(echo $last_file | cut -d '-' -f 2 | cut -d '.' -f 1)
echo $num > img/last.txt
