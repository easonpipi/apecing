from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def plantTree(x,y,z):
    mc.setBlocks(x+1,y+2,z,x+3,y+4,z+2,174)
    mc.setBlocks(x+2,y,z+1,x+2,y+3,z+1,17)
x,y,z = mc.player.getPos()
for i in range(10):
    for h in range(10):
        plantTree(x,y,z)
        x+=5
        y+=1