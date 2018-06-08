
x_width = 2.5
x_mid = -0.5
y_width = 2.5
y_mid = 0.0

tex01 = []
tex02 = []
tex03 = []
tex04 = []
tex05 = []
tex06 = []
tex07 = []
tex08 = []
tex09 = []
tex10 = []
tex11 = []
tex12 = []
tex13 = []
tex14 = []
tex15 = []
tex16 = []

tex01Done = False
tex02Done = False
tex03Done = False
tex04Done = False
tex05Done = False
tex06Done = False
tex07Done = False
tex08Done = False
tex09Done = False
tex10Done = False
tex11Done = False
tex12Done = False
tex13Done = False
tex14Done = False
tex15Done = False
tex16Done = False

sx = 40
sy = 40


def setup():
    size(400,400)
    global tex01, tex02, tex03, tex04, tex05, tex06, tex07, tex08, tex09, tex10, tex11, tex12, tex13, tex14, tex15, tex16
    for k in range(10000):
        tex01.append(0)
    for k in range(10000):
        tex02.append(0)
    for k in range(10000):
        tex03.append(0)
    for k in range(10000):
        tex04.append(0)
    for k in range(10000):
        tex05.append(0)
    for k in range(10000):
        tex06.append(0)
    for k in range(10000):
        tex07.append(0)
    for k in range(10000):
        tex08.append(0)
    for k in range(10000):
        tex09.append(0)
    for k in range(10000):
        tex10.append(0)
    for k in range(10000):
        tex11.append(0)
    for k in range(10000):
        tex12.append(0)
    for k in range(10000):
        tex13.append(0)
    for k in range(10000):
        tex14.append(0)
    for k in range(10000):
        tex15.append(0)
    for k in range(10000):
        tex16.append(0)

def draw():
    global x_mid, y_mid, x_width, y_width
    global tex01, tex02, tex03, tex04, tex05, tex06, tex07, tex08, tex09, tex10, tex11, tex12, tex13, tex14, tex15, tex16
    global tex01Done, tex02Done, tex03Done, tex04Done, tex05Done, tex06Done, tex07Done, tex08Done, tex09Done, tex10Done, tex11Done, tex12Done, tex13Done, tex14Done, tex15Done, tex16Done

    colorMode(HSB)
    loadPixels()
    if tex01Done:
        tex01Done = False
        for x in range(100):
            for y in range(100):
                i1 = y + x*width
                i2 = y + x*width
                pixels[i1] = color(tex01[i1], 200,200)
    if tex02Done:
        tex02Done = False
        for x in range(100):
            for y in range(100):
                i1 = y + x*width
                i2 = y + (x+100)*width
                pixels[i2] = color(tex02[i1], 200,200)
    if tex03Done:
        tex03Done = False
        for x in range(100):
            for y in range(100):
                i1 = y + x*width
                i2 = y + (x+200)*width
                pixels[i2] = color(tex03[i1], 200,200)
    
    updatePixels()
    
def mousePressed():
    global x_mid, y_mid, x_width, y_width
    xt = map(mouseX, 0, width, x_mid - x_width/2.0, x_mid + x_width/2.0)
    yt = map(mouseY, 0, height, y_mid - y_width/2.0, y_mid + y_width/2.0)
    # x_mid = xt
    # y_mid = yt
    # x_width *= 0.5
    # y_width *= 0.5
    thread("calcSubsection()")
    calcSubsection(mouseX, mouseY)
    
def runAll():
   pass 
    
    
def calcSubsection(x,y):
    global tex01, tex02, tex03, tex04, tex05, tex06, tex07, tex08, tex09, tex10, tex11, tex12, tex13, tex14, tex15, tex16
    nr = floor(map(y + x*width,0, 400*400, 0, 16))
    
    nrX = floor(x/100)
    nrY = floor(y/100)
    
    nr = nrY*4 + nrX
     
    comp = []
    if nr == 0:
        comp = tex01
    if nr == 1:
        comp = tex02
    if nr == 2:
        comp = tex03
    if nr == 3:
        comp = tex04
    if nr == 4:
        comp = tex05
    if nr == 5:
        comp = tex06
    if nr == 6:
        comp = tex07
    if nr == 7:
        comp = tex08
    if nr == 8:
        comp = tex09
    if nr == 9:
        comp = tex10
    if nr == 10:
        comp = tex11
    if nr == 11:
        comp = tex12
    if nr == 12:
        comp = tex13
    if nr == 13:
        comp = tex14
    if nr == 14:
        comp = tex15
    if nr == 15:
        comp = tex16
    i = 0
    for xn in range(nrX*100, nrX*100 + 100):
        for yn in range(nrY*100, nrY*100 + 100):
            xt = map(x, 0, width, x_mid - x_width/2.0, x_mid + x_width/2.0)
            yt = map(y, 0, height, y_mid - y_width/2.0, y_mid + y_width/2.0)
            
            k = 0
            
            Re = xt
            Im = yt
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
            comp[i] = k
            i += 1
    
    if nr == 0:
        tex01Done = True
    if nr == 1:
        tex02Done = True
    if nr == 2:
        tex03Done = True
    if nr == 3:
        tex04Done = True
    if nr == 4:
        tex05Done = True
    if nr == 5:
        tex06Done = True
    if nr == 6:
        tex07Done = True
    if nr == 7:
        tex08Done = True
    if nr == 8:
        tex09Done = True
    if nr == 9:
        tex10Done = True
    if nr == 10:
        tex11Done = True
    if nr == 11:
        tex12Done = True
    if nr == 12:
        tex13Done = True
    if nr == 13:
        tex14Done = True
    if nr == 14:
        tex15Done = True
    if nr == 15:
        tex16Done = True
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    