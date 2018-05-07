from particle import Particle

particles = []
dt = 0.01

col = 41
row = 30
spring = 9.0
def setup():
    size(400,400)    

    for x in range(col):
        for y in range(row):
            
            p = Particle( 20 + x*spring, 20 + y*spring, 3.0, 0.01) 
            particles.append(p)

    

def draw():
    background(234)
    
    if mousePressed and mouseButton == LEFT:
        for p in particles:
            l = dist(mouseX, mouseY, p.x, p.y)
            if l < 10.0:
                p.applyForce(500000*(mouseX - pmouseX), 500000*(mouseY - pmouseY))

    for x in range(col):
        for y in range(row):
            i = y + x*row
            i1 = y-1 + x*row
            i2 = y + (x+1)*row
            i3 = y+1 + x*row
            i4 = y + (x-1)*row
            
            if y-1 >= 0:
                particles[i].interact(particles[i1], spring) 
            if x+1 < col:
                particles[i].interact(particles[i2], spring)
            if y+1 < row:
                particles[i].interact(particles[i3], spring)
            if x-1 >= 0:
                particles[i].interact(particles[i4], spring)
        
    
    for x in range(col):
        for y in range(row):
            i = y + x*row
            particles[i].applyForce(0, 10.0)
            particles[i].applyForce(-particles[i].vx*0.1, -particles[i].vy*0.1)
            if y == 0 and x%4 == 0:
                pass
            else:
                particles[i].update(dt)
            particles[i].show()
        
        
        
        
        
        
        
        
        
        
        
    