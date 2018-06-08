class Ball:
    
    def __init__(self, r, x, y):
        self.x = x
        self.y = y
        self.r = r
        self.particles = []
        
        
    def createBall(self):
        
        for n in range(100):
            p = Particle(self.x + random(-1,1)*self.r, self.y + random(-1,1)*self.r, 1.0)
            self.particles.append(p)
            
    def evolveBall(self):
        
        for k in range(100):
            
            for p in particles:
                for p2 in particles:
                    l = dist(p.x, p.y, p2.x, p2.y)
                    dx = (p.x - p2.x)
                    dy = (p.y - p2.y)
                    p.applyForce(dx, dy)
            
            for p in particles:
                p.update(0.1)
                l = dist(p.x, p.y, self.x, self.r)
                if l > r:
                    p.x = (p.x - self.x)/l*r + self.x
                    p.y = (p.y - self.y)/l*r + self.y

    def showBall(self):
        for p in particles():
            p.show()
                    
            
        
        