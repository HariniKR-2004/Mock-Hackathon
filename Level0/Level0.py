import json
f = open('C:\Mock_Hackathon\Mock-Hackathon\Level1\level0.json')
data = json.load(f)
f.close()
distances=[]
distances.append([0]+data["restaurants"]["r0"]["neighbourhood_distance"])
count=1
for i in data['neighbourhoods']:
    distances.append([distances[0][count]]+data['neighbourhoods'][i]["distances"])
    count+=1
def TSP(c,cost,path):
    adj_vertex = 99999
    min_val = 99999
    visited[c] = 1
    if c!=0:
        path.append("n"+str(c-1))
    for k in range(len(distances)):
        if (distances[c][k] != 0 and visited[k] == 0):
            if (distances[c][k] < min_val):
                min_val = distances[c][k]
                adj_vertex = k
    if (min_val != 99999):
        cost = cost + min_val
    if (adj_vertex == 99999):
        path.append("r0")
        cost += distances[c][0]
        return
    TSP(adj_vertex,cost,path)
cost=0
visited=[0]*len(distances)
path=["r0"]
TSP(0,cost,path)
output={"v0":{"path":path}}

with open('level0_output.json', 'w') as f:
    json.dump(output, f)