        
        #Game Idea: Have people pick etween 1 and 4. Randomly generate a numer to determine
        # the height of each number's bar. After choosing a bar, have the bar animate upwards.
        


        #A bar that animates in an angle
        x = 50

        while(self._running):
            
            for event in pygame.event.get():
                self.on_event(event)
            
            pygame.draw.rect(self.board, (255, 255, 102), [x + 10, x + 15, x + 15, x + 15])

            x += 1
            
            time.sleep(0.1)


    #Laser beams that go sideways


    



