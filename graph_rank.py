import json
import re

titles = open('titles.txt','r').read().split('\n')[:-1]
data = json.load(open('visualize/graph_sicp.json'))
nodes = [i['name'] for i in data['nodes']]
ranks = []
for node in range(1,len(nodes)+1):
    ranks.append([node, 0])
    for i in data['links']:
        if (i['source'] == node) or (i['target'] == node):
            ranks[-1][1] += 1#i['weight']
ranks.sort(key=lambda x: -x[1])

#r = ['<li>%s %.2f</li>\n' %(re.sub('\xc2|\xa0|\xe2|\x80|\x94',' ',titles[i-1]), w) for (i, w) in ranks]
r = ['%d. %s %.2f\n' %(num+1, re.sub('\xc2|\xa0|\xe2|\x80|\x94',' ',titles[i-1]), w) for (num,(i, w)) in enumerate(ranks)]
print ''.join(r)
