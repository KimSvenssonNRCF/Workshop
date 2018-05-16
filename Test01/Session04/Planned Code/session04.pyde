from particle import Particle

particles = []
dt = 0.03


def setup():
    size(400,400) 
    global s , row, col
    s = 10.0
    col = floor(width/s)
    row = floor(height/s)

    r = 5.0
    
    for x in range(col):
        for y in range(row):
            
            p = Particle(r + x*s,r+ y*s, r, 1.0) 
            particles.append(p)

    

def draw():
    background(234)
    

    for x in range(col):
        for y in range(row):
            i = y + x*row
            i1 = y-1 + x*row
            i2 = y + (x+1)*row
            i3 = y+1 + x*row
            i4 = y + (x-1)*row
            
            if y-1 >= 0:
                particles[i].interact(particles[i1]) 
            if x+1 < col:
                particles[i].interact(particles[i2])
            if y+1 < row:
                particles[i].interact(particles[i3])
            if x-1 >= 0:
                particles[i].interact(particles[i4])
            
        
    for x in range(col):
        for y in range(row):
            i = y + x*row
            particles[i].update(dt)
                
    for x in range(col):
        for y in range(row):
            i = y + x*row            
            particles[i].show()

        
        
        
        
        
        
        
        
        
    