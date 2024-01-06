import json
f = open('C:\Mock_Hackathon\Mock-Hackathon\Level2\level1b.json')
data = json.load(f)
f.close()
distances=[]
distances.append([0]+data["restaurants"]["r0"]["neighbourhood_distance"])
quantities=[]
count=1
for i in data['neighbourhoods']:
    distances.append([distances[0][count]]+data['neighbourhoods'][i]["distances"])
    quantities.append(data['neighbourhoods'][i]["order_quantity"])
    count+=1
capacity=data["vehicles"]["v0"]["capacity"]
def TSP(c,cost,path):
    adj_vertex = 99999
    min_val = 99999
    visited[c] = 1
    path.append("n"+str(c-1))
    for k in index:
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

paths=[]
tempQuantity=list(quantities)
print(quantities)
count=0
while max(tempQuantity)>0:
    index=[]
    tempCapacity=capacity
    for i in tempQuantity:
        while max(tempQuantity)>0 and tempCapacity-max(tempQuantity)>=0:
            index.append(tempQuantity.index(max(tempQuantity))+1)
            tempCapacity-=max(tempQuantity)
            tempQuantity[tempQuantity.index(max(tempQuantity))]=-1
    cost=0
    visited=[0]*len(distances)
    path=[]
    print(index,tempCapacity,tempQuantity)
    TSP(0,cost,path)
    path[0]="r0"
    count+=len(path)-2
    paths.append(path)
print(count)
output={"v0":{}}
count=1
for i in range(0,len(paths)):
    string="path"+str(count)
    output["v0"][string]=paths[i]
    count+=1
print(output)
with open('C:\Mock_Hackathon\Mock-Hackathon\Level2\level1b_output.json', 'w') as f:
    json.dump(output, f)