import re

filename="input/input10.txt"
with open(filename, "rt") as input_file:
	input_str=input_file.read();

test_str="""position=< 9,  1> velocity=< 0,  2>
position=< 7,  0> velocity=<-1,  0>
position=< 3, -2> velocity=<-1,  1>
position=< 6, 10> velocity=<-2, -1>
position=< 2, -4> velocity=< 2,  2>
position=<-6, 10> velocity=< 2, -2>
position=< 1,  8> velocity=< 1, -1>
position=< 1,  7> velocity=< 1,  0>
position=<-3, 11> velocity=< 1, -2>
position=< 7,  6> velocity=<-1, -1>
position=<-2,  3> velocity=< 1,  0>
position=<-4,  3> velocity=< 2,  0>
position=<10, -3> velocity=<-1,  1>
position=< 5, 11> velocity=< 1, -2>
position=< 4,  7> velocity=< 0, -1>
position=< 8, -2> velocity=< 0,  1>
position=<15,  0> velocity=<-2,  0>
position=< 1,  6> velocity=< 1,  0>
position=< 8,  9> velocity=< 0, -1>
position=< 3,  3> velocity=<-1,  1>
position=< 0,  5> velocity=< 0, -1>
position=<-2,  2> velocity=< 2,  0>
position=< 5, -2> velocity=< 1,  2>
position=< 1,  4> velocity=< 2,  1>
position=<-2,  7> velocity=< 2, -2>
position=< 3,  6> velocity=<-1, -1>
position=< 5,  0> velocity=< 1,  0>
position=<-6,  0> velocity=< 2,  0>
position=< 5,  9> velocity=< 1, -2>
position=<14,  7> velocity=<-2,  0>
position=<-3,  6> velocity=< 2, -1>"""

lines=input_str.split('\n');

points=[];
vels=[];

for line in lines:
	regex=re.search('position=<(.*),(.*)> velocity=<(.*),(.*)>',line);
	points.append([int(regex.group(1)),int(regex.group(2))]);
	vels.append([int(regex.group(3)),int(regex.group(4))]);	
shrinking=True;

#large dummy boundaries for 1st step 
xmax_old=10000000;
ymax_old=10000000;

#time passed
t=0;

while True:
	xmax=0;
	ymax=0;
	
	t+=1;

	#update positons and boundaries
	for i in range(len(points)):
		for j in range(2):
			points[i][j] += vels[i][j];
		xmax=max(abs(points[i][0]),xmax);
		ymax=max(abs(points[i][1]),xmax);
	
	#check if starfield is still shrinking
	if xmax_old < xmax and ymax_old < ymax: 
		#previous step was smallest -> go one back in time and print
		for i in range(len(points)):
			for j in range(2):
				points[i][j] -= vels[i][j];
		break;
	
	xmax_old=xmax;
	ymax_old=ymax;
	
	print("time passed:", t, "boundaries:", xmax,"/",ymax);
	
#construct bitmap and print line by line
for i in range(-xmax,xmax+1):
		line=[];
		for j in range(-ymax,ymax+1):
			pt_on = False;
			for point in points:
				if i==point[1] and j == point[0]:
					pt_on=True;
			if pt_on==True:
				line.append('#');
			else:
				line.append(' ');
		out=''.join(line);
		print(out);