#!/usr/bin/env python3
import sqlite3

conn = sqlite3.connect('scores.db')
c = conn.cursor()

count = 0
scores = {}
for frame,team,service,result in c.execute('SELECT * FROM scores'):
    if not team in scores:
        scores[team] = 0
    scores[team] += result
    count += 1

for team in scores.keys():
    #print('Team {0:02d}: {1:0.2f}, {2}'.format(team+1, scores[team] / 17, scores[team] / (count/8)*100))
    print('Team {0:02d}: {1:0.2f}'.format(team+1, scores[team] / (count/8)*100))
