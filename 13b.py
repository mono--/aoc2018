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

test3="""/>-<\\  
|   |  
| /<+-\\
| | | v
\\>+</ |
  |   ^
  \\<->/"""

lines=input_str.split('\n')

y_dim = len(lines)
x_dim= len(lines[0])

grid=[];

for y in range(y_dim):
	grid_line=[];
	for x in range(x_dim):
		grid_line.append(lines[y][x]);
	grid.append(grid_line)

def populate(grid):
	cars=[]
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
	return cars;


def dirs(i):
	if i==0:
		return([-1,0])
	if i==1:
	 	return([0,1])
	if i==2:
	 	return([1,0])
	if i==3:
	 	return([0,-1])

def move_car(x,y,a,b,c): #x,y -> position, a -> direction, b-> turn_preference, c-> moved already in this tick
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
		

import operator
import copy

cars=populate(grid);
all_cars=cars;

while(True):
	unmoved_cars = sorted([c for c in all_cars if c[4]==0], key=operator.itemgetter(0, 1))
	
	#reset move status if all cars moved
	if len(unmoved_cars)==0:
		for c in all_cars:
			c[4]=0;

	#do the moves in order
	for car in unmoved_cars:
		all_cars.remove(car);
		
		#set of positions except moving car
		pos=set([])
		for c in all_cars:
			pos.add((c[0],c[1]))


		car_new=move_car(car[0],car[1],car[2],car[3],car[4]);
		
		all_cars.append(car_new)
		
		#check for accidents
		if (car_new[0],car_new[1]) in pos:
			print('accident at ',car_new[0],car_new[1])	
			
			#accident can only happen with recently moved car
			all_cars.remove(car_new)
			print('removing', car_new)
			#find the unique other car, that crashed
			for c in all_cars:
				if [c[0],c[1]] == [car_new[0],car_new[1]]:
					print('removing', c)
					all_cars.remove(c);
					break;

			break;

	if len(all_cars) ==1:
		#run the tick to the end
		if all_cars[0][4] == 1:
			#beware of the switch [y][x] -> x,y  :)
			print("last car at:", all_cars[0][1],all_cars[0][0])
		else:
			final_car=move_car(all_cars[0][0],all_cars[0][1],all_cars[0][2],all_cars[0][3],all_cars[0][4])
			print("last car at:", final_car[1],final_car[0]);
		exit()