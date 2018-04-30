from particle import Particle

particles = []
dt = 0.1

def setup():
    size(400,400)    
    for k in range(400):
    
        p = Particle( random(width), random(height), 6, 1.0) 
        p.vx = random(-5,5)
        particles.append(p)

    
def draw():
    background(255,255,255)
    
    if mousePressed:
        for p in particles:
            l = dist(mouseX, mouseY, p.x, p.y)
            if l < 30:
                f = 40.0
                p.applyForce(f*(mouseX - pmouseX), f*(mouseY - pmouseY))
    
    for p1 in particles:
        for p2 in particles:
            p1.interact(p2, dt)
    
    for p in particles:
        p.applyForce(0, p.mass*10.0)
       # p.applyForce(-p.vx*dt*0.1, -p.vy*dt*0.1)
        p.update(dt)
        p.show()
    
    #saveFrame("movie/test-####.png")
    