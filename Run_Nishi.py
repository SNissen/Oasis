from os import system, listdir


Re_list = [7500, 8500, 9000, 9500, 10000]
run = '17'
start = 0
i = 0
print('starting RE=%1d_%1d'%(Re_list[start], i)) 

system('mpirun -np 26 python3 NSfracStep.py '+ \
		'problem=2DPipe_Nishi '+\
		'Re=%1d '%Re_list[start]+ \
		#'restart_folder=../2DPipe_Nishi_results/data/+run+/Checkpoint_r13 ' +\
		'> Nishi'+run+'_Re_%1d_%1d'%(Re_list[start],i) )


for Re in Re_list[start+1:]:
	run = str(max([int(x) for x in listdir('../2DPipe_Nishi_results/data/.')]) +1 )
	while 'memory_error' in listdir():
		if 'kill_loop' in listdir('.'):
			print('Kill Loop found!!')
			break
		
		i += 1
		run = str(int(num)+1)
		print( 'starting RE=%1d_%1d'%(Re-100,i))
		system('rm memory_error')
		
		system('mpirun -np 26 python3 NSfracStep.py '+ \
			'problem=2DPipe_Nishi '+ \
			'Re=%1d '%(Re-100) +\
			#'dt=%1.7f '%dt +\
			'restart_folder=../2DPipe_Nishi_results/data/'+run+'/Checkpoint '+\
			'> Nishi'+run+'_Re_%1d_%1d'%(Re-100, i) )
	i = 0
	if 'kill_loop' in listdir('.'):
		print('Kill Loop found!!')
		system('rm kill_loop')
		break

	print( 'starting RE=%1d_%1d'%(Re,i))
	
	system('mpirun -np 26 python3 NSfracStep.py '+ \
		'problem=2DPipe_Nishi '+ \
		'Re=%1d '%Re +\
		#'restart_folder=../2DPipe_Nishi_results/data/'+run+'/Checkpoint '+\
		'> Nishi'+run+'_Re_%1d'%Re )