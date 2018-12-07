import re;

from operator import itemgetter;

filename="input/input04.txt"
with open(filename, "rt") as input_file:
	input_str=input_file.read();

input_str_test="""[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up""";


logs = input_str.split('\n');

log_data=[];
mask='\[1518-([0-9]+)-([0-9]+).([0-9]+):([0-9]+)\].(wakes up|falls asleep|Guard \#([0-9]+))';
for line in logs:
			data = re.search(mask, line);
			month = int(data.group(1));
			day = int(data.group(2));
			hour = int(data.group(3));
			minute = int(data.group(4));
			act = data.group(5);
			number_str = data.group(6);
			log_data.append([month,day,hour,minute,act,number_str]);

log_data.sort();

timelog = dict();
gn=0;
asleep_time=0;
wake_time=0;
for l in log_data:
	if "Guard" in l[4]:
		gn=int(l[5]);
		if not gn in timelog:
			timelog[gn]=[0]*60;
	if "wakes" in l[4]:
		wake_time=l[3];
		for i in range(wake_time-asleep_time):
			timelog[gn][asleep_time+i] = timelog[gn][asleep_time+i]+1;
	if "asleep" in l[4]:
		asleep_time=l[3];

#calcualate sleepiest guard
m=0;
gn_m=0;
for gn in timelog:
	if(sum(timelog[gn]))>m:
		m=sum(timelog[gn])
		gn_m=gn;

#calc his sleepiest minute
m=0;
i_m=0;
for i in range(60):
	if timelog[gn_m][i] > m:
		i_m=i;
		m=timelog[gn_m][i];


print("part 1:", i_m*gn_m);

m=0;
gn_m=0;
i_m=0;
for gn in timelog:
	for i in range(60):
		if timelog[gn][i]>m:
			m=timelog[gn][i];
			gn_m=gn;
			i_m=i;

print("part 2:", i_m*gn_m);