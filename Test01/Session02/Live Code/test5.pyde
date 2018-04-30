from particle import Particle

particles = []

dt = 0.1
gx = 0
gy = 10.0

def setup():
    size(400,400)
    for k in range(200):
        p = Particle(random(width), random(height), 10.0, 1.0)
        particles.append(p)

def draw():
    background(234,234,234)
    global gx,gy
    
    if keyPressed and keyCode == UP:
        gy = -10.0
        gx = 0

    if keyPressed and keyCode == DOWN:
        gy = 10.0
        gx = 0
        
    if keyPressed and keyCode == LEFT:
        gy = 0
        gx = -10.0

    if keyPressed and keyCode == RIGHT:
        gy = 0
        gx = 10.0
    
    if mousePressed:
        for p in particles:
            l = dist(mouseX, mouseY, p.x, p.y)
            if l < 30:
                force = -10.0
                p.applyForce(force*(pmouseX - mouseX), force*(pmouseY - mouseY))
    
    for p in particles:
        for p2 in particles:
            p.interact(p2)
    
    
    for p in particles:
        p.applyForce(gx, gy)
        p.update(dt)
        p.checkWalls(dt)
        p.show()
        
    saveFrame("movie/session2-####.png")
    