import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")
length = 1
width = 1
height = 1
x = 0
y = 0
z = 0.5
for k in range(5):
    x = 0
    for j in range(5):
        z = 0.5
        length = 1
        width = 1
        height = 1
        for i in range(5):
            pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length, width, height])
            z += 1
            length *= 0.9
            width *= 0.9
            height *= 0.9
        x += 1
    y += 1
pyrosim.End()