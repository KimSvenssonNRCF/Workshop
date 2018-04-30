
radie = 40.0
x = 100.0  # m
y = 200.0   # m
vx = 40.0 # m/s
vy = 0.0  # m/s

ax = 0.0 # m/(ss)
ay = 10.0 # m/(ss)
m = 1.0
dt = 0.1 # s

def setup():
    size(400,400)
    
    
def draw():
    global x,y,vx,vy,dt,radie,ax,ay,m
    
    background(234, 234, 234)
    fill(250,30,30)
    
    vx = vx + ax*dt
    vy = vy + ay*dt
    
    x = x + vx*dt
    y = y + vy*dt
    
    ax = 0
    ay = 0
    
    Fx = 0
    Fy = 0
    if x + radie > width:
        # v*m -> -v*m    
        Fx = -2.0*vx*m/dt
        x = width - radie
        
    if y + radie > height:
        Fy = -2.0*vy*m/dt
        y = height - radie
        
    if x - radie < 0:
        Fx = -2.0*vx*m/dt
        x = radie
        
    if y - radie < 0:
        Fy = -2.0*vy*m/dt
        y = radie
        
    ax = ax + Fx/m
    ay = ay + Fy/m + 9.81
    
    
    ellipse(x, y, radie*2, radie*2)
    saveFrame("movie/session1-####.png")
    
    
    
    
    
    