import re;

filename="input/input03.txt"
with open(filename, "rt") as input_file:
	input_str=input_file.read();

claims = input_str.split('\n');
cls=[];

for claim in claims:
			#print(claim);
			data = re.search('\#([0-9]+).\@.([0-9]+),([0-9]+):.([0-9]+)x([0-9]+)', claim);

			no=int(data.group(1));
			lm=int(data.group(2));
			um=int(data.group(3));
			wd=int(data.group(4));
			ht=int(data.group(5));
			cls.append([no,lm,um,wd,ht]);


patches=[];

for i in range(1,1000):
	patches.append([0]*1000);

for claim in cls:
	for i in range(claim[3]): #wd
		for j in range(claim[4]): #ht
			patches[claim[1]+i][claim[2]+j]+=1;

reused=0;
for l in patches:
	for c in l:
		if c>=2:
			reused +=1;
print("part 1:",reused);


for claim in cls:
	tainted=False;
	for i in range(claim[3]): #wd
		for j in range(claim[4]): #ht
			if patches[claim[1]+i][claim[2]+j] !=1:
				tainted=True;
	if tainted==False:
		print("part 2:", claim[0]);