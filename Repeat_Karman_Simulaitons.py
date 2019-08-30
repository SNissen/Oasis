from os import system


for i in range(5):
	system('mpirun -np 18 python3 NSfracStep.py '+ \
		'problem=2DPipe_Circle > Karman_run%1d.txt'%i)

system('mpirun -np 18 python3 NSfracStep.py '+ \
		'problem=2DPipe_Rough > Rough_run14')