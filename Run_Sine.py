from os import system, listdir

Re_list = [10, 20, 40, 60, 80, 120, 140, 160, 180]
#Re_list = [50, 150, 250, 350, 450]

run = 7
start = 0
i = 0
Re = Re_list[start]
print('starting RE=%1d_%1d'%(Re_list[start], i) ) 

system('mpirun -np 26 python3 NSfracStep.py '+ \
		'problem=2DPipe_Rough_sin '+\
		'Re=%1d '%Re+ \
		#'restart_folder=../2DPipe_Rough_sin_results/data/%1d/Checkpoint '%run +\
		'> Rough_Run%1d_Re%1d_Rs%1d'%(run,Re, i) )

while 'memory_error' in listdir():
	if 'kill_loop' in listdir('.'):
		print('Kill Loop found!!')
		break
	i += 1
	print( 'starting RE=%1d_%1d'%(Re,i))
	system('rm memory_error')

	system('mpirun -np 26 python3 NSfracStep.py '+ \
		'problem=2DPipe_Rough_sin '+ \
		'Re=%1d '%Re +\
		'restart_folder=../2DPipe_Rough_sin_results/data/%1d/Checkpoint '%run +\
		'> Rough_Run%1d_Re%1d_Rs%1d'%(run,Re, i) )
i = 0

for j in range(start+1, len(Re_list)):

	Re = Re_list[j]
	if 'kill_loop' in listdir('.'):
		print('Kill Loop found!!')
		system('rm kill_loop')
		break
	
	print( 'starting RE=%1d'%Re)
	
	system('mpirun -np 26 python3 NSfracStep.py '+ \
		'problem=2DPipe_Rough_sin '+ \
		'Re=%1d '%Re +\
		#'dt=%1.7f '%dt +\
		'restart_folder=../2DPipe_Rough_sin_results/data/%1d/Checkpoint '%run+\
		'> Rough_Run%1d_Re%1d_Rs%1d'%(run,Re, i) )

	while 'memory_error' in listdir():
		if 'kill_loop' in listdir('.'):
			print('Kill Loop found!!')
			break
		i += 1
		print( 'starting RE=%1d_%1d'%(Re,i))
		system('rm memory_error')

		system('mpirun -np 26 python3 NSfracStep.py '+ \
			'problem=2DPipe_Rough_sin '+ \
			'Re=%1d '%Re +\
			'restart_folder=../2DPipe_Rough_sin_results/data/%1d/Checkpoint '%run +\
			'> Rough_Run%1d_Re%1d_Rs%1d'%(run,Re, i) )
	i = 0
