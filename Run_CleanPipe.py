from os import system

#dt_list = [7.5e-7,  1e-3 , 2.5e-5 , 7.5e-7 ]
#Re_list = [8000, 100 , 3000 , 8000 ]
T = .5

Re_list = [16000, 500]

l_list = [0.5, 0.5, ]

for dt, Re, l in zip(dt_list, Re_list, l_list):
	system('mpirun -np 32 python NSfracStep.py '+ \
		'problem=2DPipe_Puff Re=%1d dt=%1.7f '%(Re, dt) + \
		'T=%1.1f l=%1.1f'%(T,l) )

