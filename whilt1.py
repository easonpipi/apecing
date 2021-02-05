from mcpi.minecraft import Minecraft
mc = Minecraft.create()

for i in range(20):
    x,y,z = mc.player.getPos()
    x=x+i
    mc.setBlock(x,y-1,z,57)
mc.setBlocks(x+1,y-1,z-2,x+5,y+3,z+2,169)
mc.setBlocks(x+2,y,z-1,x+4,y+2,z+1,0)
mc.setBlocks(x+1,y,z,x+1,y+1,z,0)