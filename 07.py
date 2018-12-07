from operator import itemgetter;
import re
import math
import string

filename="input/input07.txt"
with open(filename, "rt") as input_file:
	input_str=input_file.read();


test_str="""Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin."""

lines = input_str.split('\n');
conds=[];
for line in lines:
	regex=re.search('Step (.+) must be .* (.+) can begin.',line);
	x,y = regex.group(1).lower(), regex.group(2).lower();
	conds.append([x,y]);

alph=string.ascii_lowercase;

#the dict holds to each node its predecessors
graph=dict();
for c in alph:
	for cond in conds:
		if cond[1]==c and c in graph:
			graph[c].append(cond[0]);
			continue;
		if cond[1]==c:
			graph[c]=[cond[0]];
			if cond[0] not in graph:
				graph[cond[0]]=[];


#prune the graph from the node that is (i) without predecessors (ii) alphabetically earliest
solution=[];
while(len(graph)>0):
	for c in alph:
		if c in graph and graph[c]==[]:
			solution.append(c);
			del graph[c];
			for key in graph:
				if c in graph[key]:
					graph[key].remove(c);
			break;

print("part 1:", ''.join(solution));



workers=5;
worker_busy=[False]*workers;
worker_delay=[0]*workers;
working_on=['']*workers;
delay=60;
t=0;

#construct graph for part 2 again; code reuse :/
for c in alph:
	for cond in conds:
		if cond[1]==c and c in graph:
			graph[c].append(cond[0]);
			continue;
		if cond[1]==c:
			graph[c]=[cond[0]];
			if cond[0] not in graph:
				graph[cond[0]]=[];


while(len(graph)>0):
	for c in alph:
		#find c that can be pruned according to the algo in part 1...
		if c in graph and graph[c]==[]: 
			#... such that there is a free worker to prune it and noone is already working on it
			if False in worker_busy and c not in working_on: 
				# assign worker i the job to prune it
				i=worker_busy.index(False);
				worker_busy[i]=True;
				worker_delay[i]=delay+alph.index(c);
				working_on[i]=c;

	# prune all jobs, whose delay is run out
	for x in range(workers):
		if worker_busy[x]==True and worker_delay[x]==0:
			d=working_on[x];
			worker_busy[x]=False;
			#the pruning itself is done as in part 1
			del graph[d];
			for key in graph:
				if d in graph[key]:
					graph[key].remove(d);
			break;
	#time flies
	t+=1;

	#reduce each workers' delay up to a minimum of 0.
	for x in range(workers):
		worker_delay[x]=max(0,worker_delay[x]-1);

print("part 2:", t);







