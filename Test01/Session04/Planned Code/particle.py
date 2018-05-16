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

        
    def show(self):
        noStroke()
        fill(40,100,20)
        ellipse(self.x, self.y, self.r*2.0, self.r*2.0)
        
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
        
    def interact(self, p):
        pass

                
                                        
        


        
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
        