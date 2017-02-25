# Animation Example

time = 0   # use time to move objects from one frame to the next

def setup():
    size (800, 800, P3D)
    perspective (60 * PI / 180, 1, 0.1, 1000)  # 60 degree field of view
    
def draw():
    global time
    time += 0.01

    camera (0, 0, 100, 0, 0, 0, 0,  1, 0)  # position the virtual camera

    background (255, 255, 255)  # clear screen and set background to white
    # create a directional light source
    ambientLight(50, 50, 50);
    lightSpecular(255, 255, 255)
    directionalLight (100, 100, 100, -0.3, 0.5, -1)
    rotateX(PI)
    rotateY(PI)
    rotateY(time)
    rotateZ(time/4)
    rotateZ(time/6)
    noStroke()
    specular (180, 180, 180)
    shininess (15.0)
    
    # red box
    '''
    fill (255, 0, 0)
    pushMatrix()
    translate (-30, 0, 0)
    rotateX (time)
    box(20)
    popMatrix()
    
    # green sphere
    fill (0, 250, 0)
    pushMatrix()
    translate (0, 8 * sin(4 * time), 0)  # move up and down
    sphereDetail(60)  # this controls how many polygons are used to make a sphere
    sphere(10)
    popMatrix()
    '''
    # blue cylinder
    
    fill (78,255,108)
    pushMatrix()
    translate (0, 0, 0)
    rotateX (80)
    scale (10, 10, 10)
    body()
    popMatrix()
    pushMatrix()
    rotateX (80)
    #scale (10, 10, 10)
    translate(00, 0, 10)
    face()
    popMatrix()
    fill (75,208,45)
    pushMatrix()
    legs()
    popMatrix()
    pushMatrix()
    antennas()
    popMatrix()
    pushMatrix()
    hands()
    popMatrix()
    pushMatrix()
    eyes()
    popMatrix()
# cylinder with radius = 1, z range in [-1,1]
def cylinder(sides = 64):
    # first endcap
    
    beginShape()
    for i in range(sides):
        theta = i * 2 * PI / sides
        x = cos(theta)
        y = sin(theta)
        vertex ( x,  y, -1)
    endShape(CLOSE)
    
    # second endcap
    beginShape()
    for i in range(sides):
        theta = i * 2 * PI / sides
        x = cos(theta)
        y = sin(theta)
        vertex ( x,  y, 1)
    endShape(CLOSE)
    
    # sides
    x1 = 1
    y1 = 0
    for i in range(sides):
        theta = (i + 1) * 2 * PI / sides
        x2 = cos(theta)
        y2 = sin(theta)
        beginShape()
        normal (x1, y1, 0)
        vertex (x1, y1, 1)
        vertex (x1, y1, -1)
        normal (x2, y2, 0)
        vertex (x2, y2, -1)
        vertex (x2, y2, 1)
        endShape(CLOSE)
        x1 = x2
        y1 = y2
    
def body(sides = 64): 
    cylinder()
def face(sides = 64):
    sphere(10)
    pushMatrix()
    translate(0,0,9)
    scale(0.06,0.06,0.06)
    #rotateX(PI/2);
    rotateZ(PI/3);
    triangularPyramid()
    popMatrix()

def triangularPyramid(sides = 64):
    #translate(400, 400, 0)
    #stroke(0,0,0)
    fill(188,27,57)
    beginShape()
    vertex(-100, -100, -100);
    vertex( 100, -100, -100);
    vertex(   0,    0,  100);
    endShape(CLOSE)
    fill(231,207,0)
    beginShape()
    vertex( 100, -100, -100);
    vertex( 100,  100, -100);
    vertex(   0,    0,  100);
    endShape(CLOSE)
    fill(188,27,57)

    beginShape()
    vertex( 100, 100, -100);
    vertex(-100, 100, -100);
    vertex(   0,   0,  100);
    endShape(CLOSE)
    fill(231,207,0)

    beginShape()
    vertex(-100,  100, -100);
    vertex(-100, -100, -100);
    vertex(   0,    0,  100);
    endShape(CLOSE)
def legs(sides = 64):
    pushMatrix()
    translate(05,-11,0)
    scale(2,6,2)
    rotateX(PI/2)
    cylinder()
    popMatrix()
    pushMatrix()
    translate(-5,-11,0)
    scale(2,6,2)
    rotateX(PI/2)
    cylinder()
    popMatrix()
def antennas(sides = 64):
    pushMatrix()
    translate(7,18,0)
    rotateZ(3*PI/4)
    scale(2,2,2)
    rotateX(PI/2)
    cylinder()
    popMatrix()
    pushMatrix()
    translate(8.0,19,-0.0)
    sphere(2.1)
    popMatrix()
    pushMatrix()
    translate(-7,18,0)
    rotateZ(PI/4)
    scale(2,2,2)
    rotateX(PI/2)
    cylinder()
    popMatrix()
    pushMatrix()
    translate(-8.0,19,-0.0)
    sphere(2.1)
    popMatrix()
def hands(sides = 64):
    pushMatrix()
    translate(10,5,0)
    scale(2,7,2)
    rotateX(PI/2)
    cylinder()
    popMatrix()
    pushMatrix()
    translate(-10,5,0)
    scale(2,7,2)
    rotateX(PI/2)
    cylinder()
    popMatrix()
def eyes(sides = 64):
    fill(255,255,255)
    pushMatrix()
    translate(6,14,6)
    scale(1.5,1.5,0.5)
    rotateX(-PI/16)
    #rotateX(-PI/8)
    rotateY(PI/8)
    cylinder()
    popMatrix()
    pushMatrix()
    translate(-6,14,6)
    scale(1.5,1.5,0.5)
    rotateX(-PI/16)
    rotateY(-PI/8)
    cylinder()
    popMatrix()