import json

data = json.load(open('graph_dirac.json'))
nodes = [i['name'] for i in data['nodes']]
ranks = []
for node in nodes:
    ranks.append(0)
    for i in data['links']:
        if i['source'] == node:
            ranks[-1] += i['weight']
for i in range(len(ranks)):
    print i+1, ranks[i]
