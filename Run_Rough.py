from os import system, listdir
## New dt's and range made 7-4-2019. Folder updated
Re_list = [1120, 1140, 1160, 1180]
run = 3
start = 0
i = 0
Re = Re_list[start]
print('starting RE=%1d_%1d'%(Re_list[start], i) ) 

system('mpirun -np 26 python3 NSfracStep.py '+ \
		'problem=2DPipe_Rough_RW '+\
		'Re=%1d '%Re+\
		'restart_folder=../2DPipe_Rough_RW_results/data/%1d/Checkpoint '%run +\
		'> Rough_Run%1d_Re%1d_Rs%1d'%(run,Re, i) )

while 'memory_error' in listdir():
	if 'kill_loop' in listdir('.'):
		print('Kill Loop found!!')
		break
	i += 1
	print( 'starting RE=%1d_%1d'%(Re,i))
	system('rm memory_error')
	system('mpirun -np 26 python3 NSfracStep.py '+ \
		'problem=2DPipe_Rough_RW '+ \
		'Re=%1d '%(Re) +\
		#'dt=%1.7f '%dt +\
		'restart_folder=../2DPipe_Rough_RW_results/data/%1d/Checkpoint '%run +\
		'> Rough_Run%1d_Re%1d_Rs%1d'%(run,Re, i) )

for j in range(start+1, len(Re_list)):
	
	i = 0
	Re = Re_list[j]
	if 'kill_loop' in listdir('.'):
		print('Kill Loop found!!')
		system('rm kill_loop')
		break
	
	print( 'starting RE=%1d'%Re)
	system('mpirun -np 26 python3 NSfracStep.py '+ \
		'problem=2DPipe_Rough_RW '+ \
		'Re=%1d '%Re +\
		#'dt=%1.7f '%dt +\
		'restart_folder=../2DPipe_Rough_RW_results/data/%1d/Checkpoint '%run+\
		'> Rough_Run%1d_Re%1d_Rs%1d'%(run,Re, i) )

	while 'memory_error' in listdir():
		if 'kill_loop' in listdir('.'):
			print('Kill Loop found!!')
			break
		i += 1
		print( 'starting RE=%1d_%1d'%(Re,i))
		system('rm memory_error')
		system('mpirun -np 26 python3 NSfracStep.py '+ \
			'problem=2DPipe_Rough_RW '+ \
			'Re=%1d '%(Re) +\
			#'dt=%1.7f '%dt +\
			'restart_folder=../2DPipe_Rough_RW_results/data/%1d/Checkpoint '%run +\
			'> Rough_Run%1d_Re%1d_Rs%1d'%(run,Re, i) )