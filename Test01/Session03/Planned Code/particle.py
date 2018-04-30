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
        self.nx = 0
        self.ny = 0
        self.c = 1.0
        
    def show(self):
        noStroke()
        fill(150*self.c,200*self.c,220*self.c)
        ellipse(self.x, self.y, self.r*2.0, self.r*2.0)
        self.c = 1.0
        
    def update(self, dt):
       # self.x = self.x + self.nx
       # self.y = self.y + self.ny
        self.vx = self.vx + self.ax*dt
        self.vy = self.vy + self.ay*dt
        self.x = self.x + self.vx*dt
        self.y = self.y + self.vy*dt
        self.ax = 0
        self.ay = 0

        
        friction = 0.999
        if self.x-self.r < 0:
            self.x = self.r
            self.applyForce(-self.vx*2.0*self.mass/dt*friction, 0)
        if self.x+self.r > width:
            self.x = width - self.r
            self.applyForce(-self.vx*2.0*self.mass/dt*friction, 0)
        if self.y-self.r < 0:
            self.y = self.r
            self.applyForce(0, -self.vy*2.0*self.mass/dt*friction)
        if self.y+self.r > height:
            self.y = height - self.r
            self.applyForce(0, -self.vy*2.0*self.mass/dt*friction)

    def applyForce(self, fx, fy):
        self.ax = self.ax + fx/self.mass
        self.ay = self.ay + fy/self.mass
        
    def interact(self, p, dt):
        l = dist(self.x, self.y, p.x, p.y)
        r2 = self.r + p.r
        if l < (r2)*2.0:
            dx = (self.x - p.x)/(l+0.1)
            dy = (self.y - p.y)/(l+0.1)
            if l != 0:
                self.applyForce(-dx*4, -dy*4)
            
        if l < (r2)*3.5:

            
            if l != 0:
            
                vl = dist(self.vx, self.vy, p.vx, p.vy)
                dvx = (self.vx - p.vx)/(vl+0.1)
                dvy = (self.vy - p.vy)/(vl+0.1)
                f = -vl*0.03
                self.applyForce(f*dvx, f*dvy) 
                    
            if l < r2:
                    self.applyForce(dx*70, dy*70)
                    self.c *= 0.95
                
            if l < (r2)*0.1:
                if l != 0:
                    self.applyForce(dx*200.0, dy*200.0)
                
                                        
        


        
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
        