
import turtle
import random
import time
import math
# -------screen and turtle creation-----------------
startgame = False
bumper = 3
blockcheck = 1
walkframes = 0
bonusstate = 0
multi = 0
highestscore = '000000'
highscore = 0
frameovergameover = 0
points = 0
scorep1 = '000000'
pointsche = 0
scorep2 = '000000'
lift3 = 0
lift2 = 0
lift = 0
gravitymod = 0.5
speedupper = 1
apress = False
dpress = False
wpress = False
spacepress = False
spawnstopper = 0
stage = 1
stagecomp = 0
alternator = -1
pickupblock = 0
destroyed = 0
fuelspawn = 0
facing = 10
resetmap = False
controls = 0
lives = 4
falling = True
groundcheck = True
autoshoot = 0
shapesize = 3
delay = 1
gravycor = 0
updatelives = 3
nostart = True
landing = False
moveDist = 0
relocate = True
isDed = False
pts = 0
colorcounter = 0
updatepts = 0
maxspeed = 5
move1 = 0
move2 = 0
move3 = 0
move4 = 0
mywindow = turtle.Screen()
mywindow.title("Jetpac")
mywindow.bgcolor("black")
turtle.setup(640, 640)
#----INITALIZING TITLESCREEN----
mywindow.tracer(0,0)
titlescreen = turtle.Turtle()
title = "title.gif"
mywindow.addshape(title)
titlescreen.shape(title)
mywindow.update()
time.sleep(3)

# ------
'''
randomstars = turtle.Turtle()
randomstars.hideturtle()
randomstars.penup()
randomstars.color("white")
randomstars.pencolor("white")
randomstars.shape("circle")
randomstars.shapesize(0.1,0.1)
for h in range(0,40,1):
    randomstars.goto(random.randint(-300,350),random.randint(-250,250))
    randomstars.pendown()
    randomstars.stamp()
    randomstars.penup()
'''
gui = turtle.Turtle()
gui.hideturtle()
gui.penup()
gui.pencolor("cyan")
gui.goto(0,-30)
gui.penup()
pointturt = turtle.Turtle()
pointturt.hideturtle()
pointturt.penup()
pointturt.goto(-200,280)
pointturt.pencolor("white")
pointturt.pendown()
pointturt.write("1UP", "", "center", ("fixedsys", 15, "normal"))
pointturt2 = turtle.Turtle()
pointturt2.hideturtle()
pointturt2.penup()
pointturt2.goto(200,280)
pointturt2.pencolor("white")
pointturt2.pendown()
pointturt2.write("2UP", "", "center", ("fixedsys", 15, "normal"))
pointturt3 = turtle.Turtle()
pointturt3.hideturtle()
pointturt3.penup()
pointturt3.goto(0,280)
pointturt3.pencolor('#01fffe')
pointturt3.pendown()
pointturt3.write("HI", "", "center", ("fixedsys", 15, "normal"))
Hiscore = turtle.Turtle()
Hiscore.hideturtle()
Hiscore.penup()
Hiscore.goto(0,250)
Hiscore.pencolor('yellow')
Hiscore.pendown()
Hiscore.write(highestscore, "", "center", ("fixedsys", 15, "normal"))
p1s = turtle.Turtle()
p1s.hideturtle()
p1s.penup()
p1s.goto(-200,250)
p1s.pencolor('yellow')
p1s.pendown()
p1s.write(scorep1, "", "center", ("fixedsys", 15, "normal"))
p2s = turtle.Turtle()
p2s.hideturtle()
p2s.penup()
p2s.goto(200,250)
p2s.pencolor('yellow')
p2s.pendown()
p2s.write(scorep2, "", "center", ("fixedsys", 15, "normal"))
ls = turtle.Turtle()
ls.hideturtle()
ls.penup()
ls.goto(-160,280)
ls.pencolor('white')
ls.pendown()
ls2 = turtle.Turtle()
ls2.hideturtle()
ls2.penup()
ls2.goto(-150,280)
s1p1w = "s1p1w.gif"
mywindow.addshape(s1p1w)
s1p2w = "s1p2w.gif"
mywindow.addshape(s1p2w)
s2p1w = "s2p1w.gif"
mywindow.addshape(s2p1w)
s2p2w = "s2p2w.gif"
mywindow.addshape(s2p2w)
s3p1w = "s3p1w.gif"
mywindow.addshape(s3p1w)
s3p2w = "s3p2w.gif"
mywindow.addshape(s3p2w)
s1p1m = "s1p1m.gif"
mywindow.addshape(s1p1m)
s1p2m = "s1p2m.gif"
mywindow.addshape(s1p2m)
s2p1m = "s2p1m.gif"
mywindow.addshape(s2p1m)
s2p2m = "s2p2m.gif"
mywindow.addshape(s2p2m)
s3p1m = "s3p1m.gif"
mywindow.addshape(s3p1m)
s3p2m = "s3p2m.gif"
mywindow.addshape(s3p2m)
smolplatform = "smolplatform.gif"
mywindow.addshape(smolplatform)
bigplatform = "bigplatform.gif"
mywindow.addshape(bigplatform)


jewel = "jewel.gif"
mywindow.addshape(jewel)
molec = "molec.gif"
mywindow.addshape(molec)
gel = "gel.gif"
mywindow.addshape(gel)
gold = "gold.gif"
mywindow.addshape(gold)
rad = "rad.gif"
mywindow.addshape(rad)

fuzzc = "fuzzc.gif"
mywindow.addshape(fuzzc)
fuzzr = "fuzzr.gif"
mywindow.addshape(fuzzr)
fuzzm = "fuzzm.gif"
mywindow.addshape(fuzzm)
fuzzg = "fuzzg.gif"
mywindow.addshape(fuzzg)
fuzz2c = "fuzz2c.gif"
mywindow.addshape(fuzz2c)
fuzz2r = "fuzz2r.gif"
mywindow.addshape(fuzz2r)
fuzz2m = "fuzz2m.gif"
mywindow.addshape(fuzz2m)
fuzz2g = "fuzz2g.gif"
mywindow.addshape(fuzz2g)

bubc = "bubc.gif"
mywindow.addshape(bubc)
bubr = "bubr.gif"
mywindow.addshape(bubr)
bubm = "bubm.gif"
mywindow.addshape(bubm)
bubg = "bubg.gif"
mywindow.addshape(bubg)
bub2c = "bub2c.gif"
mywindow.addshape(bub2c)
bub2m = "bub2m.gif"
mywindow.addshape(bub2m)
bub2r = "bub2r.gif"
mywindow.addshape(bub2r)
bub2g = "bub2g.gif"
mywindow.addshape(bub2g)

birdg = "birdg.gif"
mywindow.addshape(birdg)
birdr = "birdr.gif"
mywindow.addshape(birdr)
birdc = "birdc.gif"
mywindow.addshape(birdc)
birdm = "birdm.gif"
mywindow.addshape(birdm)
birdgf = "birdgf.gif"
mywindow.addshape(birdgf)
birdrf = "birdrf.gif"
mywindow.addshape(birdrf)
birdcf = "birdcf.gif"
mywindow.addshape(birdcf)
birdmf = "birdmf.gif"
mywindow.addshape(birdmf)

ufog = "ufog.gif"
mywindow.addshape(ufog)
ufor = "ufor.gif"
mywindow.addshape(ufor)
ufoc = "ufoc.gif"
mywindow.addshape(ufoc)
ufom = "ufom.gif"
mywindow.addshape(ufom)

jetmanlives = "jetmanlives.gif"
mywindow.addshape(jetmanlives)

ground = "ground.gif"
mywindow.addshape(ground)

rockf1r = "rockf1r.gif"
mywindow.addshape(rockf1r)
rockf2r = "rockf2r.gif"
mywindow.addshape(rockf2r)
rockf1g = "rockf1g.gif"
mywindow.addshape(rockf1g)
rockf2g = "rockf2g.gif"
mywindow.addshape(rockf2g)
rockf1c = "rockf1c.gif"
mywindow.addshape(rockf1c)
rockf2c = "rockf2c.gif"
mywindow.addshape(rockf2c)
rockf1m = "rockf1m.gif"
mywindow.addshape(rockf1m)
rockf2m = "rockf2m.gif"
mywindow.addshape(rockf2m)

rockf1rl = "rockf1rl.gif"
mywindow.addshape(rockf1rl)
rockf2rl = "rockf2rl.gif"
mywindow.addshape(rockf2rl)
rockf1gl = "rockf1gl.gif"
mywindow.addshape(rockf1gl)
rockf2gl = "rockf2gl.gif"
mywindow.addshape(rockf2gl)
rockf1cl = "rockf1cl.gif"
mywindow.addshape(rockf1cl)
rockf2cl = "rockf2cl.gif"
mywindow.addshape(rockf2cl)
rockf1ml = "rockf1ml.gif"
mywindow.addshape(rockf1ml)
rockf2ml = "rockf2ml.gif"
mywindow.addshape(rockf2ml)


jetf1l = "jetf1l.gif"
mywindow.addshape(jetf1l)
jetf2l = "jetf2l.gif"
mywindow.addshape(jetf2l)
jetf3l = "jetf3l.gif"
mywindow.addshape(jetf3l)
jetf4l = "jetf4l.gif"
mywindow.addshape(jetf4l)
jetf1r = "jetf1r.gif"
mywindow.addshape(jetf1r)
jetf2r = "jetf2r.gif"
mywindow.addshape(jetf2r)
jetf3r = "jetf3r.gif"
mywindow.addshape(jetf3r)
jetf4r = "jetf4r.gif"
mywindow.addshape(jetf4r)
jetaf1l = "jetaf1l.gif"
mywindow.addshape(jetaf1l)
jetaf2l = "jetaf2l.gif"
mywindow.addshape(jetaf2l)
jetaf3l = "jetaf3l.gif"
mywindow.addshape(jetaf3l)
jetaf4l = "jetaf4l.gif"
mywindow.addshape(jetaf4l)
jetaf1r = "jetaf1r.gif"
mywindow.addshape(jetaf1r)
jetaf2r = "jetaf2r.gif"
mywindow.addshape(jetaf2r)
jetaf3r = "jetaf3r.gif"
mywindow.addshape(jetaf3r)
jetaf4r = "jetaf4r.gif"
mywindow.addshape(jetaf4r)
ls2.shape(jetmanlives)
miner = turtle.Turtle()
miner.speed(0)
miner.color("white")
miner.shape(jetf1l)
miner.shapesize(1.45,2.5)
miner.setheading(90)
miner.penup()
miner.goto(0,-175)
miner.hideturtle()
rockets1p1 = turtle.Turtle()
rockets1p1.turtlesize(0.75,1.5)
rockets1p1.color('white')
rockets1p1.shape(s1p1w)
rockets1p1.speed(0)
rockets1p1.penup()
rockets1p1.goto(100,-190)
rockets1p1.hideturtle()
rockets1p2 = turtle.Turtle()
rockets1p2.turtlesize(0.75,1.5)
rockets1p2.color('white')
rockets1p2.shape(s1p2w)
rockets1p2.speed(0)
rockets1p2.penup()
rockets1p2.goto(100,-175)
rockets1p2.hideturtle()
rockets2p1 = turtle.Turtle()
rockets2p1.turtlesize(0.75,1.5)
rockets2p1.color('white')
rockets2p1.shape(s2p1w)
rockets2p1.speed(0)
rockets2p1.penup()
rockets2p1.goto(0,25)
rockets2p1.hideturtle()
rockets2p2 = turtle.Turtle()
rockets2p2.turtlesize(0.75,1.5)
rockets2p2.color('white')
rockets2p2.shape(s2p2w)
rockets2p2.speed(0)
rockets2p2.penup()
rockets2p2.goto(0,40)
rockets2p2.hideturtle()
rockets3p1 = turtle.Turtle()
rockets3p1.turtlesize(0.75,1.5)
rockets3p1.color('white')
rockets3p1.shape(s3p1w)
rockets3p1.speed(0)
rockets3p1.penup()
rockets3p1.goto(-195,85)
rockets3p1.hideturtle()
rockets3p2 = turtle.Turtle()
rockets3p2.turtlesize(0.75,1.5)
rockets3p2.color('white')
rockets3p2.shape(s3p2w)
rockets3p2.speed(0)
rockets3p2.penup()
rockets3p2.goto(-195,100)
rockets3p2.hideturtle()
brick1 = turtle.Turtle()
brick1.turtlesize(1,4)
brick1.penup()
brick1.color('lightgreen')
brick1.shape(smolplatform)
brick1.goto(0,-20)
brick1.hideturtle()
brick1SemiLength = 10
brick1SemiLength2 = 40
brick2SemiLength2 = 50
brick2 = turtle.Turtle()
brick2.turtlesize(1,6)
brick2.color('lightgreen')
brick2.shape(bigplatform)
brick2.speed(0)
brick2.penup()
brick2.goto(205,110)
brick2.hideturtle()
brick3 = turtle.Turtle()
brick3.turtlesize(1,6)
brick3.color('lightgreen')
brick3.shape(bigplatform)
brick3.speed(0)
brick3.penup()
brick3.goto(-195,65)
brick3.hideturtle()
bonus = turtle.Turtle()
bonus.speed(0)
bonus.penup()
bonus.hideturtle()
bonus.goto(0,400)
floor = turtle.Turtle()
floor.turtlesize(10,60)
floor.color('#fffc36')
floor.shape(ground)
floor.speed(0)
floor.penup()
floor.goto(0,-207)
floor.hideturtle()
instructions = turtle.Turtle()
instructions.hideturtle()
instructions.pencolor("white")
instructions.penup()
instructions.goto(0,150)
instructions.pendown()
instructions.write("JETPAC  GAME  SELECTION","","center",("fixedsys",17,"normal"))
instructions.penup()
instructions.goto(-100,90)
instructions.pendown()
instructions.write("1    1  PLAYER GAME","","left",("fixedsys",17,"normal"))
instructions2 = turtle.Turtle()
instructions2.hideturtle()
instructions2.pencolor('white')
instructions.penup()
instructions.goto(-100,30)
instructions.pendown()
instructions.write("2    DEFAULT  LASER","","left",("fixedsys",17,"normal"))
instructions2.penup()
instructions2.goto(-100,-30)
instructions2.pendown()
instructions2.write("3    WASD CONTROLS","","left",("fixedsys",17,"normal"))
instructions.penup()
instructions.goto(-22,-180)
instructions.pendown()
instructions.write("5    START  GAME","","center",("fixedsys",17,"normal"))
instructions.penup()
instructions.goto(0,-250)
instructions.pendown()
instructions.write("2017 RARE LTD. ALL RIGHTS RESERVED ","","center",("fixedsys",17,"normal"))
instructions.penup()
instructions.goto(0,-290)
instructions.pendown()
instructions.write("ORIGINAL  BY  CHRIS  &  TIM  S.    REMAKE  BY  BEN M.","","center",("fixedsys",10,"normal"))
# ------------functions-----------------
def leave():
    global quitFlag
    quitFlag = True
    return
def controlswitch():
    global controls
    if controls == 0:
        controls = 1
        instructions2.clear()
        instructions2.write("3    CLASSIC CONTROLS","","left",("fixedsys",17,"normal"))
    elif controls == 1:
        controls = 0
        instructions2.clear()
        instructions2.write("3    WASD CONTROLS", "", "left", ("fixedsys", 17, "normal"))
def isapressed():
    global apress
    if controls == 0:
        apress = True
    return
def isareleased():
    global apress
    if controls == 0:
        apress = False
    return
def isbpressed():
    global apress
    if controls == 1:
        apress = True
    return
def isbreleased():
    global apress
    if controls == 1:
        apress = False
    return
def isnpressed():
    global dpress
    if controls == 1:
        dpress = True
    return
def isnreleased():
    global dpress
    if controls == 1:
        dpress = False
    return
def isdpressed():
    global dpress
    if controls == 0:
        dpress = True
    return
def isdreleased():
    global dpress
    if controls == 0:
        dpress = False
    return
def iswpressed():
    global wpress
    wpress = True
    return
def iswreleased():
    global wpress
    wpress = False
    return
def isspressed():
    global spacepress
    if controls == 1:
        spacepress = True
    return
def issreleased():
    global spacepress
    if controls == 1:
        spacepress = False
    return
def isspacepressed():
    global spacepress
    if controls == 0:
        spacepress = True
    return
def isspacereleased():
    global spacepress
    if controls == 0:
        spacepress = False

def automaticloop():
    global autoshoot, spacepress
    if startgame == True and spacepress == True:
        autoshoot += 1
        if autoshoot == 10 or autoshoot == 0:
            autoshoot = 0
            shoot()
    return
def left():
    global facing, blockcheck
    if startgame == True and apress == True:
        facing = -10
        if miner.ycor() == -175 or blockcheck == 2:
            miner.goto(miner.xcor() - (0.22*fwdAmnt), miner.ycor())
        elif blockcheck == 1:
            miner.goto(miner.xcor() - (0.8*fwdAmnt),miner.ycor())
        return
def right():
    global facing
    if startgame == True and dpress == True:
        facing = 10
        if miner.ycor() == -175 or blockcheck == 2:
            miner.goto(miner.xcor() + (0.22*fwdAmnt), miner.ycor())
        elif blockcheck == 1:
            miner.goto(miner.xcor() + (0.8*fwdAmnt), miner.ycor())
        return
'''
def faster():
    global moveDist, groundcheck, falling
    if wpress == True:
        groundcheck = True
        falling = True
        print('j')
        if miner.ycor() <= -175 and groundcheck == True:
            if moveDist == 0:
                moveDist = (gravitymod) + 0.1 + fwdAmnt
                print('w')
            groundcheck = False
            print('w1')
        if miner.ycor() >= -175 and moveDist < (gravitymod *fwdAmnt) + 0.1  and wpress == True:
            moveDist = moveDist + 0.5
        if miner.ycor() >= 300:
            miner.goto(miner.xcor(),300)
    return
'''
def walkcycle():
    global walkframes
    if miner.ycor() == -175 or blockcheck == 2:
        if facing == 10:
            if dpress == True:
                walkframes += 1
                if walkframes == 5:
                    miner.shape(jetf2r)
                if walkframes == 10:
                    miner.shape(jetf3r)
                if walkframes == 15:
                    miner.shape(jetf4r)
                if walkframes == 20:
                    miner.shape(jetf1r)
                    walkframes = 0
            else:
                miner.shape(jetf1r)
                walkframes = 0
        if facing == -10:
            if apress == True:
                walkframes += 1
                if walkframes == 5:
                    miner.shape(jetf2l)
                if walkframes == 10:
                    miner.shape(jetf3l)
                if walkframes == 15:
                    miner.shape(jetf4l)
                if walkframes == 20:
                    miner.shape(jetf1l)
                    walkframes = 0
            else:
                miner.shape(jetf1l)
                walkframes = 0
    if blockcheck == 1 and miner.ycor() != -175:
        if facing == 10:
            walkframes += 1
            if walkframes == 5:
                miner.shape(jetaf1r)
            if walkframes == 10:
                miner.shape(jetaf2r)
            if walkframes == 15:
                miner.shape(jetaf3r)
            if walkframes == 20:
                miner.shape(jetaf4r)
                walkframes = 0
        if facing == -10:
            walkframes += 1
            if walkframes == 5:
                miner.shape(jetaf1l)
            if walkframes == 10:
                miner.shape(jetaf2l)
            if walkframes == 15:
                miner.shape(jetaf3l)
            if walkframes == 20:
                miner.shape(jetaf4l)
                walkframes = 0
def noW():
    global falling, wpress
    falling = False
    wpress = False
    return
def start():
    global nostart
    if nostart == True:
        global startgame
        startgame = True
        rockets1p1.showturtle()
        rockets1p2.showturtle()
        rockets2p1.showturtle()
        rockets2p2.showturtle()
        rockets3p1.showturtle()
        rockets3p2.showturtle()
        brick1.showturtle()
        brick2.showturtle()
        brick3.showturtle()
        ls.write(lives, "", "center", ("fixedsys", 15, "normal"))
        ls2.showturtle()
        floor.showturtle()
        miner.showturtle()
        instructions.clear()
        instructions2.clear()
        nostart = False
def gravy(m1,rad,player):
    global gravycor, groundcheck, moveDist, falling
    if startgame == True:
        if player == 1 and wpress == True:
            m1.goto(m1.xcor(), m1.ycor() + (gravitymod * fwdAmnt)+3)
        if m1.ycor() > -200 + rad:
            m1.goto(m1.xcor(), m1.ycor() - (gravitymod*fwdAmnt))
        if player == 1 and wpress == False and miner.ycor() != -600:
            if m1.ycor() <= -200 + rad:
                m1.goto(m1.xcor(),-175)
def edgewrap(t):
    #t - a turtle, r = its radius
    if t.xcor() > (340) or t.xcor() < (-340):
        t.hideturtle()
        t.penup()
        t.setx(-1 * t.xcor())
        t.showturtle()
        t.forward(1)
    if t != miner:
        if t.ycor() > (340) or t.ycor() < (-340):
            t.hideturtle()
            t.penup()
            t.setx(-1 * t.xcor())
            t.showturtle()
            t.forward(1)
    return
def collideBounce(t1,r1,s1,t2,r2,s2): # s = speed, t = turtle, r = radius, # denotes the turtle
    global bumper
    dist = ( (t1.xcor() - t2.xcor())**2 + (t1.ycor() - t2.ycor())**2) ** 0.5
    if dist < (r1 + r2):
        newHead1 = t2.heading() + random.randint(-3,3)
        newHead2 = t1.heading() + random.randint(-3,3)
        t1.setheading(newHead1)
        t1.forward(s1 + bumper)
        t2.setheading(newHead2)
        t2.forward(s2 + bumper)
        if relocate == True:
            t1.goto(random.randint(-300,350),random.randint(-250,250))
    return
def brickbounce(t1,r1,b1,sem1,sem2, smabig):
    global move1
    global move2
    global move3
    global move4
    global bumper
    #b1 = a brick, sem1 = its semilength
    brickBottom = b1.ycor() - sem1
    brickTop = b1.ycor() + sem1
    brickLeft = b1.xcor() - sem2
    brickRight = b1.xcor() + sem2
    rockBottom = t1.ycor() - r1
    rockTop = t1.ycor() + r1
    rockRight = t1.xcor() + r1
    rockLeft = t1.xcor() - r1
    #setect a top collision
    if rockBottom < brickTop and rockLeft < brickRight and rockRight > brickLeft and rockTop > brickBottom and stage == 2:
        ang = t1.towards(b1.xcor(), b1.ycor())
        if smabig == 0:
            if ang <= 14.036 or ang >= 345.964:
                t1.setheading(180 - t1.heading())
                t1.forward(bumper)
            elif ang <= 165.964 and ang >= 14.036:
                t1.setheading(360 - t1.heading())
                t1.forward(bumper)
            elif ang <= 194.036 and ang >= 165.964:
                t1.setheading(180 - t1.heading())
                t1.forward(bumper)
            else:
                t1.setheading(360 - t1.heading())
                t1.forward(bumper)
        else:
            if ang <= 9.462 or ang >= 350.538:
                t1.setheading(180 - t1.heading())
                t1.forward(bumper)
            elif ang <= 170.538 and ang >= 9.462:
                t1.setheading(360 - t1.heading())
            elif ang <= 189.462 and ang >= 170.538:
                t1.setheading(180 - t1.heading())
                t1.forward(bumper)
            else:
                t1.setheading(360 - t1.heading())
        return
def brickcollide(t1,r1,b1,sem1,sem2,offset,offset2,smabig,isminer):
    global move1, blockcheck
    global move2
    global move3
    global move4
    global bumper
    #b1 = a brick, sem1 = its semilength
    brickBottom = b1.ycor() - sem1 - offset
    brickTop = b1.ycor() + sem1 + offset
    brickLeft = b1.xcor() - sem2 - offset2
    brickRight = b1.xcor() + sem2 + offset2
    rockBottom = t1.ycor() - r1
    rockTop = t1.ycor() + r1
    rockRight = t1.xcor() + r1
    rockLeft = t1.xcor() - r1
    #setect a top collision
    if rockBottom < brickTop and rockLeft < brickRight and rockRight > brickLeft and rockTop > brickBottom:
        ang = t1.towards(b1.xcor(), b1.ycor())
        if smabig == 0:
            if ang <= 14.036 or ang >= 345.964:
                t1.goto(t1.xcor() - 13, t1.ycor())
            elif ang <= 165.964 and ang >= 14.036:
                t1.goto(t1.xcor(), brickBottom - 0.05)
            elif ang <= 194.036 and ang >= 165.964:
                t1.goto(t1.xcor() + 13,t1.ycor())
            else:
                t1.goto(t1.xcor(), t1.ycor() + (gravitymod*fwdAmnt))
                if isminer == 1:
                    blockcheck = 2

        else:
            if ang <= 9.462 or ang >= 350.538:
                t1.goto(t1.xcor() - 13, t1.ycor())
            elif ang <= 170.538 and ang >= 9.462:
                t1.goto(t1.xcor(), brickBottom - 0.05)
            elif ang <= 189.462 and ang >= 170.538:
                t1.goto(t1.xcor() + 13, t1.ycor())
            else:
                t1.goto(t1.xcor(), t1.ycor() + (gravitymod*fwdAmnt))
                if isminer == 1:
                    blockcheck = 2

    else:
        if isminer == 1 and blockcheck != 2:
            blockcheck = 1


def brickcollidelarge(t1,r1,b1,sem1,sem2,offset,offset2):
    global move1
    global move2
    global move3
    global move4
    global bumper
    #b1 = a brick, sem1 = its semilength
    brickBottom = b1.ycor() - sem1 - offset
    brickTop = b1.ycor() + sem1 + offset
    brickLeft = b1.xcor() - sem2 - offset2
    brickRight = b1.xcor() + sem2 + offset2
    rockBottom = t1.ycor() - r1
    rockTop = t1.ycor() + r1
    rockRight = t1.xcor() + r1
    rockLeft = t1.xcor() - r1
    #setect a top collision
    if rockBottom < brickTop and rockLeft < brickRight and rockRight > brickLeft and rockTop > brickBottom:
        ang = t1.towards(b1.xcor(), b1.ycor())
        if ang <= 9.462 or ang >= 350.538:
            t1.goto(t1.xcor() - 13, t1.ycor())
        elif ang <= 170.538 and ang >= 9.462:
            t1.goto(t1.xcor(), brickBottom - 16)
        elif ang <= 189.462 and ang >= 170.538:
            t1.goto(t1.xcor() + 13,t1.ycor())
        else:
            t1.goto(t1.xcor(),t1.ycor()+0.5)
            blockcheck = False
        return
def rocketglue(t1,t2):
    t1.goto(t2.xcor(),t2.ycor()+15)
    return
def partlifters1(t1,t2,pos,stage):
    global lift, pickupblock, points
    dist = ((t1.xcor() - t2.xcor()) ** 2 + (t1.ycor() - t2.ycor()) ** 2) ** 0.5
    if dist <= 25 and lift != 2 and lift != 1:
        lift = 1
        points += 100
    if lift == 1:
        if t2.xcor() >= 88 and t2.xcor() <= 113:
            isdropped = True
            lift = 2
        else:
            isdropped = False
            t2.goto(t1.xcor(),t1.ycor() -15)
    if lift == 2:
        t2.goto(100,t2.ycor()+(0.25*fwdAmnt))
        if t2.ycor() <= pos:
            t2.goto(t2.xcor(),pos)
            pickupblock = 1
def partlifters2(t1,t2,pos,stage):
    global lift2, fuelspawn, points
    if pickupblock == 1:
        dist = ((t1.xcor() - t2.xcor()) ** 2 + (t1.ycor() - t2.ycor()) ** 2) ** 0.5
        if dist <= 25 and lift2 != 2 and lift2 != 1:
            lift2 = 1
            points += 100
        if lift2 == 1:
            if t2.xcor() >= 88 and t2.xcor() <= 113:
                isdropped = True
                lift2 = 2
            else:
                isdropped = False
                t2.goto(t1.xcor(),t1.ycor() - 15) #650 to 900
        if lift2 == 2:
            t2.goto(100,t2.ycor()+(0.25*fwdAmnt))
            if t2.ycor() <= pos:
                t2.goto(t2.xcor(),pos)
                if fuelspawn != 2:
                    fuelspawn = 1
def partlifterf(t1,t2,fuelnum):
    global lift3, fuelspawn, fuelstates, colorcounter, stagecomp, points
    if fuelspawn == 2:
        dist = ((t1.xcor() - t2.xcor()) ** 2 + (t1.ycor() - t2.ycor()) ** 2) ** 0.5
        if dist <= 25 and fuelstates[fuelnum] != 2 and fuelstates[fuelnum] != 1:
            fuelstates[fuelnum] = 1
            points += 100
        if fuelstates[fuelnum] == 1:
            if t2.xcor() >= 88 and t2.xcor() <= 113:
                isdropped = True
                fuelstates[fuelnum] = 2
            else:
                isdropped = False
                t2.goto(t1.xcor(),t1.ycor() -15)
        if fuelstates[fuelnum] == 2 or fuelstates[fuelnum] == 3:
            t2.goto(100,t2.ycor()+(0.25*fwdAmnt))
            if t2.ycor() <= -130:
                t2.hideturtle()
                t2.goto(-1000,-1000)
                if fuelnum == 0:
                    rockets1p1.shape(s1p1m)
                    print('1')
                if fuelnum == 1:
                    rockets1p2.shape(s1p2m)
                    print('2')
                if fuelnum == 2:
                    rockets2p1.shape(s2p1m)
                    print('3')
                if fuelnum == 3:
                    rockets2p2.shape(s2p2m)
                    print('4')
                if fuelnum == 4:
                    rockets3p1.shape(s3p1m)
                    print('5')
                if fuelnum == 5:
                    rockets3p2.shape(s3p2m)
                    stagecomp = 1
                    flashingrocket()
                    print('6')
                if fuelstates[fuelnum] != 3:
                    fuelspawn = 1
                    fuelstates[fuelnum] = 3
def spawnfuel():
    global fuel, fuelIndex, fuelstates, fuelspawn
    if fuelspawn == 1 and len(fuel) != 6:
        fuelspawn = 2
        fuelIndex += 1
        fuel.append(turtle.Turtle())
        fuel[fuelIndex].color('magenta')
        fuelimage = "fuel.gif"
        mywindow.addshape(fuelimage)
        fuel[fuelIndex].shape(fuelimage)
        fuel[fuelIndex].turtlesize(1,9)
        fuel[fuelIndex].penup()
        fuel[fuelIndex].hideturtle()
        spawnpoint = random.randint(2,5)
        if spawnpoint == 2:
            fuel[fuelIndex].goto(-195,330)
        if spawnpoint == 3:
            fuel[fuelIndex].goto(-100,330)
        if spawnpoint == 4:
            fuel[fuelIndex].goto(0,330)
        if spawnpoint == 5:
            fuel[fuelIndex].goto(200,330)
        fuel[fuelIndex].showturtle()
        fuelstates.append(0)
        print('fuel spawned')
        return
def enemyspawn(respawn,k):
    global enemy, enemyIndex, enemystates, fuelspawn, stage
    if respawn == 1:
        enemyIndex += 1
        enemy.append(turtle.Turtle())
        enemycolors.append(0)
        enemy[enemyIndex].color('magenta')
        enemy[enemyIndex].turtlesize(1.2,1.2)
        enemy[enemyIndex].penup()
        enemy[enemyIndex].hideturtle()
        enemyproperties(enemyIndex)
        enemy[enemyIndex].showturtle()
        enemyaltstates.append(0)
        enemystates.append(0)
        print('baddie spawned')
    return

def enemyproperties(enemyIndex):
    global enemy,enemystates, fuelspawn, stage, enemycolors
    spawnpoint = random.randint(2, 3)
    if spawnpoint == 2:
        enemy[enemyIndex].goto(-330, random.randint(-180, 310))
        if stage == 1:
            headin = random.randint(2, 3)
            if headin == 2:
                enemy[enemyIndex].setheading(350)
            if headin == 3:
                enemy[enemyIndex].setheading(359)
            colorchooser = random.randint(2, 6)
            if colorchooser == 5:
                enemy[enemyIndex].shape(rockf1c)
                enemycolors[enemyIndex] = 1
            elif colorchooser == 4:
                enemy[enemyIndex].shape(rockf1r)
                enemycolors[enemyIndex] = 2
            elif colorchooser == 3:
                enemy[enemyIndex].shape(rockf1g)
                enemycolors[enemyIndex] = 3
            else:
                enemy[enemyIndex].shape(rockf1m)
                enemycolors[enemyIndex] = 4
        if stage == 2:
            enemy[enemyIndex].setheading(120)
            colorchooser = random.randint(2, 6)
            if colorchooser == 5:
                enemy[enemyIndex].shape(fuzzc)
                enemycolors[enemyIndex] = 1
            elif colorchooser == 4:
                enemy[enemyIndex].shape(fuzzr)
                enemycolors[enemyIndex] = 2
            elif colorchooser == 3:
                enemy[enemyIndex].shape(fuzzg)
                enemycolors[enemyIndex] = 3
            else:
                enemy[enemyIndex].shape(fuzzm)
                enemycolors[enemyIndex] = 4
        if stage == 3:
            colorchooser = random.randint(2, 6)
            if colorchooser == 5:
                enemy[enemyIndex].shape(bubc)
                enemycolors[enemyIndex] = 1
            elif colorchooser == 4:
                enemy[enemyIndex].shape(bubr)
                enemycolors[enemyIndex] = 2
            elif colorchooser == 3:
                enemy[enemyIndex].shape(bubg)
                enemycolors[enemyIndex] = 3
            else:
                enemy[enemyIndex].shape(bubm)
                enemycolors[enemyIndex] = 4
        if stage == 4:
            colorchooser = random.randint(2, 6)
            if colorchooser == 5:
                enemy[enemyIndex].shape(birdc)
                enemycolors[enemyIndex] = 1
            elif colorchooser == 4:
                enemy[enemyIndex].shape(birdr)
                enemycolors[enemyIndex] = 2
            elif colorchooser == 3:
                enemy[enemyIndex].shape(birdg)
                enemycolors[enemyIndex] = 3
            else:
                enemy[enemyIndex].shape(birdm)
                enemycolors[enemyIndex] = 4
        if stage == 5:
            colorchooser = random.randint(2, 6)
            if colorchooser == 5:
                enemy[enemyIndex].shape(ufoc)
                enemycolors[enemyIndex] = 1
            elif colorchooser == 4:
                enemy[enemyIndex].shape(ufor)
                enemycolors[enemyIndex] = 2
            elif colorchooser == 3:
                enemy[enemyIndex].shape(ufog)
                enemycolors[enemyIndex] = 3
            else:
                enemy[enemyIndex].shape(ufom)
                enemycolors[enemyIndex] = 4
    if spawnpoint == 3:
        enemy[enemyIndex].goto(330, random.randint(-180, 310))
        if stage == 1:
            headin = random.randint(2, 3)
            if headin == 2:
                enemy[enemyIndex].setheading(190)
            if headin == 3:
                enemy[enemyIndex].setheading(181)
            colorchooser = random.randint(2, 6)
            if colorchooser == 5:
                enemy[enemyIndex].shape(rockf1cl)
                enemycolors[enemyIndex] = 5
            elif colorchooser == 4:
                enemy[enemyIndex].shape(rockf1rl)
                enemycolors[enemyIndex] = 6
            elif colorchooser == 3:
                enemy[enemyIndex].shape(rockf1gl)
                enemycolors[enemyIndex] = 7
            else:
                enemy[enemyIndex].shape(rockf1ml)
                enemycolors[enemyIndex] = 8
        if stage == 2:
            enemy[enemyIndex].setheading(60)
            colorchooser = random.randint(2, 6)
            if colorchooser == 5:
                enemy[enemyIndex].shape(fuzzc)
                enemycolors[enemyIndex] = 1
            elif colorchooser == 4:
                enemy[enemyIndex].shape(fuzzr)
                enemycolors[enemyIndex] = 2
            elif colorchooser == 3:
                enemy[enemyIndex].shape(fuzzg)
                enemycolors[enemyIndex] = 3
            else:
                enemy[enemyIndex].shape(fuzzm)
                enemycolors[enemyIndex] = 4
        if stage == 3:
            colorchooser = random.randint(2, 6)
            if colorchooser == 5:
                enemy[enemyIndex].shape(bubc)
                enemycolors[enemyIndex] = 1
            elif colorchooser == 4:
                enemy[enemyIndex].shape(bubr)
                enemycolors[enemyIndex] = 2
            elif colorchooser == 3:
                enemy[enemyIndex].shape(bubg)
                enemycolors[enemyIndex] = 3
            else:
                enemy[enemyIndex].shape(bubm)
                enemycolors[enemyIndex] = 4
        if stage == 4:
            colorchooser = random.randint(2, 6)
            if colorchooser == 5:
                enemy[enemyIndex].shape(birdcf)
                enemycolors[enemyIndex] = 1
            elif colorchooser == 4:
                enemy[enemyIndex].shape(birdrf)
                enemycolors[enemyIndex] = 2
            elif colorchooser == 3:
                enemy[enemyIndex].shape(birdgf)
                enemycolors[enemyIndex] = 3
            else:
                enemy[enemyIndex].shape(birdmf)
                enemycolors[enemyIndex] = 4
        if stage == 5:
            colorchooser = random.randint(2, 6)
            if colorchooser == 5:
                enemy[enemyIndex].shape(ufoc)
                enemycolors[enemyIndex] = 1
            elif colorchooser == 4:
                enemy[enemyIndex].shape(ufor)
                enemycolors[enemyIndex] = 2
            elif colorchooser == 3:
                enemy[enemyIndex].shape(ufog)
                enemycolors[enemyIndex] = 3
            else:
                enemy[enemyIndex].shape(ufom)
                enemycolors[enemyIndex] = 4
def bonusactivate():
    global bonusstate, points
    bonusindicator = random.randint(0,1000)
    if bonusindicator == 100 or bonusstate != 0:
        if bonusstate == 0:
            bonusdecider = random.randint(1,6)
            spawnpoint = random.randint(2, 5)
        else:
            bonusdecider = 14
            spawnpoint = 14
        if bonusdecider == 1 or bonusstate == 1:
            bonus.shape(jewel)
            bonusstate = 1
        if bonusdecider == 2 or bonusstate == 2:
            bonus.shape(gel)
            bonusstate = 2
        if bonusdecider == 3 or bonusstate == 3:
            bonus.shape(molec)
            bonusstate = 3
        if bonusdecider == 4 or bonusstate == 4:
            bonus.shape(gold)
            bonusstate = 4
        if bonusdecider == 5 or bonusstate == 5:
            bonus.shape(rad)
            bonusstate = 5
        if spawnpoint == 2:
            bonus.goto(-195, 330)
        if spawnpoint == 3:
            bonus.goto(-100, 330)
        if spawnpoint == 4:
            bonus.goto(0, 330)
        if spawnpoint == 5:
            bonus.goto(200, 330)
        bonus.showturtle()
        dist = ((miner.xcor() - bonus.xcor()) ** 2 + (miner.ycor() - bonus.ycor()) ** 2) ** 0.5
        if dist <= 35:
            bonus.hideturtle()
            if bonusstate == 1:
                points += 300
                bonusstate = 0
            if bonusstate == 2:
                points += 100
                bonusstate = 0
            if bonusstate == 3:
                points += 150
                bonusstate = 0
            if bonusstate == 4:
                points += 250
                bonusstate = 0
            if bonusstate == 5:
                points += 200
                bonusstate = 0
def enemyanimate(j):
    global animateframes, enemycolors, enemy
    if stage == 1:
        animateframes += 1
        if animateframes == 10:
            if enemycolors[j] == 1:
                enemy[j].shape(rockf2c)
            if enemycolors[j] == 2:
                enemy[j].shape(rockf2r)
            if enemycolors[j] == 3:
                enemy[j].shape(rockf2g)
            if enemycolors[j] == 4:
                enemy[j].shape(rockf2m)
            if enemycolors[j] == 5:
                enemy[j].shape(rockf2cl)
            if enemycolors[j] == 6:
                enemy[j].shape(rockf2rl)
            if enemycolors[j] == 7:
                enemy[j].shape(rockf2gl)
            if enemycolors[j] == 8:
                enemy[j].shape(rockf2ml)
        if animateframes == 20:
            if enemycolors[j] == 1:
                enemy[j].shape(rockf1c)
            if enemycolors[j] == 2:
                enemy[j].shape(rockf1r)
            if enemycolors[j] == 3:
                enemy[j].shape(rockf1g)
            if enemycolors[j] == 4:
                enemy[j].shape(rockf1m)
            if enemycolors[j] == 5:
                enemy[j].shape(rockf1cl)
            if enemycolors[j] == 6:
                enemy[j].shape(rockf1rl)
            if enemycolors[j] == 7:
                enemy[j].shape(rockf1gl)
            if enemycolors[j] == 8:
                enemy[j].shape(rockf1ml)
            animateframes = 0
def spawnbullet():
    global bullets, bulletindex, bulletfollowindex, bulletdist
    if bulletindex != 6:
        bulletindex += 1
        bulletfollowindex += 1
        bullets.append(turtle.Turtle())
        bulletfollow.append(turtle.Turtle())
        bullets[bulletindex].speed(0)
        bulletfollow[bulletfollowindex].speed(0)
        bullets[bulletindex].turtlesize(0.0001, 0.5)
        bullets[bulletindex].shape('square')
        bulletfollow[bulletfollowindex].turtlesize(0.3,0.5)
        bullets[bulletindex].hideturtle()
        bullets[bulletindex].pensize(3)
        bulletfollow[bulletfollowindex].pensize(3)
        bulletfollow[bulletfollowindex].hideturtle()
        bulletstates.append(0)
        bulletdist.append(0)
        laserout.append(0.0000001)
        shootime.append(0)
        bulletfollowstates.append(0)
    return
#0.6 pixels per tick. Depending what 'end' of the turtle the size will increase from the speed of the laser as its
#leaving the gun will be either 0.6, 0.3, or 0 respectively if firing left.
# if speed is 0, or 0.6 the laser will grow 0.6 pixels per tick
def shoot():
    global shootflag, bulletstates, counterres, newbulletTime, facing
    counterres = 0
    shootflag = True
    for d in range(0,len(bulletstates),1):
        if bulletstates[d] == 0 and counterres == 0:
            bulletstates[d] = 2
            color = randcolor()
            bullets[d].pencolor(color)
            bullets[d].color(color)
            bullets[d].showturtle()
            if facing == -10:
                bullets[d].setheading(180)
                bulletfollow[d].setheading(180)
            if facing == 10:
                bullets[d].setheading(0)
                bulletfollow[d].setheading(0)
            counterres = 1
    counterres = 0
    spawnbullet()
    return
def bulletmove(k):
    global newbulletTime, bulletdist, laserout, facing, shootime, multi
    if bulletstates[k] == 3 or bulletstates[k] == 4 or bulletstates[k] == 2:
        if bullets[k].heading == 180:
            lefty = -1
        else:
            lefty = 1
        bulletfollow[k].hideturtle()
        bulletfollow[k].pendown()
        if bulletstates[k] == 2:
            if bullets[k].heading() == 0:
                laserout[k] += 0.06
                bullets[k].forward(0.6)
            elif bullets[k].heading() == 180:
                laserout[k] += 0.06
                bullets[k].forward(0.6)
            bullets[k].turtlesize(0.1,laserout[k])
        elif bulletstates[k] == 3:
            bullets[k].forward(0.6)
            bulletdist[k] += 1
            if bulletdist[k] == 700:
                bulletfollowstates[k] = 3
        elif bulletstates[k] == 4:
            if bullets[k].heading() == 0:
                bullets[k].forward(-0.6)
                laserout[k] -= 0.06
            elif bullets[k].heading() == 180:
                bullets[k].forward(0.6)
                laserout[k] += 0.06
            bullets[k].turtlesize(0.1,laserout[k])
            if laserout[k] <= -0.06 or laserout[k] >= 0.06:
                laserout[k] = 0.000000124
        if bulletfollowstates[k] == 3:
            bulletfollow[k].forward(1.2)
        if laserout[k] >= 1 and bulletstates[k] == 2:
            bulletstates[k] = 3
        if shootime[k] == 1 or shootime[k] == 20*multi:
            randlaz = random.randint(1,4)
            print(randlaz)
            if randlaz == 3:
                bullets[k].pendown()
            else:
                bullets[k].penup()
            multi += 1
        shootime[k] += 1
        if shootime[k] == 700 or bulletstates[k] == 4:
            bulletstates[k] = 4
        if laserout[k] == 0.000000124:
            bullets[k].clear()
            bulletfollow[k].clear()
            laserout[k] = 0.0000001
            bullets[k].turtlesize(0.00000000001,0.5)
            bulletstates[k] = 0
            bulletfollowstates[k] = 0
            bulletdist[k] = 0
            shootime[k] = 0
            multi = 0
    if bulletstates[k] == 0 and bulletfollowstates[k] == 0:
        bullets[k].penup()
        bullets[k].hideturtle()
        bulletfollow[k].hideturtle()
        bulletfollow[k].penup()
        bullets[k].goto(miner.xcor() + facing,miner.ycor())
        bulletfollow[k].goto(miner.xcor(),miner.ycor())
def bulletcollide(t1,r1,b1,sem1,sem2,offset,offset2,k):
    global move1, lives, lift, lift2
    global move2
    global move3
    global move4
    global bumper
    #b1 = a brick, sem1 = its semilength
    brickBottom = b1.ycor() - sem1 - offset
    brickTop = b1.ycor() + sem1 + offset
    brickLeft = b1.xcor() - sem2 - offset2
    brickRight = b1.xcor() + sem2 + offset2
    enemyBottom = t1.ycor() - r1
    enemyTop = t1.ycor() + r1
    enemyRight = t1.xcor() + r1
    enemyLeft = t1.xcor() - r1
    #setect a top collision
    if enemyBottom < brickTop and enemyLeft < brickRight and enemyRight > brickLeft and enemyTop > brickBottom:
        bulletstates[k] = 4
def enemykill(t1,r1,b1,sem1,sem2,offset,offset2,k,j):
    global move1, lives, lift, lift2, bulletstates, enemystates, points
    global move2
    global move3
    global move4
    global bumper
    #b1 = a brick, sem1 = its semilength
    brickBottom = b1.ycor() - sem1 - offset
    brickTop = b1.ycor() + sem1 + offset
    brickLeft = b1.xcor() - sem2 - offset2
    brickRight = b1.xcor() + sem2 + offset2
    enemyBottom = t1.ycor() - r1
    enemyTop = t1.ycor() + r1
    enemyRight = t1.xcor() + r1
    enemyLeft = t1.xcor() - r1
    #setect a top collision
    if enemyBottom < brickTop and enemyLeft < brickRight and enemyRight > brickLeft and enemyTop > brickBottom:
        bulletstates[k] = 4
        enemystates[j] = 3
        points += 25
def aim(k):
    global facing
    if facing == -30 and bulletstates[k] == 2:
        bullets[k].setheading(180)
        bulletfollow[k].setheading(180)
    if facing == -30 and bulletstates[k] == 2:
        bullets[k].setheading(0)
        bulletfollow[k].setheading(0)
def randcolor():
    colorrand = random.randint(0,2)
    if colorrand == 0:
        randomcolor = "#FF00FF"
    if colorrand == 1:
        randomcolor = "#FFFFFF"
    if colorrand == 2:
        randomcolor = "#00FFFF"
    return randomcolor
def enemymovement(j):
    global stage, enemy, enemystates
    if enemystates[j] == 0:
        if stage == 1:
            enemy[j].forward(1.7)
        if stage == 2:
            enemy[j].forward(1.8)
        if stage == 3:
            if enemy[j].xcor() <= -300 and enemyaltstates[j] == 0:
                enemyaltstates[j] = 1
            elif enemy[j].xcor() >= 300 and enemyaltstates[j] == 0:
                enemyaltstates[j] = 2
            elif enemyaltstates[j] == 1:
                vector = random.randint(1, 100)
                if miner.ycor() >= enemy[j].ycor() and vector == 3:
                    enemy[j].setheading(45)
                if miner.ycor() == enemy[j].ycor() and vector == 3:
                    enemy[j].setheading(0)
                if miner.ycor() <= enemy[j].ycor() and vector == 3:
                    enemy[j].setheading(-45)
            elif enemyaltstates[j] == 2:
                vector = random.randint(1, 100)
                if miner.ycor() >= enemy[j].ycor() and vector == 3:
                    enemy[j].setheading(135)
                if miner.ycor() == enemy[j].ycor() and vector == 3:
                    enemy[j].setheading(180)
                if miner.ycor() <= enemy[j].ycor() and vector == 3:
                    enemy[j].setheading(225)
            enemy[j].forward(1.2)
        if stage == 4:
            if enemy[j].xcor() <= -300:
                enemy[j].goto(-300, enemy[j].ycor())
                enemyaltstates[j] += 1
                goattack = random.randint(1, 800)
                if enemyaltstates[j] <= 500:
                    enemy[j].goto(enemy[j].xcor(), enemy[j].ycor() + 0.3)
                elif enemyaltstates[j] <= 1000:
                    enemy[j].goto(enemy[j].xcor(), enemy[j].ycor() - 0.3)
                else:
                    enemyaltstates[j] = 0
                if goattack == 800:
                    enemy[j].goto(enemy[j].xcor() + 1, enemy[j].ycor())
                    enemyaltstates[j] = 4000
            elif enemy[j].xcor() >= 300:
                enemy[j].goto(300, enemy[j].ycor())
                enemyaltstates[j] += 1
                goattack = random.randint(1, 800)
                if enemyaltstates[j] <= 100:
                    enemy[j].goto(enemy[j].xcor(), enemy[j].ycor() + 0.6)
                elif enemyaltstates[j] <= 200:
                    enemy[j].goto(enemy[j].xcor(), enemy[j].ycor() - 0.6)
                else:
                    enemyaltstates[j] = 0
                if goattack == 800:
                    enemy[j].goto(enemy[j].xcor() - 1, enemy[j].ycor())
                    enemyaltstates[j] = -4000
            else:
                ang = enemy[j].towards(enemy[j].xcor(), miner.ycor())
                enemy[j].setheading(ang)
                enemy[j].forward(0.7)
                if enemyaltstates[j] == -4000:
                    enemy[j].goto(enemy[j].xcor() - 1.5, enemy[j].ycor())
                if enemyaltstates[j] == 4000:
                    enemy[j].goto(enemy[j].xcor() + 1.5, enemy[j].ycor())
        if stage == 5:
            dist = ((miner.xcor() - enemy[j].xcor()) ** 2 + (miner.ycor() - enemy[j].ycor()) ** 2) ** 0.5
            ang = enemy[j].towards(miner.xcor(), miner.ycor())
            if dist <= 300:
                enemy[j].setheading(ang)
                enemy[j].forward(1.5)
            else:
                if enemy[j].ycor() <= miner.ycor():
                    enemy[j].goto(enemy[j].xcor() + 1.5, enemy[j].ycor() + 0.6)
                if enemy[j].ycor() >= miner.ycor():
                    enemy[j].goto(enemy[j].xcor() + 1.5, enemy[j].ycor() - 0.6)

            sporatic = random.randint(-3, 3)
            enemy[j].goto(enemy[j].xcor() + (sporatic / 2), enemy[j].ycor() + sporatic)
    return
def hitground(j):
    global enemy, enemystates
    if enemy[j].ycor() <= -190 and stage == 1:
        enemystates[j] = 3
    elif stage == 2 or stage == 3:
        if enemy[j].ycor() <= -190:
            enemy[j].setheading(360 - enemy[j].heading())
        elif enemy[j].ycor() >= 315:
            enemy[j].setheading(360 - enemy[j].heading())
    return
def destroy(j):
    global enemy, enemystates, destroyed, spawnstopper, speedupper
    if enemystates[j] == 3 or enemystates[j] == 14:
        enemy[j].goto(1000,1000)
        enemy[j].hideturtle()
        enemyproperties(j)
        enemystates[j] = 0
        enemyaltstates[j] = 0
        enemy[j].showturtle()
        spawnstopper = 1
    return
def playercollide(t1,r1,b1,sem1,sem2,offset,offset2,k):
    global move1, lives, lift, lift2, enemystates, isDed, resetmap
    global move2
    global move3
    global move4
    global bumper
    #b1 = a brick, sem1 = its semilength
    brickBottom = b1.ycor() - sem1 - offset
    brickTop = b1.ycor() + sem1 + offset
    brickLeft = b1.xcor() - sem2 - offset2
    brickRight = b1.xcor() + sem2 + offset2
    enemyBottom = t1.ycor() - r1
    enemyTop = t1.ycor() + r1
    enemyRight = t1.xcor() + r1
    enemyLeft = t1.xcor() - r1
    #setect a top collision
    if enemyBottom < brickTop and enemyLeft < brickRight and enemyRight > brickLeft and enemyTop > brickBottom:
        if int(lives) == 0:
            miner.hideturtle()
            isDed = True
        elif miner.ycor() >= -3000:
            lives = lives - 1
            ls.clear()
            if int(lives) == 0:
                ls2.hideturtle()
            else:
                ls.write(lives, "", "center", ("fixedsys", 15, "normal"))
            resetmap = True
            if pickupblock == 0 and lift == 1:
                lift = 0
            if pickupblock == 1 and lift2 == 1:
                lift2 = 0
            for l in range(0,len(fuel),1):
                if fuelstates[l] == 1:
                    fuelstates[l] = 0
            miner.goto(0, -175)

        return
def brickcrash(j,r1,b1,sem1,sem2,offset,smabig):
    global move1, enemy, enemystates
    global move2
    global move3
    global move4
    global bumper
    #b1 = a brick, sem1 = its semilength
    brickBottom = b1.ycor() - sem1 - offset
    brickTop = b1.ycor() + sem1 + offset
    brickLeft = b1.xcor() - sem2 - offset
    brickRight = b1.xcor() + sem2 + offset
    rockBottom = enemy[j].ycor() - r1
    rockTop = enemy[j].ycor() + r1
    rockRight = enemy[j].xcor() + r1
    rockLeft = enemy[j].xcor() - r1
    #setect a top collision
    if rockBottom < brickTop and rockLeft < brickRight and rockRight > brickLeft and rockTop > brickBottom:
        ang = enemy[j].towards(b1.xcor(), b1.ycor())
        if smabig == 0:
            if ang <= 9.462 or ang >= 350.538:
                enemystates[j] = 3
            elif ang <= 170.538 and ang >= 9.462:
                enemystates[j] = 3
            elif ang <= 189.462 and ang >= 170.538:
                enemystates[j] = 3
            else:
                enemystates[j] = 3
                blockcheck = False
        else:
            if ang <= 14.036 or ang >= 345.964:
                enemystates[j] = 3
            elif ang <= 165.964 and ang >= 14.036:
                enemystates[j] = 3
            elif ang <= 194.036 and ang >= 165.964:
                enemystates[j] = 3
            else:
                enemystates[j] = 3
                blockcheck = False
        return
def fwdCalc(visTurts):
    global speedScale
    #Sp =  0.0255683816 + 0.311678 * math.log(visTurts + 1)
    if visTurts == 1:
        Sp = 0.3
    elif visTurts == 2:
        Sp = 0.3
    elif visTurts == 3:
        Sp = 0.3
    else:
        Sp = (0.01 + 0.311678 * math.log(visTurts + 1))
    Sp = 1 * Sp
    return Sp
def stagecompletion(t1,t2):
    global stagecomp, fuel, fuelstates, fuelIndex, lift, lift2, pickupblock,fuelspawn,falling,groundcheck,colorcounter, landing, gravycor, moveDist, stage, enemystates, enemy, enemyIndex, enemyaltstates, pickupblock, lives
    if stagecomp == 1:
        dist = ((t1.xcor() - t2.xcor()) ** 2 + (t1.ycor() - t2.ycor()) ** 2) ** 0.5
        if rockets1p1.ycor() >= 330 or landing == True:
            miner.goto(0, -600)
            for p in range(0,len(enemy),1):
                enemy[p].hideturtle()
            for i in range(0,len(fuel),1):
                fuel[i].hideturtle()
            for o in range(0,len(bullets),1):
                bullets[o].hideturtle()
            rockets1p1.shape(s1p1w)
            rockets1p2.shape(s1p2w)
            rockets2p1.shape(s2p1w)
            rockets2p2.shape(s2p2w)
            rockets3p1.shape(s3p1w)
            rockets3p2.shape(s3p2w)
            if stage == 4:
                    pickupblock = 0
                    fuelspawn = 0
                    rockets1p1.goto(100, -190)
                    rockets1p2.goto(100, -175)
                    rockets2p1.goto(0, 25)
                    rockets2p2.goto(0, 40)
                    rockets3p1.goto(-195, 85)
                    rockets3p2.goto(-195, 100)
                    lives += 1
                    ls.clear()
                    ls.write(lives, "", "center", ("fixedsys", 15, "normal"))
                    lift2 = 0
                    lift = 0
            else:
                rockets1p1.goto(rockets1p1.xcor(), rockets1p1.ycor() - (0.2*fwdAmnt))
                rockets1p2.goto(rockets1p2.xcor(), rockets1p1.ycor() + 15)
                rockets2p1.goto(rockets2p1.xcor(), rockets1p1.ycor() + 30)
                rockets2p2.goto(rockets2p2.xcor(), rockets1p1.ycor() + 45)
                rockets3p1.goto(rockets3p1.xcor(), rockets1p1.ycor() + 60)
                rockets3p2.goto(rockets3p2.xcor(), rockets1p1.ycor() + 75)
                pickupblock = 1
                fuelspawn = 1
                lift2 = 2
                lift = 2
                landing = True
            if rockets1p1.ycor() <= -190 or stage == 4:
                if stage != 4:
                    rockets1p1.goto(100,-190)
                    rockets1p2.goto(100,-175)
                    rockets2p1.goto(100,-160)
                    rockets2p2.goto(100, -145)
                    rockets3p1.goto(100, -130)
                    rockets3p2.goto(100, -115)
                stage += 1
                if stage == 6:
                    stage = 1
                time.sleep(2)
                rockets1p1.color('white')
                rockets1p2.color('white')
                rockets2p1.color('white')
                rockets2p2.color('white')
                rockets3p1.color('white')
                rockets3p2.color('white')
                landing = False
                fuel = []
                fuelstates = []
                fuelIndex = -1
                enemyIndex = -1
                enemystates = []
                enemyaltstates = []
                enemy = []
                startgame = False
                bumper = 3
                lift3 = 0
                stagecomp = 0
                alternator = 1
                falling = True
                groundcheck = True
                shapesize = 3
                gravycor = 0
                updatelives = 3
                nostart = True
                moveDist = 0
                relocate = True
                isDed = False
                pts = 0
                colorcounter = 0
                updatepts = 0
                miner.goto(0,-175)
                miner.showturtle()
        if dist <= 10 or miner.isvisible() == False:
            miner.goto(0,-600)
            miner.hideturtle()
            rockets1p1.goto(rockets1p1.xcor(),rockets1p1.ycor() + (0.1*fwdAmnt))
            rockets1p2.goto(rockets1p2.xcor(),rockets1p1.ycor() + 15)
            rockets2p1.goto(rockets2p1.xcor(),rockets1p1.ycor() + 30)
            rockets2p2.goto(rockets2p2.xcor(),rockets1p1.ycor() + 45)
            rockets3p1.goto(rockets3p1.xcor(),rockets1p1.ycor() + 60)
            rockets3p2.goto(rockets3p2.xcor(),rockets1p1.ycor() + 75)
            stagecomp = 1

def death(t1, r1, m1):
    global isDed
    global lives
    dist = ((t1.xcor() - m1.xcor()) ** 2 + (t1.ycor() - m1.ycor()) ** 2) ** 0.5
    if dist < (r1) and int(lives) == 0:
        miner.hideturtle()
        isDed = True
    elif dist < (r1):
        lives = lives - 1
        miner.goto(0,0)
    return
def collectathon(t1, r1, m1):
    global pts
    dist = ((t1.xcor() - m1.xcor()) ** 2 + (t1.ycor() - m1.ycor()) ** 2) ** 0.5
    if dist < (r1):
        pts = int(pts) +1
    return

def gameover():
    global isDed, startgame, stage, enemy, fuel, bullets, highscore, highestscore, fuelstates, enemyIndex,fuelIndex,enemystates,enemyaltstates, lives, frameovergameover, nostart
    if isDed == True:
        startgame = False
        brick1.hideturtle()
        brick2.hideturtle()
        brick3.hideturtle()
        rockets1p1.hideturtle()
        rockets1p2.hideturtle()
        rockets2p1.hideturtle()
        rockets2p2.hideturtle()
        rockets3p1.hideturtle()
        rockets3p2.hideturtle()
        bonus.hideturtle()
        floor.hideturtle()
        for k in range(0,len(enemy),1):
            enemy[k].hideturtle()
        for l in range(0, len(fuel), 1):
            fuel[l].hideturtle()
        for j in range(0,len(bullets),1):
            bullets[j].hideturtle()
            bullets[j].clear()
        instructions.penup()
        instructions.goto(0, -20)
        instructions.pendown()
        instructions.write("GAME  OVER  PLAYER  1", "", "center", ("fixedsys", 17, "normal"))
        if points > highscore:
            highscore = points
            pointstr = str(points)
            if points > 9:
                highestscore = '0000' + pointstr
            if points > 99:
                highestscore = '000' + pointstr
            if points > 999:
                highestscore = '00' + pointstr
            if points > 9999:
                highestscore = '0' + pointstr
            if points > 99999:
                highestscore = pointstr
            Hiscore.clear()
            Hiscore.write(highestscore, "", "center", ("fixedsys", 15, "normal"))
        stage = 1
        pickupblock = 0
        fuelspawn = 0
        rockets1p1.goto(100, -190)
        rockets1p2.goto(100, -175)
        rockets2p1.goto(0, 25)
        rockets2p2.goto(0, 40)
        rockets3p1.goto(-195, 85)
        rockets3p2.goto(-195, 100)
        bonus.goto(0, 400)
        lift2 = 0
        lift = 0
        rockets1p1.color('white')
        rockets1p2.color('white')
        rockets2p1.color('white')
        rockets2p2.color('white')
        rockets3p1.color('white')
        rockets3p2.color('white')
        landing = False
        fuel = []
        fuelstates = []
        fuelIndex = -1
        enemyIndex = -1
        enemystates = []
        enemyaltstates = []
        enemy = []
        startgame = False
        bumper = 3
        lift3 = 0
        stagecomp = 0
        alternator = 1
        lives = 4
        falling = True
        groundcheck = True
        shapesize = 3
        gravycor = 0
        updatelives = 3
        nostart = True
        moveDist = 0
        relocate = True
        bonus.goto(0, 400)
        pts = 0
        colorcounter = 0
        updatepts = 0
        miner.goto(0, -175)
        frameovergameover += 1
        print(frameovergameover)
        if frameovergameover == 400:
            instructions.clear()
            isDed = False
            frameovergameover = 0
            instructions.pencolor("white")
            instructions.penup()
            instructions.goto(0, 150)
            instructions.pendown()
            instructions.write("JETPAC  GAME  SELECTION", "", "center", ("fixedsys", 17, "normal"))
            instructions.penup()
            instructions.goto(-100, 90)
            instructions.pendown()
            instructions.write("1    1  PLAYER GAME", "", "left", ("fixedsys", 17, "normal"))
            instructions2 = turtle.Turtle()
            instructions2.hideturtle()
            instructions2.pencolor('white')
            instructions.penup()
            instructions.goto(-100, 30)
            instructions.pendown()
            instructions.write("2    DEFAULT  LASER", "", "left", ("fixedsys", 17, "normal"))
            instructions2.penup()
            instructions2.goto(-100, -30)
            instructions2.pendown()
            instructions2.write("3    WASD CONTROLS", "", "left", ("fixedsys", 17, "normal"))
            instructions.penup()
            instructions.goto(-22, -180)
            instructions.pendown()
            instructions.write("5    START  GAME", "", "center", ("fixedsys", 17, "normal"))
            instructions.penup()
            instructions.goto(0, -250)
            instructions.pendown()
            instructions.write("2017 RARE LTD. ALL RIGHTS RESERVED ", "", "center", ("fixedsys", 17, "normal"))




def flashingrocket():
    global newTime, oldtime, alternator
    alternator += 1
    if alternator == 200:
        rockets1p1.shape(s1p1m)
        rockets1p2.shape(s1p2m)
        rockets2p1.shape(s2p1m)
        rockets2p2.shape(s2p2m)
        rockets3p1.shape(s3p1m)
        rockets3p2.shape(s3p2m)
        alternator = 0
    if alternator == 100:
        rockets1p1.shape(s1p1w)
        rockets1p2.shape(s1p2w)
        rockets2p1.shape(s2p1w)
        rockets2p2.shape(s2p2w)
        rockets3p1.shape(s3p1w)
        rockets3p2.shape(s3p2w)
def pointupdate():
    global points, scorep1, pointsche
    if points != pointsche:
        pointstr = str(points)
        if points > 9:
            scorep1 = '0000' + pointstr
            pointsche = points
        if points > 99:
            scorep1 = '000' + pointstr
            pointsche = points
        if points > 999:
            scorep1 = '00' + pointstr
            pointsche = points
        if points > 9999:
            scorep1 = '0' + pointstr
            pointsche = points
        if points > 99999:
            scorep1 = pointstr
            pointsche = points
        p1s.clear()
        p1s.write(scorep1, "", "center", ("fixedsys", 15, "normal"))
def reset():
    global resetmap, enemy, enemyaltstates, enemystates, enemyIndex
    if resetmap == True:
        for p in range(0, len(enemy), 1):
            enemy[p].hideturtle()
        enemy = []
        enemystates = []
        enemyaltstates = []
        enemyIndex = -1
        resetmap = False

# ---------------main body---------------------
mywindow.onkeypress(iswpressed, "w")
mywindow.onkeyrelease(iswreleased, "w")
mywindow.onkeypress(isapressed, "a")
mywindow.onkeyrelease(isareleased, "a")
mywindow.onkeypress(isdpressed, "d")
mywindow.onkeyrelease(isdreleased, "d")
mywindow.onkeyrelease(noW, "w")
mywindow.onkeypress(isspacepressed, "space")
mywindow.onkeyrelease(isspacereleased, "space")
mywindow.onkeypress(isbpressed, "b")
mywindow.onkeyrelease(isbreleased, "b")
mywindow.onkeypress(isnpressed, "n")
mywindow.onkeyrelease(isnreleased, "n")
mywindow.onkeypress(isspressed, "s")
mywindow.onkeyrelease(issreleased, "s")
mywindow.onkey(controlswitch, "3")
mywindow.onkey(start, "5")
mywindow.listen()
mywindow.onkey(leave, '6')

shootflag= False
quitFlag = False
mywindow.tracer(0,0)


fuel = []
fuelstates = []
fuelIndex = -1
enemy = []
enemycolors = []
enemystates = []
enemyaltstates = []
enemyIndex = -1
bullets = []
bulletstates = []
bulletindex = -1
bulletfollow = []
bulletfollowstates = []
bulletfollowindex = -1
bulletdist = []
laserout = []
shootime = []

startTime = time.clock()
print(time.clock())
newTime = int(startTime)
newbulletTime = round(startTime,2)

while quitFlag == False:
    oldTime = newTime
    oldbulletTime = newbulletTime
    newTime = int(time.clock() - startTime)
    newbulletTime = round(time.clock() - startTime, 1)
    fwdAmnt = fwdCalc(sum(fuelstates+enemystates))  # getting a new forward amount based on visible turtles
    fwdAmnt = 2
    #--------------------------
    if miner.ycor() != -600:
        gravy(miner,25,1)
    edgewrap(miner)
    left()
    right()
    walkcycle()
    blockcheck = 1
    automaticloop()
    if miner.ycor() != -600:
        gameover()
    if len(enemy) < 8 and startgame == True:
        enemyspawn(1,0)
    if len(enemy) < 6 and startgame == True:
        spawnbullet()
    bonusactivate()
    if bonusstate != 0:
        gravy(bonus,10,0)
        brickcollide(bonus, 0.75, brick1, brick1SemiLength, brick1SemiLength2, 7, 0, 0, 0)
        brickcollide(bonus, 0, brick2, brick1SemiLength, brick2SemiLength2, 7, 0, 1, 0)
        brickcollide(bonus, 0, brick3, brick1SemiLength, brick2SemiLength2, 7, 0, 1, 0)
    rocketglue(rockets2p2,rockets2p1)
    rocketglue(rockets3p2,rockets3p1)
    if stagecomp != 1:
        gravy(rockets2p1,10,0)
        gravy(rockets3p1,10,0)
        partlifters1(miner,rockets2p1,-160,0)
        partlifters2(miner, rockets3p1, -130, 1)

    for k in range(0,len(enemy),1):
        enemymovement(k)
        edgewrap(enemy[k])
        if stage == 1:
            brickcrash(k,0,brick1,brick1SemiLength,brick1SemiLength2,5,1)
            brickcrash(k,0, brick2, brick1SemiLength, brick2SemiLength2, 5, 0)
            brickcrash(k,0, brick3, brick1SemiLength, brick2SemiLength2, 5, 0)
        else:
            brickbounce(enemy[k], 5, brick1, brick1SemiLength, brick1SemiLength2, 0)
            brickbounce(enemy[k], 5, brick2, brick1SemiLength, brick2SemiLength2, 1)
            brickbounce(enemy[k], 5, brick3, brick1SemiLength, brick2SemiLength2, 1)
        hitground(k)
        destroy(k)
        for b in range(0,len(bullets),1):
            bulletmove(b)
            edgewrap(bullets[b])
            edgewrap(bulletfollow[b])
            bulletcollide(bullets[b],0,brick1,brick1SemiLength,brick1SemiLength2,0,0,b)
            bulletcollide(bullets[b], 0, brick2, brick1SemiLength, brick2SemiLength2, 0, 0, b)
            bulletcollide(bullets[b], 0, brick3, brick1SemiLength, brick2SemiLength2, 0, 0, b)
            aim(b)
            enemykill(enemy[k],9,bullets[b],laserout[b],0.1,0,0,b,k)
        if enemystates[k] == 3:
            if newTime - oldTime != 1:
                enemyspawn(0,k)
                spawnstopper = 0
                enemystates[k] = 14
        if miner.ycor() != -600:
            playercollide(enemy[k], 23, miner, 1.45, 2.5, 0, 0, k)
    brickcollide(miner,0,brick1,brick1SemiLength,brick1SemiLength2,23,10,0,1)
    brickcollide(miner, 0, brick2, brick1SemiLength, brick2SemiLength2,23,10,1,1)
    brickcollide(miner, 0, brick3, brick1SemiLength, brick2SemiLength2,25,10,1,1)
    brickcollide(rockets2p1, 0.75, brick1, brick1SemiLength, brick1SemiLength2,7,0,0,0)
    brickcollide(rockets2p1, 0, brick2, brick1SemiLength, brick2SemiLength2,7,0,1,0)
    brickcollide(rockets2p1, 0, brick3, brick1SemiLength, brick2SemiLength2,7,0,1,0)
    brickcollide(rockets3p1, 0.75, brick1, brick1SemiLength, brick1SemiLength2,7,0,0,0)
    brickcollide(rockets3p1, 0, brick2, brick1SemiLength, brick2SemiLength2,7,0,1,0)
    brickcollide(rockets3p1, 0, brick3, brick1SemiLength, brick2SemiLength2,7,0,1,0)
    spawnfuel()
    pointupdate()
    if fuelspawn == 2:
        for j in range(0,len(fuel),1):
            gravy(fuel[j], 10,0)
            brickcollide(fuel[j], 0, brick1, brick1SemiLength, brick1SemiLength2, 7,0, 0,0)
            brickcollide(fuel[j], 0, brick2, brick1SemiLength, brick2SemiLength2, 7,0, 1,0)
            brickcollide(fuel[j], 0, brick3, brick1SemiLength, brick2SemiLength2, 7,0, 1,0)
            if stagecomp != 1:
                partlifterf(miner,fuel[j],j)
    if stagecomp == 1:
        flashingrocket()
        stagecomp = 1
    reset()
    stagecompletion(miner,rockets1p1)
    stagecompletion(miner,rockets1p2)
    stagecompletion(miner,rockets3p2)
    stagecompletion(miner,rockets2p2)
    titlescreen.hideturtle()
    mywindow.update()
    if startgame == True and delay == 1:
        time.sleep(3)
        delay = 0




mywindow.bye()