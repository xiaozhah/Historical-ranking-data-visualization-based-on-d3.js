import re
import datetime

lis = []
pattern = re.compile(r'.*-(.*)\+.*')
start_time = datetime.date(2019,1,1)

csv_fp = open('phonemes.csv','wt')
csv_fp.write('name,type,value,date\n')

with open('debug_way3.log') as fp:
	fp.readline()
	for i in range(90):
		if i % 20 != 0:
			fp.readline()
			for i in range(10):
				fp.readline()
			fp.readline()
		else:
			fp.readline()
			for i in range(10):
				date_now = start_time + datetime.timedelta(days=1)
				line = fp.readline().split()
				assert(len(line)==3)
				line[0] = line[0].rstrip()
				phoneme = re.sub(pattern,'\\1',line[0])
				csv_fp.write('%s,%s,%s,%s\n' % (line[0], phoneme, int(line[2]), date_now.strftime("%Y-%m-%d")))
			start_time = date_now
			fp.readline()

csv_fp.close()