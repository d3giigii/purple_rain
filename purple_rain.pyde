from RainDrop import RainDrop

width = 1280
height = 720
num_drops = 1000
drop_list = [RainDrop(width) for drop in xrange(num_drops)]

def setup():
    size(width, height)
    frameRate(144)
    pass

def draw():
    background(255, 210, 255)
    for drop in drop_list:
        drop.fall()
        drop.show()
    pass
