from os import system

dt_list = [ 8e-5, 8e-5, 8e-5, 5e-5, 5e-5, 2e-5, 2e-5, 2e-5, 1e-5, 1e-5, 9e-6]

Re_list = [  2e3,  3e3,  4e3,  5e3,  6e3,  7e3,  8e3,  9e3, 10e3, 11e3, 12e3]

dt_list = dt_list[-6:]

Re_list = Re_list[-6:]

for Re, dt in zip(Re_list, dt_list):
    system('mpirun -np 12 python NSfracStep.py problem=2DPipe_Puff '+\
           ' Re=%1i'%Re + \
           ' dt=%1.6f'%dt )
