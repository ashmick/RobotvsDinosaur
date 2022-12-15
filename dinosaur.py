from robot import Robot

class Dinosaur:
    pass

    def __init__(self, name, attack_power,health):
        self.name=name
        self.attack_power=attack_power
        self.health=health
        pass
    
    
    def attack(self,robot):
        robot.health -= self.attack_power
            
        # -=self.attack_power
        
        print(f'{self.name} has hit {robot.name} and now {robot.name} is losing his wires over this hit!! Health is going down by {self.attack_power}%!!')
        
        
       
        #I want the health to go down by the attack power of dino and display total
        
        
              
        pass