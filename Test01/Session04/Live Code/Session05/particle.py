class Particle:
    
    def __init__(self, x, y, r, mass):
        self.x = x
        self.y = y
        self.r = r
        self.mass = mass
        self.vx = 0
        self.vy = 0
        self.ax = 0
        self.ay = 0
        
        self.oldX = []
        self.oldY = []
        self.oldT = []
        
        self.reversed = False
        self.reversed_index = -1
        
        self.drawTail = True

        
    def reverseV(self):
        if self.reversed:
            pass
        else:
            self.reversed = True
            self.reversed_index = len(self.oldX)
            self.vx = -self.vx
            self.vy = -self.vy
        
    def show(self):
        stroke(0)
        strokeWeight(2)
        for k in range(len(self.oldX)-1):
            if self.reversed:
                if k > self.reversed_index:
                    stroke(100,200,100)
            line(self.oldX[k], self.oldY[k], self.oldX[k+1], self.oldY[k+1])
        if len(self.oldX) > 0:
            line(self.oldX[len(self.oldX)-1], self.oldY[len(self.oldX)-1], self.x, self.y)
            
        noStroke()

        fill(150,70,70)
        ellipse(self.x, self.y, self.r*2.0, self.r*2.0)
        
    def update(self, dt, t):
        self.oldX.append(self.x)
        self.oldY.append(self.y)
        self.oldT.append(t)
        
        self.vx = self.vx + self.ax*dt
        self.vy = self.vy + self.ay*dt
        self.x = self.x + self.vx*dt
        self.y = self.y + self.vy*dt
        self.ax = 0
        self.ay = 0
        
        if len(self.oldX) > 10.0/(dt):
            self.oldX.remove(self.oldX[0])
            self.oldY.remove(self.oldY[0])
            self.oldT.remove(self.oldT[0])


    def applyForce(self, fx, fy):
        self.ax = self.ax + fx/self.mass
        self.ay = self.ay + fy/self.mass
        
    def interact(self, p):
        pass

                
                                        
    def checkWalls(self, dt):
        
        loss = 1.0
        if self.x + self.r > width:
            self.x = width - self.r
            self.applyForce(-2.0*self.vx*self.mass/dt*loss, 0)
        
        if self.y + self.r > height:
            self.y = height - self.r
            self.applyForce(0, -2.0*self.vy*self.mass/dt*loss)
        
        if self.x - self.r < 0:
            self.x = self.r
            self.applyForce(-2.0*self.vx*self.mass/dt*loss, 0)
            
        if self.y - self.r < 0:
            self.y = self.r
            self.applyForce(0, -2.0*self.vy*self.mass/dt*loss)


        
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
        