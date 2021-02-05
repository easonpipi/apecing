from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
x,y,z=mc.player.getPos()

time.sleep(3)

ID=mc.getPlayerEntityId('pipi0505')
mc.postToTitle(ID,'3')
time.sleep(1)
mc.postToTitle(ID,'2')
time.sleep(1)
mc.postToTitle(ID,'1')
time.sleep(1)
mc.postToTitle(ID,'--開始--')

mc.setBlocks(x-10,y+1,z-1,x+10,y+1,z-1,0)
while True:
    
    x,y,z=mc.player.getPos()
    s=mc.getBlock(x,y-1,z)
    if s == 35:
        mc.postToTitle(ID,'----恭喜通過終點----')
        break