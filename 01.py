import math;
import sys;

filename="input/input01.txt"
with open(filename, "rt") as input_file:
	input_str=input_file.read();

lines=input_str.split('\n');

freq=0;
for l in lines:
		if l[0]=="+":
			freq+=int(l[1:]);
		else:
			freq-=int(l[1:]);
print("part 1:", freq);

freq=0;
frs=set();
frs.add(0);
while True:
	for l in lines:
		if l[0]=="+":
			freq+=int(l[1:]);
		else:
			freq-=int(l[1:]);
		if freq in frs:
			print("part 2:", freq);
			sys.exit();
		frs.add(freq);