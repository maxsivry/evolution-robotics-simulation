import time as t
import pybullet as p
physicsClient = p.connect(p.GUI)

# to disable the sidebar uncomment following line
#p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
for i in range(1000):
    p.stepSimulation()
    t.sleep(1/60)
p.disconnect()
