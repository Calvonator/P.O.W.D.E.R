import pygame
from pygame import time
#import operator
import random
import time

class sll_iterator():

    def __init__(self, head):
        self.current = head

    def __iter__(self):
        return self

    def __next__(self):

        if not self.current:
            raise StopIteration

        else:
            item = self.current.element
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
        self.size += 1
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

        current = self.head

        if current is not None:
            if current.element.index == target: #If head is the target

                self.head = current.get_next()
                current = None
                return True
        
        while current is not None:
            if current.element.index == target:
                break

            previous = current
            current = current.get_next()

        if current == None:     #Key was not present
            return False
        
        previous.next = current.get_next()

        current = None


    def print(self):
        if self.head != None:
            current = self.head

            while current != None:
                print(current.element.index)
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


class button():

    def __init__(self, name, text, coordinates, colour):
        self.name = name
        self.x, self.y = coordinates[0], coordinates[1]
        self.dimensions = (50, 30)
        self.colour = colour
        self.text = text
        self.rect = pygame.Rect(self.x, self.y, self.dimensions[0], self.dimensions[1])
        
    


class Sand():

    def __init__(self, index, coordinates):
        self.index = index
        self.type = 0
        self.x, self.y = coordinates[0], coordinates[1]      #Coordinates
        #self.exists = True
        self.stop = False
        self.colour = (255, 255, 102)   #Yellowy Sand Colour
        self.dimension = (8, 8)
        self.rect = pygame.Rect(self.x, self.y, self.dimension[0], self.dimension[1])
        self.fall_rate = 8  #Fall 8 pixels per frame
    
    #Update the particles rect object with the particles new coordinates
    def update(self):
        self.rect.left, self.rect.top = self.x, self.y


class Life():

    def __init__(self, index, coordinates):
        self.index = index
        self.type = 1
        self.x, self.y = coordinates[0], coordinates[1]
        self.colour = (0, 255, 0)   #Yellowy Sand Colour
        self.dimension = (8, 8)
        self.grown = False
        self.growth_rate = 1       #Grow once every 60 frames (1 sec if running at 60 fps)
        self.growth_ctr = self.growth_rate
        self.rect = pygame.Rect(self.x, self.y, self.dimension[0], self.dimension[1])


    def grow(self):

        grow_side = random.randint(0, 7)

        
        #Straight Left growth
        if grow_side == 0:  
            new_x = self.x - self.dimension[0]  #Move to the left by the width of particle
            new_y = self.y                      #Keep on same y axis

            
        #Angle Up Left growth  
        if grow_side == 1: 
            new_x = self.x - self.dimension[0]
            new_y = self.y - self.dimension[1]


        #Straight Up growth
        if grow_side == 2:
            new_x = self.x
            new_y = self.y - self.dimension[1]


        #Angle Up Right growth
        if grow_side == 3: 
            new_x = self.x + self.dimension[0]
            new_y = self.y - self.dimension[1]

        #Straight Right growth
        if grow_side == 4: 
            new_x = self.x + self.dimension[0]
            new_y = self.y

        #Angle Down Right growth
        if grow_side == 5: 
            new_x = self.x + self.dimension[0]
            new_y = self.y + self.dimension[1]

        #Straight Down growth
        if grow_side == 6: 
            new_x = self.x
            new_y = self.y + self.dimension[1]

        #Angle Down Left growth
        if grow_side == 7: 
            new_x = self.x - self.dimension[0]
            new_y = self.y + self.dimension[1]
        
        return (new_x, new_y)
        



class powder_game:

    def __init__(self):
        self._running = False
        self.board = None
        self.size = self.width, self.height = 1280, 720
        self.particles = singly_linked_list()
        self.particle_size = 0
        self.buttons = []
        self.current_particle = "sand"
        #self.orig_surf = None
        #self.new_surf = None


    def on_init(self):
        pygame.init()
        self.board = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        
        #Draw menu buttons
        smallfont = pygame.font.SysFont("Corbel", 25)

        #Button Text
        sand_text = smallfont.render("Sand", True, (255, 255, 255))
        life_text = smallfont.render("Life", True, (255, 255, 255))

        #Button Coords
        sand_button_coords = (100, 50)
        life_button_coords = (170, 50)

        #Create button object
        self.buttons.append(button("sand_button", sand_text, sand_button_coords, (255, 255, 102)))
        self.buttons.append(button("life_button", life_text, life_button_coords, (0, 255, 0)))
        





    def on_event(self, event):

        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()

            if self.buttons[0].rect.collidepoint(mouse_pos):     #Sand particle selected
                self.current_particle = "sand"
                return

            if self.buttons[1].rect.collidepoint(mouse_pos):     #Life particle selected
                self.current_particle = "life"
                return


            self.spawn(mouse_pos)


        if event.type == pygame.QUIT:       #Quit the game if crossed out
            self._running = False

    def draw_menu(self):
        
        for button in self.buttons:
            pygame.draw.rect(self.board, button.colour, button.rect)


    def on_loop(self):

        self.board.fill((0, 0, 0))
        #Update each particle
        for particle in self.particles:

            if particle.type == 0:
                #Put in own function
                
                #If particle has already collided, skip
                if particle.stop:
                    self.draw(particle)
                    continue

                if self.detect_collision(particle):
                    particle.stop = True
                    #self.draw(particle)
                    continue
                    
                #Remove particles out of window
                if particle.x < 0 or particle.x > self.size[0]: #width
                    self.particles.delete(particle.index)
                    self.particle_size -= 1
                    print("REMOVED!")
                elif particle.y < 0 or particle.y > self.size[1]: #height
                    self.particles.delete(particle.index)
                    self.particle_size -= 1
                    print("REMOVED!")


                #Detect collision with other particles


                particle.y += particle.fall_rate      #"Fall" the object by as many pixels defined in fall_rate
                self.draw(particle)

                particle.update()

            if particle.type == 1:


                #Stop growth outside of the window  NOTE: Maybe both ifs can merged, but I think readability better this way
                if particle.x < 0 or particle.x > self.size[0]: #width
                    particle.grown = True      #Stops the growth
                elif particle.y < 0 or particle.y > self.size[1]: #height
                    particle.grown = True

                #Check if particle has stopped growing
                if particle.grown == True:
                    self.draw(particle)
                    continue
                
                #print(particle.growth_ctr)
                #Check if the particle is ready to grow (0) if not, decrement the growth counter
                if particle.growth_ctr > 0:
                    particle.growth_ctr -= 1

                elif particle.growth_ctr == 0:
                    growth_coordinates = particle.grow()
                    #print("GROW!")
                    self.spawn(growth_coordinates)
                    particle.grown = True
                    #particle.growth_ctr = particle.growth_rate #Reset the 




    def spawn_lots(self):

        #op = 0
        #while True:
        for x in range(10, 19, 25):
            self.spawn((x, 50))


    def on_render(self):
        #IDEA: See if looping through an updating positions and then loop again and render is more efficient
        #self.particle_size = len(self.particles)
        
        self.draw_menu()
    

        pygame.display.update()
        
    def detect_collision(self, particle_check):
        #Iterate over each particle to detect collision

        if self.particle_size < 2:
            return False

        for particle in self.particles:

            if particle_check.rect.left == particle.rect.left and particle_check.rect.top == particle.rect.top: #If the two particles have the same coordinates, assume its the same particle (To avoid having to create a second list without the particle being searched)
                continue

            if particle_check.rect.colliderect(particle.rect):
                #print("STOPPED!")

                particle_check.stop = True
                particle.stop = True    #Particle that collided with current particle
                
        
    def on_cleanup(self):
        pygame.quit()

    def spawn(self, position):  #Determine current selected particle (Or use a global set variable) and spawn that particle. Add particle object to particle list
        particle_index = self.particle_size + 1
        if self.current_particle == "sand":
            particle = Sand(particle_index, position)
        elif self.current_particle == "life":
            particle = Life(particle_index, position)

        self.particles.insert(particle)
        #self.draw(particle)
        self.particle_size += 1

    def on_execute(self):
        

        if self.on_init() == False:
            self._running = False

        #x = 50
        #y = 50

        #self.spawn_lots()
        #self.spawn_concrete()
        clock = pygame.time.Clock()


        while(self._running):
            
            #self.orig_surf = self.board.copy()
            #self.new_surf = pygame.surface.Surface()
            first = time.time()

            for event in pygame.event.get():
                self.on_event(event)
            
            
            
            #pygame.draw.rect(self.board, (255, 255, 102), [x, y, 15, 15])

            #Animate the fall for each particle


            #x += 3
            #y += 1
 
            #time.sleep(0.01)
            #self.particles.print()
            self.on_loop()
            self.on_render()

            second = time.time()
            frame = second - first
            print(frame)
            clock.tick(60)

    def draw(self, particle):       #Draw the particle to the board

            
        pygame.draw.rect(self.board, particle.colour, [particle.x, particle.y, particle.dimension[0], particle.dimension[1]])




    









if __name__ == "__main__":

    #sand = sand()
    
    game = powder_game()
    game.on_execute()