import graph_generator as gg
import time
from numpy import sin, cos, arccos, pi, round

# In the Algorithms class dfs method(implemented using recursion) make use of the class property,
# hence in the driver code it is mandatory to use different instances(objects) of the class.
class Algorithms:
    def __init__(self):
        self.visited=[]
        self.path=[]

    def dfs(self,graph,start,goal,heuristics=None):
        if len(self.visited)==0:
            self.visited.append(start)
        if start==goal:
            self.path.append(start)
            return
        for i in range(len(graph[start])):
            if graph[start][i][0] not in self.visited:
                self.visited.append(graph[start][i][0])
                temp=self.dfs(graph,graph[start][i][0],goal)
                if goal in self.path:
                    self.path.append(start)
                    return start
                if temp:
                    break

    def ucs(self,graph,start,goal,heuristics=None):
        parent=None
        visited={}
        frontier=[]
        frontier.append((start,0))
        path=[]
        while frontier:
            frontier=sorted(frontier,key= lambda x:x[1],reverse=True)
            current=frontier.pop()
            if current[0]==goal:
                break
            if current[0] not in visited:
                visited[current[0]]=(parent,current[1])
            parent=current
            for i in graph[current[0]]:
                if i[0] not in visited:
                    visited[i[0]]=(parent[0],i[1])
                    frontier.append((i[0],i[1]+parent[1]))
        curr=visited[goal]
        path.append(goal)
        while curr[0]!=None:
            path.append(curr[0])
            curr=visited[curr[0]]
        return path[::-1]
            
    def a_star(self,graph,start,goal,heuristics):
        parent=None
        visited={}
        frontier=[]
        frontier.append((start,heuristics[start]))
        path=[]
        while frontier:
            frontier=sorted(frontier,key= lambda x:x[1],reverse=True)
            current=frontier.pop()
            if current[0]==goal:
                break
            if current[0] not in visited:
                visited[current[0]]=(parent,current[1])
            parent=current
            for i in graph[current[0]]:
                if i[0] not in visited:
                    visited[i[0]]=(parent[0],i[1])
                    frontier.append((i[0],i[1]+parent[1]+heuristics[i[0]]))
        curr=visited[goal]
        path.append(goal)
        while curr[0]!=None:
            path.append(curr[0])
            curr=visited[curr[0]]
        return path[::-1]

    def heuristc_fun(self,start,goal):
        #Read the locations from romenia_locations.txt  file and store it in dictionary.
        line_dict={}
        with open("romenia_locations.txt","r") as file:
            for line in file:
                if line.startswith("City"):
                    continue
                line_lis=line.split()
                line_dict[" ".join(line_lis[:-2])]=(float(line_lis[-2]),float(line_lis[-1]))
        #Iterate over the line_dict and produce the distance in miles between two locations.
        latitude=(line_dict[start][0],line_dict[goal][0])
        longitude=(line_dict[start][1],line_dict[goal][1])
        theta = longitude[0] - longitude[1]
        distance = 60 * 1.1515 * arccos(round(
                (sin(latitude[0]*pi/180) * sin(latitude[1]*pi/180)) + 
                (cos(latitude[0]*pi/180) * cos(latitude[1]*pi/180) * cos(theta*pi/180)),8))*180/pi
        distance=round(distance,2)
        return distance

    # This function will take any algorithm with their start and goal; run it n number of times and return-
    # the average time in MicroSeconds and their solution length.
    def average_calc(self,algorithm,graph,start,goal,n):
        heuristics={}
        with open("romenia_locations.txt","r") as file:
            for line in file:
                if line.startswith("City"):
                    continue
                line_lis=line.split()
                city_name=' '.join(line_lis[:-2])
                heuristics[city_name]=self.heuristc_fun(city_name,goal)        
        total_time=0 
        for i in range(n):

            start_instance=time.perf_counter()
            path=algorithm(graph,start,goal,heuristics)
            end_instance=time.perf_counter()

            span=(end_instance-start_instance)*1000000
            total_time+=span
        avg_time=round(total_time/n,2)
        if (algorithm==self.dfs):
            print("DFS Algorithm")
            return f"Average_time:{avg_time} MicroSeconds\nPath_length:{len(self.path)}\nPath:{self.path[::-1]}\n"
        elif(algorithm==self.ucs):
            print("UCS Algorithm")
            return f"Average_time:{avg_time} MicroSeconds\nPath_length:{len(path)}\nPath:{path}\n"
        elif(algorithm==self.a_star):
            print("A* Search Algorithm")
            return f"Average_time:{avg_time} MicroSeconds\nPath_length:{len(path)}\nPath:{path}\n"

# Driver code:

# graph={"a":[("c",4),("b",5)],"b":[("d",2),("c",3),("a",5)],"c":[("a",4),("b",3)],"d":[("b",2),("e",1)],"e":[("d",1),("f",6)],"f":[("e",1)]}
# heuristics={"a":7,"b":3,"c":1,"d":1,"e":0,"f":4}
# start="a"
# goal="e"
# dfs=Algorithms()

# # dfs.dfs(graph,start,goal)
# # print(dfs.path[::-1])

# # print(dfs.ucs(graph,start,goal))

# # print(dfs.a_star(graph,start,goal,heuristics))
# print(dfs.heuristc_fun("Pitesti","Pitesti"))

