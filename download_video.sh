#!/usr/bin/env bash
url="https://manifest.googlevideo.com/api/manifest/hls_playlist/id/pSmFu168XUk.1/itag/93/source/yt_live_broadcast/requiressl/yes/ratebypass/yes/live/1/cmbypass/yes/goi/160/sgoap/gir%3Dyes%3Bitag%3D140/sgovp/gir%3Dyes%3Bitag%3D134/hls_chunk_host/r1---sn-hhp-45gl.googlevideo.com/playlist_type/DVR/ei/EGmfXL2CD9fjigSt_4CgBg/gcr/us/mm/32/mn/sn-hhp-45gl/ms/lv/mv/u/pl/16/dover/11/keepalive/yes/mt/1553950287/disable_polymer/true/ip/138.247.111.59/ipbits/0/expire/1553972592/sparams/ip,ipbits,expire,id,itag,source,requiressl,ratebypass,live,cmbypass,goi,sgoap,sgovp,hls_chunk_host,playlist_type,ei,gcr,mm,mn,ms,mv,pl/signature/1EF4F1B1FDA1632BAABD07BC270315DAED7982C8.40382DE514BA4777631134DEBB78F3BA1CC53EB1/key/dg_yt0/playlist/index.m3u8"

file="video/$1.mkv"
streamlink "$url" best -o "$file"
