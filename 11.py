import sys

ser_no=8561;
cells=[];

def power(a,b,s):
	return(int(str(int((((a+10)*b+s)*(a+10))/100))[-1])-5);

grid_size=300; 

for y in range(0,grid_size+1):
	line=[];
	for x in range(0,grid_size+1):
		line.append(power(x,y,ser_no));
	#print(line);
	cells.append(line);

#recursion is a speedup, but not really necessary: the max is at d=12 as can be seen from the output.
def square(x,y,d):
	global cells;
	t=0;
	if d<10:
		for m in range(d):
			for n in range(d):
				t += cells[y+m][x+n];
		return t;
	elif d%2==0:
		return(square(x,y,int(d/2))+square(x+int(d/2),y,int(d/2))+square(x,y+int(d/2),int(d/2))+square(x+int(d/2),y+int(d/2),int(d/2)));
	else:
		return(square(x,y,(d-1))+sum([cells[y+d-1][x+j] for j in range(d)])+ sum([cells[y+j][x+d-1] for j in range(d-1)]));


x_max,y_max,d=1,1,1
print()
print("part 1 solution is the value at d=3");
print()
print("part 2 solution is the maximal value (this is to be expected for d<20")
print()
for d in range(1,25):
	max_power=square(1,1,d);
	for i in range(1,grid_size-(d-2)):
		for j in range(1,grid_size-(d-2)):
			if square(j,i,d) > max_power:
				max_power = square(j,i,d);
				x_max=j;
				y_max=i;
				d_max=d;
	print(x_max,y_max, d, max_power); 
	sys.stdout.flush();