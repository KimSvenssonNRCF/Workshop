
x_width = 2.5
x_mid = -0.5
y_width = 2.5
y_mid = 0.0


def setup():
    size(400,400)
    

def draw():
    global x_mid, y_mid, x_width, y_width
    colorMode(HSB)
    loadPixels()
    for x in range(width):
        for y in range(height):
            i = x + y*height
            k = 0
            
            Re = map(x, 0, width, x_mid - x_width/2.0, x_mid + x_width/2.0) 
            Im = map(y, 0, height, y_mid - y_width/2.0, y_mid + y_width/2.0)
            cRe = Re
            cIm = Im
            while k < 255:
                Retemp = Re*Re - Im*Im + cRe
                Imtemp = cIm + 2*Re*Im
                Re = Retemp
                Im = Imtemp
                
                if dist(Re, Im, 0, 0) > 2:
                    break
                else:
                    k+= 1
            if k == 255:
                pixels[i] = color(255-k, 0,0)
            else:
                pixels[i] = color(255-k, 200,50+k)
    
    updatePixels()
    noLoop()
    
def mousePressed():
    global x_mid, y_mid, x_width, y_width
    xt = map(mouseX, 0, width, x_mid - x_width/2.0, x_mid + x_width/2.0)
    yt = map(mouseY, 0, height, y_mid - y_width/2.0, y_mid + y_width/2.0)
    x_mid = xt
    y_mid = yt
    x_width *= 0.5
    y_width *= 0.5
    loop()