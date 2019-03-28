import matplotlib.pyplot as plt
import re
import sys
#Plots all tasks in a tasks.dat file. Takes information from file itself.
#If arguments given after filename, plots only those tasks. Otherwise plots
#all tasks
#This is some real good script :3:3:3
def StrIsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

file = sys.argv[1]

#Extract lines containing information about task type. Line 5 onwards (index 4)
taskdict={} #Dictionary to store column numbers and task types
with open(file) as tasksfile:
		for line in tasksfile:
			if line[0]=="#":
				splitline = re.split('  | |: |\n',line)
				if(StrIsInt(splitline[1])): #If the second element of split line is a integer
					#Store integer and task name in taskdict
					taskdict[int(splitline[1])] = splitline[2]

taskstoprint=[]
if len(sys.argv)>2: #If some tasks to print given specifically
	for i in range(2,len(sys.argv)): #sys.argv[1] is filename, 2 onwards are tasks to print
		taskstoprint.append(str(sys.argv[i]))
#print taskdict
#taskdict now contains {"taskname":col_no,...}
#We'll replace col_no with array of number of organisms over time

numcol = len(taskdict)

#print numcol. numcol is total number of columns.
matrix=[] #A 2d matrix containing no. of organisms for each task. matrix[0] = [0,100,200...] and so on

for i in range(0,numcol):
	matrix.append([])

with open(file) as tasksfile:
	for line in tasksfile: #iterates through lines
		if line[0]!="#" and line[0]!="\n": #Gets rid of non data lines
			words = line.split()
			for i in range(0,numcol):
				matrix[i].append(int(words[i]));
#print matrix


#Each row of the 2D matrix is now a set of values of tasks over time.
#First row is updates
if len(sys.argv)<=2:
	for i in range(1,numcol):
		plt.plot(matrix[0],matrix[i],label=taskdict[i+1]) #Get label from dict 

if len(sys.argv)>2:
	for i in range(1,numcol):
		if taskdict[i+1] in taskstoprint:
			plt.plot(matrix[0],matrix[i],label=taskdict[i+1])

plt.xlabel('Time Step (Updates)')
plt.ylabel('Number of organisms performing task')

plt.legend()
plt.show()
