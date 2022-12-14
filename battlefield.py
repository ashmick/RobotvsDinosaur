from dinosaur import Dinosaur
from robot import Robot

class Battlefield:
    
    def __init__(self) :
       self.robot= Robot("Big Techie")
       self.dinosaur= Dinosaur("Da Monster",20)
    
    def run_game(self):
        # if battle gets to 0 then shut off
        
        # Robot hits dino
        self.robot.attack(self.dinosaur.name)
        battle_one_results= self.dinosaur.health - self.robot.active_weapon.attack_power
        print(f'{self.dinosaur.name} now has a health of {battle_one_results}%!!!')
        
        # dino hits robo
        self.dinosaur.attack(self.robot.name)
        battle_two_results=self.dinosaur.health-self.dinosaur.attack_power
        print(f'{self.robot.name} just got served and now has health of {battle_two_results}%')

        # robot hits dino again
        self.robot.attack(self.dinosaur.name)
        battle_three_results= battle_one_results-self.robot.active_weapon.attack_power        
        print(f'I think {self.robot.name} has an unfair advantage here. But here he goes again with his {self.robot.active_weapon.name}. One quick plunder and {self.dinosaur.name} is now looking a little less monsterish. Health has went down and now little monster is at {battle_three_results}%. He is on his way out of here I think')
        
        

        #I want the dinosaur to hit the robot and the health go down
        #then take the total of the new health amount 
        #then have the robot hit the dinosaur and display the new health from that
        
        # 100-20=total_new new_health
        # new_health- new damage= new health
        # pass
    
    def display_welcome(self):
        pass
    
    def battle_phase(self):
        pass
    
    def display_winner(self):
        pass