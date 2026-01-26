import pyrosim.pyrosim as pyrosim

length = 1
width = 1
height = 1
x = 0
y = 0
z = 0.5

#create environemnt, where nultiple "links" or objects can exist
def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[x-2,y-2,z] , size=[length, width, height])
    pyrosim.End()


"""
Creating the body . . .
creating robot body, in Unified Robot Description format (.urdf)
in these files, all links must be attached by a joint. Bodies are organized as trees, such that the first cube/link will be the root and all the subsequent links/joints will refer to the previous node in memory. Joints must be placed in the relative position of two connecting links. The root link position is absolute, all subsequent links positions will reflect change of pos from previous links, same as with joints.

"""

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[0,0,0.5] , size=[length, width, height])
    
    #joints should always be named "Parent_Child" 
    pyrosim.Send_Joint( name = "Torso_Leg" , parent= "Torso" , child = "Leg" , type = "revolute", position = [0.5,0,1])
    pyrosim.Send_Cube(name="Leg", pos=[x+1,y,z+1] , size=[length, width, height])
    pyrosim.End()

Create_World()
Create_Robot()