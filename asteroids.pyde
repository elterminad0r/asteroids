from orbital import Orbital

def setup():
    size(800, 800, P3D)
    
    for _ in range(30):
        Orbital(10, 20, 170, 250, 0.6)

def draw():
    background(0)
    colorMode(HSB, 255, 255, 255)
    noStroke()
    fill(255)
    lights()
    translate(400, 400)
    sphere(150)
    Orbital.update()
    Orbital.draw()