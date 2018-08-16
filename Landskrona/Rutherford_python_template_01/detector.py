class Detector:
    
    def __init__(self, x, y, r):
        
        self.x = x
        self.y = y
        self.r = r
        self.detections = [0 for k in range(360)]
        self.decay = False
        
    
    def detect(self, p):
        if dist(self.x, self.y, p.x, p.y) >= self.r and dist(self.x, self.y, p.oldX, p.oldY) <= self.r:
            #if p.x >= width/2 +15.0 or p.x <= width/2 - 15.0:
            self.detectTrue(p)
            p.reset()
                
            
    def detectTrue(self, p):
        l = dist(self.x, self.y, p.x, p.y)
        dx = -(self.x - p.x)
        dy = -(self.y - p.y)

        theta = atan2(dy, dx)
            

        self.detections[floor(degrees((theta+TWO_PI)%TWO_PI))] += 1
        #println(floor(degrees(theta+PI)))
        
        
    def show(self):    

        
        deg = 0.0
        colorMode(HSB)
        for d in self.detections:
            x = self.x + (self.r+1)*cos(radians(deg))
            y = self.y + (self.r+1)*sin(radians(deg))
            if self.decay:
                x2 = self.x + (self.r + 30*sqrt(d) + 1.0)*cos(radians(deg))
                y2 = self.y + (self.r + 30*sqrt(d) + 1.0)*sin(radians(deg))
            else:
                x2 = self.x + (self.r + 10*sqrt(d) + 1.0)*cos(radians(deg))
                y2 = self.y + (self.r + 10*sqrt(d) + 1.0)*sin(radians(deg))  
            deg += 1.0
            #if deg%60 == 0:
                #text("degree: " + str(deg), x-30, y)
            if d != 0:
                strokeWeight(2)
                
                stroke(map(deg, 0, 360, 0, 255), 200,200)
                line(x,y,x2,y2)
            
        colorMode(RGB)
        noFill()
        stroke(0)
        strokeWeight(1)
        ellipse(self.x, self.y, self.r*2, self.r*2)
        
        if self.decay:
            for k in range(len(self.detections)):
                self.detections[k] *= (1.0 - 0.0015)
                #self.detections[k] += -1
        
        

            
            
            
            
        
        
        
        
    