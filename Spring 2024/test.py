grade = open('Grades.txt', 'r')
lines = grade.readlines()
print(lines)

for k in range(len(lines)):
	lines[k] = (lines[k].split())
print(lines)

for i in range(1,len(lines),1):
	for j in range(len(lines[i])):
		lines[i][j] = float(lines[i][j])

print(lines)
g = 0
grades = []

for i in range(1,len(lines),1):

	g = 0.05*lines[i][1]+0.15*lines[i][2]+0.15*lines[i][3]+0.2*lines[i][4]+0.45*lines[i][5]
	g = round(g,2)
	grades.append(g)

final=[]

for i in range(len(grades)):
	if float(grades[i]) >= 90:
		final.append('A')
	elif float(grades[i]) >= 80:
		final.append('B')
	elif float(grades[i]) >= 70:
		final.append('C')
	elif float(grades[i]) >= 60:
		final.append('D')
	else:
		final.append('F')
d = []
f = open('Final.txt', 'w')
d.append('Index    ' + 'Total   ' + 'Letter  ')
for i in range(1, len(lines),1):

	d.append('{0}    {1}     {2}  '.format(lines[i][0], grades[i-1], final[i-1]))
	print(d[i])
	f.write(d[i] + '\n')
f.close()
