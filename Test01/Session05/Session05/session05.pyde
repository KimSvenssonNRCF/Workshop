from particle import Particle



gx = 0.0
gy = 981 # cm/s^2   1 pixel = 1 cm
t = 0.0
def setup():
    size(400,400) 
  
    global p
    p = Particle(random(width), random(height/3), 10.0, 1.0) 
    p.vx = random(-400,400)
    p.vy = random(-400,400)


dt = 1.0/100.0
    

def draw():
    background(234)
    
    global p, t
    
            
    p.applyForce(gx*p.mass, gy*p.mass)    # applicera gravitationskraften
    p.update(dt, t)  # Uppdatera partiklens position
    p.checkWalls(dt) # kolla om partiklen krockar med väggarna
    
    t += dt # håll koll på vilken tid som förflutit
    
    p.drawTail = True  # rita upp partikelns senaste positioner
    p.show() # rita upp partiklen i fönstret
    
    
    
    
    
    
    # Skriver ut positionen och tidpunkten för den närmaste delen av svansen/bollen
    if mousePressed:
        maxL = 100000
        indx = -1
        for k in range(len(p.oldX)):
            l = dist(mouseX, mouseY, p.oldX[k], p.oldY[k])
            if l < maxL:
                maxL = l
                indx = k
        s = "("+ str(p.oldX[indx])+","+str(p.oldY[indx])+")"
        s = "( %.2f, %.2f, %.2f)" % (p.oldX[indx], p.oldY[indx], p.oldT[indx])
        if p.oldX[indx] > width -122:
            fill(255)
            stroke(0)
            strokeWeight(1)
            rect(p.oldX[indx]-123, p.oldY[indx]-15, 123, 20)
            fill(0)
            text(s, p.oldX[indx]-122, p.oldY[indx])
        else:
            fill(255)
            stroke(0)
            strokeWeight(1)
            rect(p.oldX[indx], p.oldY[indx]-15, 123, 20)
            fill(0)
            text(s, p.oldX[indx]+2, p.oldY[indx])
        fill(255,0,0)
        ellipse(p.oldX[indx], p.oldY[indx], 5,5)
        
            
    


        
        
        
        
        
        
        
        
        
    