
players=9;
last=25;

scores=[0]*players;

#list copy implementation -> runtime for part 1 ~ 1 min

#list of marbles
game=[0];

#index of current marble
cur=0;

cur_player=0;

for i in range(1,last+1):
	if (i %23)==0:
		scores[cur_player] += i+game[(cur-7)];
		
		#this is the slow step
		game=game[:(cur-7)%len(game)]+game[(cur-6)%len(game):];
		cur=(cur-7)%len(game);
	elif len(game)>1:
		game=game[:(cur+2)%len(game)]+[i]+game[(cur+2)%len(game):];
		cur=(cur+2)%(len(game)-1);
	
	#step 0
	else:
		game=game+[i];
		cur=cur+1;
	
	cur_player=(cur_player+1) % players;

print("part 1:", max(scores));

###########################
#poor man's ring buffer :)#
###########################
from copy import copy
class node:
	def __init__(self):
		self.data = None;
		self.next = None;
		self.prev = None;

class ring_buf:
	def __init__(self):
		self.cur_node = None;
		self.leng = 0;

	def add_node(self, data):
		if self.leng == 0:
			first_node = node();
			first_node.prev=first_node;
			first_node.next=first_node;
			first_node.data=data;
			self.cur_node = first_node;
			self.leng = 1;

		else:
			#construct node
			new_node = node();
			next_node = self.cur_node.next;
			new_node.data=data;
			self.leng+=1;
			#set new links
			new_node.prev=self.cur_node;
			new_node.next=next_node;
			next_node.prev=new_node;
			self.cur_node.next=new_node;
			#advance view
			self.cur_node=new_node;
	#we don't need this		
	def print_node(self):
		print(str(self.cur_node.data));

	def rot(self,i):
		if i >= 0:
			for _ in range(i):
				self.cur_node=self.cur_node.next;
		if i < 0:
			for _ in range(-i):
				self.cur_node=self.cur_node.prev;

	def pop(self):
		if self.leng != 0:
			self.cur_node.prev.next=self.cur_node.next;
			self.cur_node.next.prev=self.cur_node.prev;

			ret = copy(self.cur_node.data);
			self.cur_node = self.cur_node.next;
			self.leng -= 1;
			return(ret);
		else:
			return(None);

players=425
last=70848

last=last*100;

scores=[0]*players;
cur_player=0;

game=ring_buf();
game.add_node(0);

for i in range(1,last+1):
	if (i % 23)==0:
		game.rot(-7);
		scores[cur_player] += i + int(game.pop());
	else:
		game.rot(1);
		game.add_node(i);
	
	cur_player= (cur_player+1) % players;

print("part 2:", max(scores));



