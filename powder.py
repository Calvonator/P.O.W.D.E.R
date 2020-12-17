import pygame
from pygame import time
import operator

#import time




def draw(self, position, colour):#, dimensions):       #Draw the particle to the board

            
    pygame.draw.rect(self.board, colour, [position[0], position[1], 15, 15])



class Sand():

    def __init__(self, coordinates):
        self.x, self.y = coordinates[0], coordinates[1]      #Coordinates
        #self.exists = True
        self.stop = False
        self.colour = (255, 255, 102)   #Yellowy Sand Colour
        self.dimension = (8, 8)
        self.rect = pygame.Rect(self.x, self.y, self.dimension[0], self.dimension[1])
        self.fall_rate = 8  #Fall 8 pixels per frame
    
    def update(self):
        self.rect.left, self.rect.top = self.x, self.y


class powder_game:

    def __init__(self):
        self._running = False
        self.board = None
        self.size = self.width, self.height = 1280, 720
        self.particles = []
        self.particle_size = 0
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

        #op = 0
        #while True:
        for x in range(10, 19, 25):
            self.spawn((x, 50))


    def on_render(self):

        self.particle_size = len(self.particles)
        
        self.board.fill((0, 0, 0))

        for particle in self.particles:
            particle.update()
        
        for particle in self.particles:

            
            #Remove particles out of window
            if particle.x < 0 or particle.x > self.size[0]: #width
                self.particles.remove(particle)
                print("REMOVED!")
            elif particle.y < 0 or particle.y > self.size[1]: #height
                self.particles.remove(particle)
                print("REMOVED!")

            #If particle has collided, skip
            if particle.stop:
                self.draw(particle)
                continue

            if self.detect_collision(particle):
                particle.stop = True

            particle.y += particle.fall_rate      #"Fall" the object by as many pixels defined in fall_rate
            self.draw(particle)

            #print(particle.y)

        pygame.display.update()
        
    def detect_collision(self, particle_check):
        #Iterate over each particle to detect collision

        if self.particle_size < 2:
            return False

        for particle in self.particles:

            if particle_check.rect.left == particle.rect.left and particle_check.rect.top == particle.rect.top: #If the two particles have the same coordinates, assume its the same partcile (To avoid having to create a second list without the partcile being searched)
                continue

            if particle_check.rect.colliderect(particle.rect):
                #print("STOPPED!")

                particle_check.stop = True
                particle.stop = True    #Particle that collided with current particle
                
        
    def on_cleanup(self):
        pygame.quit()

    def spawn(self, position):  #Determine current selected particle (Or use a global set variable) and spawn that particle. Add particle object to particle list
        
        particle = Sand(position)
        self.particles.append(particle)
        
        self.draw(particle)


    def on_execute(self):
        
        

        if self.on_init() == False:
            self._running = False

        #x = 50
        #y = 50

        self.spawn_lots()
        #self.spawn_concrete()
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

    def draw(self, particle):       #Draw the particle to the board

            
        pygame.draw.rect(self.board, particle.colour, [particle.x, particle.y, particle.dimension[0], particle.dimension[1]])




    









if __name__ == "__main__":

    #sand = sand()
    
    game = powder_game()
    game.on_execute()