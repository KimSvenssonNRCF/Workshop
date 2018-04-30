
x = 10
y = 10
vx = 2
vy = 3
ax = 0
ay = 1

def setup():
    size(400,400)
    
def draw():
    global x,y,vx,vy,ax,ay
    vx = vx + ax
    vy = vy + ay
    x = x + vx
    y = y + vy    
    if x < 0:
        vx = -vx
    if x > width:
        vx = -vx
    if y < 0:
        vy = -vy
    if y > height:
        vy = -vy
    background(234,234)
    fill(mouseX,mouseY,(mouseX+mouseY)/2.0)
    ellipse(x, y, 40, 40)
    