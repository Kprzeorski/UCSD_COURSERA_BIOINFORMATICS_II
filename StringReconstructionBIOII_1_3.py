# UCSD-COURSERA bioinformatics II course: 1.3 StringReconstruction

# python 3.7.2

f = open("Hamiltonian.txt", "r")
testSet = f.read().splitlines()


def findStartingIndex(Texts):
    
    graph = {}
    k = len(Texts[0])
    for i in range(0,len(Texts)): 
        for j in range(0,len(Texts)):
            
            firstmatch = -1
            matching = False            
            d2 = 0
            
            for d in range(1,k):
                if Texts[i][d] == Texts[j][d2]:
                    if matching == False:
                        matching = True
                        firstmatch = d
                        d2 += 1
                    elif matching == True:
                        d2 += 1
                else:
                    d2 = 0
                    matching = False
                    firstmatch = -1
                    break

            if firstmatch != -1:
                if Texts[i] not in graph:
                    graph[Texts[i]] = [Texts[j]]
                else:
                    graph[Texts[i]].append(Texts[j])        
    
    return graph


preliminaryGraph = findStartingIndex(testSet)
graph = {}

# remove any destinations that counted more than once
for k, v in preliminaryGraph.items():
    if k not in graph:
        graph[k] = []
        for item in v:
            if item not in graph[k]:
                graph[k].append(item)

# sort the list of destinations for each node
for node, value in graph.items():
    graph[node].sort()

# pretty printing
for node, destinations in graph.items():
    print(node, "->", ','.join(str(item) for item in destinations))
    
    
    
# def seek(current node, the current path, the graph/adjacency list )
def seek(current, path, graph):
    
    # if current node has not been visited, add to path
    if current not in path:
        path.append(current)
        # all nodes in path are unique and if 16 nodes, then done
        if len(path) == 16:
            return "success", path
    else:
        return "fail", path
        
    for node in graph[current]:
        status, path = seek(node, path, graph)
        if status == "success":
            break #break this loop
    
    return status, path


# begin searching for 4-universal string
for node, value in graph.items():
    status, path = seek(node, [], graph)
    if status == "success":
        break # break this loop
        
print(status, path)
# 0 1 2 4 8 9 3 6 12 13 10 5 11 7 14 15    
