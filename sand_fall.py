import pygame
from pygame import time
#import time

def draw(self, position, colour):#, dimensions):       #Draw the particle to the board

            
    pygame.draw.rect(self.board, colour, [position[0], position[1], 15, 15])



class Sand():

    def __init__(self, coordinates):
        self.x = coordinates[0]      #Coordinates
        self.y = coordinates[1]
        self.exists = True
        self.colour = (255, 255, 102)   #Yellowy Sand Colour
        self.dimension = (8, 8)
        self.fall_rate = 0  #Move every 5 frames
        self.current_fall = self.fall_rate
    
    def falling(self):
        if self.current_fall == 0:
            self.current_fall = self.fall_rate
            return True

        else:
            self.current_fall -= 1
            return False

class Concrete():

    def __init__(self, coordinates):
        self.x, self.y = coordinates[0], coordinates[1]
        self.exists = True
        self.colour = (130, 130, 130)
        self.dimension = (8, 8)
        self.is_solid = True



class powder_game:

    def __init__(self):
        self._running = False
        self.board = None
        self.size = self.weight, self.height = 1280, 720
        self.particles = []
        #self.orig_surf = None
        #self.new_surf = None


    def on_init(self):
        pygame.init()
        self.board = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

    def on_event(self, event):

        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            self.spawn(mouse_pos)


        if event.type == pygame.QUIT:       #Quit the game if crossed out
            self._running = False

    def on_loop(self):
        pass


    def spawn_lots(self):

        for x in range(10, 500, 25):
            self.spawn((x, 50))


    def on_render(self):
        
        self.board.fill((0, 0, 0))
        
        for particle in self.particles:
            try:    
                if particle.falling():
                    particle.y += 8#particle.fall_rate        #"Fall" the object by as many pixels defined in fall_rate
                    #print(particle.fall_rate)
                    self.draw((particle.x, particle.y), particle.colour, particle.dimension)
            except:
                pass
        pygame.display.flip()
        
        
    def on_cleanup(self):
        pygame.quit()

    def spawn(self, position):  #Determine current selected particle (Or use a global set variable) and spawn that particle. Add particle object to particle list
        
        particle = Sand(position)
        self.particles.append(particle)
        
        self.draw(position, particle.colour, particle.dimension)

    def spawn_concrete(self):
        for x in range(1, 1280, 8):
            particle = Concrete((x, 8))

            self.particles.append(particle)

            self.draw((particle.x, particle.y), particle.colour, particle.dimension)
        pygame.display.flip()

    def on_execute(self):
        
        

        if self.on_init() == False:
            self._running = False

        #x = 50
        #y = 50

        self.spawn_lots()
        self.spawn_concrete()
        clock = pygame.time.Clock()


        while(self._running):
            
            #self.orig_surf = self.board.copy()
            #self.new_surf = pygame.surface.Surface()


            for event in pygame.event.get():
                self.on_event(event)
            
            
            
            #pygame.draw.rect(self.board, (255, 255, 102), [x, y, 15, 15])

            #Animate the fall for each particle


            #x += 3
            #y += 1
 
            #time.sleep(0.01)

            self.on_loop()
            self.on_render()
            clock.tick(60)

    def draw(self, position, colour, dimension):       #Draw the particle to the board

            
        pygame.draw.rect(self.board, colour, [position[0], position[1], dimension[0], dimension[1]])




    









if __name__ == "__main__":

    #sand = sand()
    
    game = powder_game()
    game.on_execute()