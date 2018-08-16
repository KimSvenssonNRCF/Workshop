class Particle:
    
    def __init__(self, x, y, m, q):
        self.x = x
        self.y = y
        self.m = m
        self.q = q
        self.vx = 0
        self.vy = 0
        self.ax = 0
        self.ay = 0
        self.angle = HALF_PI
        self.spread = 50.0
        self.isAlpha = True
        self.oldX = x
        self.oldY = y
        
        
        
    def update(self, dt):
        self.oldX = self.x
        self.oldY = self.y
        self.vx = self.vx + self.ax*dt
        self.vy = self.vy + self.ay*dt    
        self.x = self.x + self.vx*dt
        self.y = self.y + self.vy*dt    
        self.ax = 0
        self.ay = 0
        self.isAlpha = True
        #self.angle = 0
        
        if self.y < 0:
            self.reset()
        # if self.y > height:
        #     self.reset()
        if self.x < 0:
            self.reset()
        if self.x > width:
            self.reset()
        
        
        
    def show(self):
        colorMode(HSB)
        noStroke()
        if self.isAlpha:
            fill(50, 200,200) 
        else:
            fill(190, 200,200) 
        ellipse(self.x, self.y, 5,5)
        
        
        
    def applyForce(self, fx, fy):
        self.ax = self.ax + fx/self.m
        self.ay = self.ay + fy/self.m
        
        

    def reset(self):
        
        self.y = height/2 + random(height)
        rx = random(-self.spread,self.spread)
        ry = 0
        self.x = rx
        
        xt = self.x*cos(self.angle-HALF_PI) - self.y*sin(self.angle-HALF_PI)
        yt = self.x*sin(self.angle-HALF_PI) + self.y*cos(self.angle-HALF_PI)
        
        self.x = xt
        self.y = yt
        
        self.x += width/2
        self.y += height/2
        
        #self.y = height/2 + (height/2 + random(height))*sin(self.angle) 
        #self.x = width/2 + (width/2 + random(-10, 10))*cos(self.angle)
        
        
        #self.y = height + random(height)
        #self.x = random(width/2 -10.0, width/2+10.0)
        self.vx = 0
        self.vy = 0
        F = 1000.0
        l = dist(width/2, height/2, self.x, self.y)
        dx = (width/2 + rx*cos(self.angle-HALF_PI) - ry*sin(self.angle-HALF_PI) - self.x)/(l + 0.01)
        dy = (height/2 + rx*sin(self.angle-HALF_PI) + ry*cos(self.angle-HALF_PI) - self.y)/(l + 0.01)
        self.applyForce(F*dx, F*dy)
        
    
    