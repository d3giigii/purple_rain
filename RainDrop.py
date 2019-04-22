class RainDrop():
    def __init__(self, w):
        self.x_pos = random(w)                          # set x pos to random position 
        self.y_pos = random(-100, -50)                  # set y pos to random position above screen 
        self.y_speed = random(4, 10)                    # set falling speed of each drop to random val
        self.gravity = random(.05, .2)                  # set gravity 
        self.length = random(10, 20)*(10)*self.gravity  # length should be influenced by falling speed i.e. faster drops appear larger
        pass
    
    def show(self):
        stroke(140, 45, 225)
        line(self.x_pos, self.y_pos, self.x_pos, self.y_pos+self.length)
        pass
    
    def fall(self):
        self.y_pos += self.y_speed            # drop falls downward y_speed pixels
        self.y_speed += self.gravity          # y_speed gradually increases by gravity
        
        # if drop reaches bottom, get new random values for drop. 
        if self.y_pos > 720:                   
            self.x_pos = random(width)                      
            self.y_pos = random(-100, -50)                  
            self.y_speed = random(4, 10)                    
            self.gravity = random(.05, .2)                  
            self.length = random(10, 20)*(10)*self.gravity 
        pass
    pass
