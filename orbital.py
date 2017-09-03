from random import choice

def apply_to(l):
    def to_all(func):
        def f(*args, **kwargs):
            for i in list(l):
                func(i, *args, **kwargs)
        return f
    return to_all

class Orbital(object):
    inst = set()

    def __init__(self, min_r, max_r, min_obt, max_obt, elev_range):
        self.r = random(min_r, max_r)
        self.orbit = random(min_obt, max_obt)
        self.vel = random(0.01, 0.02)
        self.elev = choice([1, -1]) * random(elev_range)
        self.ang = random(TWO_PI)
        self.c = random(255)
        
        self.inst.add(self)
    
    @staticmethod
    @apply_to(inst)
    def update(self):
        self.ang += self.vel
    
    @staticmethod
    @apply_to(inst)
    def draw(self):
        pushMatrix()
        fill(self.c, 255, 255)
        rotateX(self.elev)
        rotateY(self.ang)
        translate(self.orbit, 0, 0)
        sphere(self.r)
        popMatrix()