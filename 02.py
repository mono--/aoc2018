filename="input/input02.txt"
with open(filename, "rt") as input_file:
	input_str=input_file.read();

lines = input_str.split('\n');

twos=0;
threes=0;
for l in lines:
	tw=False;
	th=False;
	for c in l:
		if l.count(c)==2 and tw==False:
			twos+=1;
			tw=True;
		if l.count(c)==3 and th==False:
			threes+=1;
			th=True;

print("part 1:", twos*threes);

for l in lines:
	for k in lines:
		mm=False;
		for i in range(len(l)):
			if l[i] != k[i]:#
				if mm == False:
					mm = True;
				else:
					break;
			if i == len(k)-1 and mm == True:
				l1=k;
				l2=l;
ans='';
for i in range(len(l1)):
	if l1[i]==l2[i]:
		ans=ans+l1[i];

print("Part 2:", ans);