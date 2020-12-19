import pygame
from pygame import time
import operator

#import time

class sll_iterator():

    def __init__(self, head):
        self.current = head

    def __iter__(self):
        return self

    def __next__(self):

        if not self.current:
            raise StopIteration

        else:
            item = self.current
            self.current = self.current.get_next()
            return item

class singly_linked_list():

    def __init__(self):
        self.head = None
        self.size = 0

    def __iter__(self):
        return sll_iterator(self.head)

    def create_node(self, value, next):
        node = singly_linked_list_node(value, None)
        return node


    def insert(self, value):
        if self.head != None:
            current = self.head

            while current != None:
                previous = current
                current = current.next 
            previous.next = self.create_node(value, None)
        else:
            self.head = self.create_node(value, None)


    def delete(self, target):           #Not done
        if self.head != None:
            current = self.head

            while current.element != target or current != None:    
                previous = current
                current = current.next
            

    def find_max(self):             
        if self.head != None:
            
            current = self.head
            max = current.element

            while current != None:
                if current.element > max:
                    max = current.element
                current = current.next
            return max
        else:
            return None
    
    def print(self):
        if self.head != None:
            current = self.head

            while current != None:
                print(current.element.y)
                current = current.next


    def find_target(self, target):
        
        current = self.head 
        
        while current != None:
            if current.element == target:
                return True
            current = current.next
        return False
            


class singly_linked_list_node():
    __slots__ = 'next', 'element'
    def __init__(self, value, next):
        self.next = next
        self.element = value

    def get_next(self):
        
        return self.next



def draw(self, position, colour):#, dimensions):       #Draw the particle to the board

            
    pygame.draw.rect(self.board, colour, [position[0], position[1], 15, 15])



class Sand():

    def __init__(self, coordinates):
        self.x, self.y = coordinates[0], coordinates[1]      #Coordinates
        self.exists = True
        self.colour = (255, 255, 102)   #Yellowy Sand Colour
        self.dimension = (8, 8)
        #self.rect = pygame.Rect(self.x, self.y, self.dimension)
        self.fall_rate = 5  #Move every 5 frames
        self.current_fall = self.fall_rate
    
    def falling(self):
        if self.current_fall == 0:
            self.current_fall = self.fall_rate
            return True

        else:
            self.current_fall -= 1
            return False



class powder_game:

    def __init__(self):
        self._running = False
        self.board = None
        self.size = self.weight, self.height = 1280, 720
        self.particles = singly_linked_list()
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
        self.particles.insert(particle)
        
        self.draw(position, particle.colour, particle.dimension)


    def on_execute(self):
        
        

        if self.on_init() == False:
            self._running = False

        #x = 50
        #y = 50

        self.spawn_lots()
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
            self.particles.print()
            clock.tick(60)

    def draw(self, position, colour, dimension):       #Draw the particle to the board

            
        pygame.draw.rect(self.board, colour, [position[0], position[1], dimension[0], dimension[1]])




    









if __name__ == "__main__":

    #sand = sand()
    
    game = powder_game()
    game.on_execute()