import sys
import os
import pycuber as pc
from pycuber.solver import CFOPSolver

#Würfel erstellen
cubie = pc.Cubie()
#                           000000000111111111222222222333333333444444444555555555
#                           000 000 000 111 111 111 222 222 222 333 333 333 444 444 444 555 555 555
#
#   0:red
#   1:yellow
#   2:green
#   3:white
#   4:orange
#   5:blue
#          !
top = "422415250" #Oben (Gelb) 1
bot = "333333333" #Unten (Weiß) 3
bac = "005145444" #Hinten (Orange) 4
fro = "141201000" #Vorne (Rot) 0
lef = "114054555" #Links (Blau) 5
rig = "511220222" #Rechts (Grün) 2
cubie = pc.array_to_cubies(lef + top + fro + bot + rig + bac)
print(cubie)
cube = pc.Cube(cubie)
cube_step = pc.Cube(cubie)

print(cube)

#Würfel mischen
#alg = pc.Formula()
#random_alg = alg.random()
#print(random_alg)
#cube(random_alg)
#print(cube)

#Würfel lösen
solver = CFOPSolver(cube)
solution = solver.solve(suppress_progress_messages=False)

#Würfel gelöst
print(cube)
for step in solution:
    cube_step(step)
    print(step)
    print(cube_step)


print('\x1b[6;30;42m' + 'Gelöst!' + '\x1b[0m')
