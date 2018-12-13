filename="input/input13.txt"
with open(filename, "rt") as input_file:
	input_str=input_file.read();

test="""/->-\\        
|   |  /----\\
| /-+--+-\\  |
| | |  | v  |
\\-+-/  \\-+--/
  \\------/   """

test2="""|  |  |  |  
v  |  |  |  
|  v  v  |  
|  |  |  v  
|  |  ^  ^  
^  ^  |  |  
|  |  |  |  """
lines=input_str.split('\n')

grid=[];
pos=set([])
cars=[];
y_dim = len(lines)
x_dim= len(lines[0])

for y in range(y_dim):
	grid_line=[];
	for x in range(x_dim):
		grid_line.append(lines[y][x]);
	grid.append(grid_line)


for l_idx in range(y_dim):
	for c_idx in range(x_dim):
		s=grid[l_idx][c_idx];
		#dirs: 0=up,1=right, 2=down, 3=left
		if s=='v': 
			cars.append([l_idx,c_idx,2,0,0]);
			grid[l_idx][c_idx]='|'
			continue;
		if s=='<': 
			cars.append([l_idx,c_idx,3,0,0]);
			grid[l_idx][c_idx]='-'
			continue;
		if s=='^': 
			cars.append([l_idx,c_idx,0,0,0]);
			grid[l_idx][c_idx]='|'
			continue;
		if s=='>': 
			cars.append([l_idx,c_idx,1,0,0]);
			grid[l_idx][c_idx]='-'
			continue;

def print_state(grid):
	for line in grid:
		l=''.join(line);
	return(None);

def dirs(i):
	if i==0:
		return([-1,0])
	if i==1:
	 	return([0,1])
	if i==2:
	 	return([1,0])
	if i==3:
	 	return([0,-1])

def move_car(x,y,a,b,c):
	car=[x,y,a,b,c]
	car_new=[0]*5
	global pos
	global grid
	next_tile_pos=[car[0],car[1]];
	next_tile_pos[0] += dirs(car[2])[0];
	next_tile_pos[1] += dirs(car[2])[1];
	next_tile=grid[next_tile_pos[0]][next_tile_pos[1]];
	if next_tile=='-' or next_tile=='|':
		car_new[:]=car[:];
		car_new[0] = next_tile_pos[0];
		car_new[1] = next_tile_pos[1];
	elif next_tile=="/":
		car_new[:]=car[:];
		car_new[0]=next_tile_pos[0];
		car_new[1]=next_tile_pos[1];
		if car[2]==0 or car[2]==2:
			car_new[2] = car[2]+1;
		elif car[2]==1 or car[2]==3:
			car_new[2] = car[2]-1;
	elif next_tile=='\\':
		car_new[:]=car[:];
		car_new[0]=next_tile_pos[0];
		car_new[1]=next_tile_pos[1];
		
		if car[2]==0 or car[2]==2:
			car_new[2] = (car[2]+3) % 4;
		elif car[2]==1 or car[2]==3:
			car_new[2] = (car[2] + 1) % 4;
		
	elif next_tile=="+":
		car_new[:]=car[:];
		car_new[0]=next_tile_pos[0];
		car_new[1]=next_tile_pos[1];
		if car[3] == 0:
			car_new[2] = (car[2]+3) % 4;
			car_new[3] = 1;
		if car[3] == 1:
			car_new[2] = car[2];
			car_new[3] = 2;
		if car[3] == 2:
			car_new[2] = (car[2] + 1)%4;
			car_new[3] = 0;
	else:
		print("strange tile:", next_tile);
		exit()
	car_new[4]=1;
	return(car_new)
		


for car in cars:
	pos.add((car[0],car[1]))

import operator

for ct in range(200):
	cars = sorted(cars, key=operator.itemgetter(0, 1));
	for car in cars:
		pos.remove((car[0],car[1]));
		car_new=move_car(car[0],car[1],car[2],car[3],car[4]);
		if (car_new[0],car_new[1]) in pos:
			print("1st accident at:", car_new[1],car_new[0]);
			exit()
		else: 
			pos.add((car_new[0],car_new[1]))
			car[:]=car_new[:];