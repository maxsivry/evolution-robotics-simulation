import time as t
import pybullet as p
import pybullet_data
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# to disable the sidebar uncomment following line
p.configureDebugVisualizer()

#initiate gravitational force on z axis
p.setGravity(0,0,-9.8)

#create floor
planeId = p.loadURDF("plane.urdf")

#create world
p.loadSDF("world.sdf")

#create robo
robotID = p.loadURDF("body.urdf")

#run simul
for i in range(1000):
    p.stepSimulation()
    t.sleep(2/60)
p.disconnect()
