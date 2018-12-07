filename="input/input06.txt"
with open(filename, "rt") as input_file:
	input_str=input_file.read();

from operator import itemgetter;


test_str="""1, 1
1, 6
8, 3
3, 4
5, 5
8, 9"""

lines = input_str.split('\n');
pts=[];

def manh_dist(p,q):
	return(abs(p[0]-q[0])+abs(p[1]-q[1]));

def manh_dist_all(p,l):
	md=0;
	for q in l:
		md += manh_dist(p,q);
	return(md);

def nearest(p,pts):
	s=sorted(pts, key=(lambda x: manh_dist(p,x)))[0]; 
	t=sorted(pts, key=(lambda x: manh_dist(p,x)))[1]; 
	if manh_dist(p,s)==manh_dist(p,t):
		return [];
	else:
		return s;

for line in lines:
	[x,y]=line.split(',');
	pts.append([int(x),int(y)]);

x_min=x_max=pts[0][0];
y_min=y_max=pts[0][1];

#calculate bounding rectangle
for p in pts:
	x_min=min(x_min,p[0]);
	x_max=max(x_max,p[0]);
	y_min=min(y_min,p[1]);
	y_max=max(y_max,p[1]);

def ubb(p):
	if x_min< p[0] < x_max and y_min<p[1]<y_max:
		return False;
	else:
		return True;

areas=dict();
areas1=dict();
for p in pts:
	areas[str(p)]=0;
	areas1[str(p)]=0;

#these are not optimale ranges, but sufficient,
#i.e. outside all points belong to unbounded areas

#idea is: bump the ranges by diff(=1) and check which ones stay the same

diff=1;

for i in range(x_min-y_min,x_max+y_max):
	for j in range(y_min-x_min,y_max+x_max):
		s = nearest([i,j],pts);
		if s == []:
			continue;
		if ubb(s):
			continue;
		else:
			areas[str(s)]+= 1;
			areas1[str(s)]+=1;

#borders1
for i in range(x_min-y_min-diff,x_max+y_max+diff):
	for j in [y_min-x_min-diff,y_max+x_max+diff]:
		s = nearest([i,j],pts);
		if s == []:
			continue;
		if ubb(s):
			continue;
		else:
			areas1[str(s)]+=1;
#borders2
for i in [x_min-y_min-diff,x_max+y_max+diff]:
	for j in range(y_min-x_min-diff,y_max+x_max+diff):
		s = nearest([i,j],pts);
		if s == []:
			continue;
		if ubb(s):
			continue;
		else:
			areas1[str(s)]+=1;

print("part 1:", max(areas[key] for key in areas if areas[key]==areas1[key]));

areas=dict();

#ranges are easy this time (but not optimal)
b=int(10000/len(pts));
for i in range(x_min-b,x_max+b):
	for j in range(y_min-b,y_max+b):
		areas[str([i,j])]=manh_dist_all([i,j] , pts);

ct=0;

for p in areas:
	if areas[p] < 10000:
		#print(p);
		ct+=1;
print("part 2:", ct);