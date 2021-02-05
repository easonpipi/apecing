from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import random
x,y,z = mc.player.getPos()
y=y-1
mc.setBlock(x,y,z,169)

for i in range(20):
    rc = random.choice(range(1,7))
    if rc==1:
        mc.setBlocks(x+1,y,z,x+2,y,z,169)
        x=x+2
    if rc==2:
        mc.setBlocks(x-1,y,z,x-2,y,z,169)
        x=x-2
    if rc==3:
        mc.setBlocks(x,y,z+1,x,y,z+2,169)
        z=z+2
    if rc==4:
        mc.setBlocks(x,y,z-1,x,y,z-2,169)
        z=z-2
    if rc==5:
        mc.setBlocks(x,y+1,z,x,y+2,z,169)
        y=y+2
    if rc==6:
        mc.setBlocks(x,y-1,z,x,y-2,z,169)
        y=y-2