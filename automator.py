# Builds avida and runs for different values of m_share. Can be adapted to required task


from shutil import copy
import os
for i in range(1,11):
	#This part change cOrganism.h to modify m_share (from 0.1 to 1.0)
	M_SHARE = float(0.1*i)
	filename = 'avida-core/source/main/cOrganism.h'

	file_lines = open(filename).read().splitlines()

	file_lines[77]= "  double m_share = " + str(M_SHARE) +";" 

	open('cOrganism.h','w').write('\n'.join(file_lines))
	copy('cOrganism.h','avida-core/source/main')
	
	#This part builds avida after the modification
	os.system('./build_avida')

	#This part copies the environment.cfg, events.cfg and avida.cfg files for experiment
        copy('backup/environment.cfg','cbuild/work/')
	copy('backup/events.cfg','cbuild/work/')
	copy('backup/avida.cfg','cbuild/work/')

	#This part executes avida
	os.chdir('cbuild/work')
	os.system('./avida')
	os.chdir('/home/bhaskar/avidainsts/avida_1-1')
	
	#This part copies the data to ExpData folder after experiment is over as data<i>
	os.system('cp -r cbuild/work/data /home/bhaskar/avidainsts/ExpData/v1-1/data'+str(i))
	
