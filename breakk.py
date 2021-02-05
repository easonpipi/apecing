from mcpi.minecraft import Minecraft
mc = Minecraft.create()
from random import randrange

answer = randrange(0,16)
myID = mc.getPlayerEntityId("pipi0505")

while True:
    hits = mc.events.pollProjectileHits()
    if len(hits) > 0:
        hit = hits[0]
        
        block = mc.getBlockWithData(hit.pos)
        data = block.data
        
        if data<answer:
            mc.postToChat('錯的離譜')
        elif data>answer:
            mc.postToChat('錯的徹底')
        else:
            mc.setBlock(hit.pos,57)
            mc.postToTitle(myID,'!!!!!!!!!!猜對了!!!!!!!!!!')
            break