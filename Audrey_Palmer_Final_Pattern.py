canvasw = 1000
canvash = 1000

w = 100
h = 100

size(canvasw,canvash)
    
def square(w,h,i,j):
    fill(random(),random(),random(),1)
    stroke(1, 0, 0, .75)
    strokeWidth(10)

def circle(w,h,i,j):
    pad = 0.50
    fill(random(),random(),random(),1)
    oval(w*.25+i,h*.25+j,w*pad,h*pad)
    stroke(0, 0, 0, .7)
    strokeWidth(20)
       
def drawmymodule(w,h,i,j):
    rect(0+i,0+j,w,h)
    square(w,h,i,j)
    circle(w,h,i,j)
        
for i in range(0,canvasw,w):
    for j in range(0,canvash,h):
        drawmymodule(w,h,i,j)
    #nested for loop 
 
 