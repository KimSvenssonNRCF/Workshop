
class Particle:
    
    def __init__(self, x, y, radius, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.mass = mass
        self.vx = 0
        self.vy = 0
        self.ax = 0
        self.ay = 0
        
    def show(self):
        #fill(self.vx*25,self.vy*25,self.mass)
        #fill(floor(random(255)), floor(random(255)), floor(random(255)))
        fill(dist(0,0,self.vx, self.vy)*10.0)
        noStroke()
        ellipse(self.x, self.y, self.radius*2, self.radius*2)
        
    def update(self, dt):
        self.vx = self.vx + self.ax*dt
        self.vy = self.vy + self.ay*dt
        self.x = self.x + self.vx*dt
        self.y = self.y + self.vy*dt
        
        self.ax = 0
        self.ay = 0
        
    def applyForce(self, fx, fy):
        self.ax = self.ax + fx/self.mass
        self.ay = self.ay + fy/self.mass
        
    def checkWalls(self, dt):
        
        if self.x + self.radius > width:
            self.x = width - self.radius
            self.applyForce(-2.0*self.vx*self.mass/dt, 0)
            
        if self.y + self.radius > height:
            self.y = height - self.radius
            self.applyForce(0, -2.0*self.vy*self.mass/dt)
            
        if self.x - self.radius < 0:
            self.x = self.radius
            self.applyForce(-2.0*self.vx*self.mass/dt, 0)
            
        if self.y - self.radius < 0:
            self.y = self.radius
            self.applyForce(0, -2.0*self.vy*self.mass/dt)
        
        
    
    def interact(self, p):
        l = dist(self.x, self.y, p.x, p.y)
        if l < self.radius + p.radius:
            dx = (self.x - p.x)/(l + 0.1)
            dy = (self.y - p.y)/(l + 0.1)
            P = 50.0
            self.applyForce(P*dx, P*dy)
            
            vl = dist(self.vx, self.vy, p.vx, p.vy)
            dvx = (self.vx - p.vx)/(vl + 0.1)
            dvy = (self.vy - p.vy)/(vl + 0.1)
            V = -8.0
            self.applyForce(V*dvx, V*dvy)
            
    
        
        
        
        
        
        
        
        
        
        
        