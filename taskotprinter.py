import sys
import matplotlib.pyplot as plt

#Plots the number of certain tasks done overtime from tasks.dat file.
#Change the kind of tasks to plot here
#Give tasks.dat files as command line parameters


#filename=sys.argv[1]
#savedes=sys.argv[2]
for i in range(1,len(sys.argv)):
	file = sys.argv[i]
	COLUMN_TIME=1
	#COLUMN_NOT=1
	#COLUMN_NAND=1
	#COLUMN_AND=1
	#COLUMN_ORNOT=1
	#COLUMN_OR=1
	#COLUMN_ANDNOT=1
	#COLUMN_NOR=1
	#COLUMN_XOR=1
	#COLUMN_EQ=1
	COLUMN_AND=11
	m_share=i*0.1
 	TimeList=[]
	#NotList=[]
	#NandList=[]
	AndList=[]
	#OrnotList=[]
	#OrList=[]
	#AndnotList=[]
	#NorList=[]
	#XorList=[]
	#EqList=[]
	#Times2List=[]

	with open(file) as fileTasks:
    		for line in fileTasks:
        		if line[0]!="#" and line[0]!="\n":
            			words=line.split()
            			TimeList.append(int(words[COLUMN_TIME-1]))
            			#NotList.append(int(words[COLUMN_NOT-1]))
            			#NandList.append(int(words[COLUMN_NAND-1]))
            			#AndList.append(int(words[COLUMN_AND-1]))
            			#OrnotList.append(int(words[COLUMN_ORNOT-1]))
            			#OrList.append(int(words[COLUMN_OR-1]))
            			#AndnotList.append(int(words[COLUMN_ANDNOT-1]))
            			#NorList.append(int(words[COLUMN_NOR-1]))
            			#XorList.append(int(words[COLUMN_XOR-1]))
            			#EqList.append(int(words[COLUMN_EQ-1]))
            			AndList.append(int(words[COLUMN_AND-1]))

			
		plt.plot(TimeList,AndList,label=file)
#plt.plot(TimeList,NandList,label="NAND")
#plt.plot(TimeList,AndList,label="AND")
#plt.plot(TimeList,OrnotList,label="ORNOT")
#plt.plot(TimeList,OrList,label="OR")
#plt.plot(TimeList,AndnotList,label="ANDNOT")
#plt.plot(TimeList,NorList,label="NOR")
#plt.plot(TimeList,XorList,label="XOR")
#plt.plot(TimeList,EqList,label="EQ")
plt.xlabel('Time step')
plt.ylabel('Number of organisms performing task')

plt.legend()
plt.show()
#plt.savefig(savedes, bbox_inches='tight')
















