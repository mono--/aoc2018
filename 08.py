filename="input/input08.txt"
with open(filename, "rt") as input_file:
	input_str=input_file.read();

test_str="2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"
inp=[int(a) for a in input_str.split()];

def read(i):
	#the sum
	s=0;
	#no of children is first info in a node
	children=inp[i];
	i+=1;
	#no if metadata 
	meta=inp[i];
	i+=1;

	if children==0:
		#return sum of metadata for this node and the beginning of next info
		return [sum(inp[j+i] for j in range(meta)),i+meta]; 
	
	for k in range(children):
		[x,y]=read(i);
		s+=x;
		#start reading at next info
		i=y;
	
	#if this node has children, don't forget to also read its own metadata
	return [s+sum(inp[j+i] for j in range(meta)),i+meta];

print("part 1:", read(0)[0]);

def value(i):
	#beginning is the same as for part 1
	s=0;
	children=inp[i];
	i+=1;
	meta=inp[i];
	i+=1;
	if children==0:
		return [sum(inp[j+i] for j in range(meta)),i+meta];

	#if node has children:
	#construct list of child nodes with entries [value of child, beginning of next info]
	ch_nodes=[];
	for k in range(children):
		[x,y]=value(i);
		ch_nodes.append([x,y]);
		i=y;

	#update value with values of all children referenced in this node's metadata
	for j in range(meta):
		if inp[j+i] <= children: #we only count the elegible metadata
			s+=ch_nodes[inp[i+j]-1][0];

	return [s,i+meta];

print("part 2:",value(0)[0]);