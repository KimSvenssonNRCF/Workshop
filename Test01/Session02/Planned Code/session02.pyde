from particle import Particle

def setup():
    size(400,400)
    global p
    p = Particle( 100, 150, 20, 1.0)
    
def draw():
    background(234,234,234)
    p.applyForce(mouseX - p.x, mouseY - p.y)
    p.update(0.1)
    p.show()

    