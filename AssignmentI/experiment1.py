import graphs
import Search_algorithms as sa
# The romenia graph we populated on the 'graphs.py'.
graph=graphs.Romenia()
graph.add()
graph=graph.romenia.graph

start="Oradea"
goal="Eforie"
#Here Fagaras is the goal.
fagaras=sa.Algorithms()
final_solution1=fagaras.average_calc(fagaras.dfs,graph,start,goal,100000)
print(final_solution1)
final_solution2=fagaras.average_calc(fagaras.ucs,graph,start,goal,100000)
print(final_solution2)
final_solution3=fagaras.average_calc(fagaras.a_star,graph,start,goal,100000)
print(final_solution3)

start="Oradea"
goal="Bucharest"
#Here pitesti is the goal.
pitesti=sa.Algorithms()
final_solution1=pitesti.average_calc(pitesti.dfs,graph,start,goal,100000)
print(final_solution1)
final_solution2=pitesti.average_calc(pitesti.ucs,graph,start,goal,100000)
print(final_solution2)
final_solution3=pitesti.average_calc(pitesti.a_star,graph,start,goal,100000)
print(final_solution3)

start="Oradea"
goal="Arad"
#Here pitesti is the goal.
rimnicu_vilcea=sa.Algorithms()
final_solution1=rimnicu_vilcea.average_calc(rimnicu_vilcea.dfs,graph,start,goal,100000)
print(final_solution1)
final_solution2=rimnicu_vilcea.average_calc(rimnicu_vilcea.ucs,graph,start,goal,100000)
print(final_solution2)
final_solution3=rimnicu_vilcea.average_calc(rimnicu_vilcea.a_star,graph,start,goal,100000)
print(final_solution3)

start="Oradea"
goal="Urziceni"
#Here pitesti is the goal.
timisoara=sa.Algorithms()
final_solution1=timisoara.average_calc(timisoara.dfs,graph,start,goal,100000)
print(final_solution1)
final_solution2=timisoara.average_calc(timisoara.ucs,graph,start,goal,100000)
print(final_solution2)
final_solution3=timisoara.average_calc(timisoara.a_star,graph,start,goal,100000)
print(final_solution3)

start="Oradea"
goal="Vaslui"
#Here pitesti is the goal.
iasi=sa.Algorithms()
final_solution1=iasi.average_calc(iasi.dfs,graph,start,goal,100000)
print(final_solution1)
final_solution2=iasi.average_calc(iasi.ucs,graph,start,goal,100000)
print(final_solution2)
final_solution3=iasi.average_calc(iasi.a_star,graph,start,goal,100000)
print(final_solution3)