
# Recursion fractal animation.
# Each branch calls two more branches until the length of
# a single line is less than 1 pixel.
# the angle between the branches changes with time and we get an
# evovling pattern that moves between symmetric systems and nonsense.
#
# Kim Svenssson, Lund University, 2018


# initializes the program, creates a window
def setup():    
    size(400,400)


# creates a variable called t, to keep track of time
t = 0.0



# draws everything
# draw calls the branch-recursion function each time it draws.
# each call will create a new tree.
def draw():
    
    # draws a new background each frame
    background(234)
    
    # starts of the recursion with these values.
    # a single line starting at the bottom reaching upwards.
    branch(width/2, height-10, 100, radians(-90))
    
    # updates the time variable
    global t
    t += 0.002
    

# A recursive function designed to call itself
def branch(x,y,l,a):
    
    # if the length of a branch is shorter than 1 pixel, stop the recursion
    if l <  1:
        return
    else:
        # if the length is longer than 1 pixel, calculate the new end points for a line
        # using the cos() and sin() functions combined with the length
        x2 = x + l*cos(a)
        y2 = y + l*sin(a)
        
        # draw a line
        line(x,y,x2,y2)
        
        # call branch with the new positions as arguments and a short length 
        # and an angle that depends on t. allowing us to have an animation that changes
        # in time.
        branch(x2,y2, l/1.5, a-5*cos(t))
        branch(x2,y2, l/1.5, a+5*sin(t))