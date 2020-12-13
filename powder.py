import pygame
import time

def draw(self, position, colour):#, dimensions):       #Draw the particle to the board

            
    pygame.draw.rect(self.board, colour, [position[0], position[1], 15, 15])



class Sand():

    def __init__(self, coordinates):
        self.x = coordinates[0]      #Coordinates
        self.y = coordinates[1]
        self.exists = True
        self.colour = (255, 255, 102)   #Yellowy Sand Colour
        self.dimensions = (15, 15)
        self.fall_rate = 5  #Move every 5 frames
        self.current_fall = self.fall_rate
    
    def falling(self):
        if self.current_fall == 0:
            self.current_fall = self.fall_rate
            return True

        else:
            self.current_fall -= 1

    


class powder_game:

    def __init__(self):
        self._running = False
        self.board = None
        self.size = self.weight, self.height = 640, 400
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


        for particle in self.particles:

            if particle.falling():
                particle.y += particle.fall_rate        #"Fall" the object by as many pixels defined in fall_rate
                print(particle.fall_rate)
                self.draw((particle.x, particle.y), particle.colour)

    def on_render(self):

        
        pygame.display.update()
        #self.board.fill((0, 0, 0))

    def on_cleanup(self):
        pygame.quit()

    def spawn(self, position):  #Determine current selected particle (Or use a global set variable) and spawn that particle. Add particle object to particle list

        particle = Sand(position)
        self.particles.append(particle)
        
        self.draw(position, (255, 255, 102))

    def on_execute(self):
        
        if self.on_init() == False:
            self._running = False

        #x = 50
        #y = 50

        



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
            

    def draw(self, position, colour):#, dimensions):       #Draw the particle to the board

            
        pygame.draw.rect(self.board, colour, [position[0], position[1], 15, 15])

       



    









if __name__ == "__main__":

    #sand = sand()
    
    game = powder_game()
    game.on_execute()