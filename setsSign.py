from mcpi.minecraft import Minecraft
mc = Minecraft.create()

Aa=[]
Bb=[]
Cc=[]
Dd=[]

for i in range(1,4):
    Aa.append(1*i)
for i in range(1,4):
    Bb.append(2*i)
for i in range(1,4):
    Cc.append(3*i)
for i in range(1,4):
    Dd.append(4*i)

x,y,z = mc.player.getPos()
mc.setSign(x,y,z,63,8,str(Aa),str(Bb),str(Cc),str(Dd))