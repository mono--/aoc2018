filename="input/input05.txt"
with open(filename, "rt") as input_file:
	input_str=input_file.read().strip();

from operator import itemgetter;

test_str="""dabAcCaCBAcCcaDA""";

#a string copy for each replacement
# runtime ~20sec
def redu1(s): 
	red=True;
	while(red):
		st=s;
		red=False;
		for i in range(len(st)-1):
			if st[i].lower()==st[i+1].lower() and st[i] != st[i+1]:
				red=True;
				s=st[:i]+st[i+2:];
				break;
	return(len(s));

#better: does one run of removals while going through the whole string
#but ad-hoc end of string handling and still one string-copy per run
#runtime ~2 sec
def redu2(s):
	red=True;
	while(red):
		st='';
		red=False;
		red1=False;
		for i in range(len(s)-1):
			if red1==True:
				red1=False;
				continue;
			elif s[i].lower()==s[i+1].lower() and s[i] != s[i+1]:
				red=True;
				red1=True;
				continue;
			st=st+s[i];
		s=st+s[-1];
	return (len(s));

# "best": only one run over entire string
#runtime <0.1 sec
def redu3(s):	
	buf=['_'];
	for c in s:
		if buf[-1].lower()== c.lower() and buf[-1]!= c:
			buf.pop();
		else:
			buf.append(c);
	return(len(buf)-1);

print("part 1:",redu3(input_str)); 


