#!/usr/bin/env python3
import json
import sqlite3
import os
import shutil
from PIL import Image
from multiprocessing import Pool
import subprocess
import sys

def insert_scores(img_name, scores):
    frame = int(img_name.split('-')[-1].split('.')[0])
    score_values = []
    for team in range(NUM_TEAMS):
        for service in range(NUM_SERVICES):
            score_values.append((frame, team, service, scores[team][service]))

    conn = sqlite3.connect('scores.db')
    c = conn.cursor()
    c.executemany('INSERT INTO scores (frame, team, service, result) VALUES (?,?,?,?)', score_values)
    conn.commit()
    conn.close()

def calc_score_img(img_name):
    global origin, xsp, ysp, NUM_TEAMS, NUM_SERVICES
    img = Image.open(img_name)
    pix = img.load()

    scores = {}
    for team in range(NUM_TEAMS):
        scores[team] = {}
        for service in range(NUM_SERVICES):
            coord = (origin[0]+xsp*team, origin[1]+ysp*service)
            red = pix[coord[0], coord[1]][0]
            if red > 200:
                scores[team][service] = 0
            else:
                scores[team][service] = 1
    insert_scores(img_name, scores)
    return scores

def calc_score_imgs(img_names):
    #p = Pool(1)
    #p.map(calc_score_img, img_names)
    for img in img_names:
        print(img)
        calc_score_img(img)

if __name__ == '__main__':
    with open('config.json', 'r') as f:
        cfg = json.load(f)
    origin = cfg['origin']
    xsp = cfg['x_space']
    ysp = cfg['y_space']
    NUM_TEAMS = cfg['teams']
    NUM_SERVICES = cfg['services']

    imgs = ['img/'+f for f in os.listdir('img') if 'bmp' in f]
    imgs.sort()
    print('Calculating scores')
    calc_score_imgs(imgs)

    print('Cleaning up files')
    for img in imgs:
        os.remove(img)
