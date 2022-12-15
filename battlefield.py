from dinosaur import Dinosaur
from robot import Robot

class Battlefield:
    
    def __init__(self) :
       self.robot= Robot("Big Techie",100)
       self.dinosaur= Dinosaur("Da Monster",20,100)
    
    def display_welcome(self):
        print("Welcome to the game")
        pass
    
    def battle_phase(self):
        while self.dinosaur.health > 0 and self.robot.health > 0:
            self.robot.attack(self.dinosaur)
            if self.dinosaur.health>0:
                self.dinosaur.attack(self.robot)
            
        pass
    
    def display_winner(self):
        if self.dinosaur.health > 0:
            print(f"{self.dinosaur.name} defeats {self.robot.name}")
        elif self.robot.health > 0:
            print(f"{self.robot.name} defeats {self.dinosaur.name}")
        pass
    
    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()
        pass
        
        
        
        
        
        # if battle gets to 0 then shut off
    #     battle_scores=[]
    #     while battle_scores[-1]  ==0:     
    #         self.robot.attack(self.dinosaur)
    #         battle_one_results= self.dinosaur.health - self.robot.active_weapon.attack_power
    #         print(f'{self.dinosaur.name} now has a health of {battle_one_results}%!!!')
    #         battle_scores.append(battle_one_results)
            

    # # Robot hits dino
    #         self.dinosaur.attack(self.robot.name)
    #         battle_one_results= self.robot.health - self.dinosaur.attack_power
    #         print(f'{self.robot.name} now has a health of {battle_one_results}%!!!')
    #         battle_scores.append(battle_one_results)
    #         if battle_one_results==0: 
            
                
            
    #         # dino hits robo
    #         self.dinosaur.attack(self.robot.name)
    #         battle_two_results=self.dinosaur.health-self.dinosaur.attack_power
    #         print(f'{self.robot.name} just got served and now has health of {battle_two_results}%')
    #         battle_scores.append(battle_two_results)
            
    #         # robot hits dino again
    #         self.robot.attack(self.dinosaur.name)
    #         battle_three_results= battle_one_results-self.robot.active_weapon.attack_power        
    #         print(f'I think {self.robot.name} has an unfair advantage here. But here he goes again with his {self.robot.active_weapon.name}. One quick plunder and {self.dinosaur.name} is now looking a little less monsterish. Health has went down and now little monster is at {battle_three_results}%. He is on his way out of here I think')
    #         battle_scores.append(battle_three_results)
    #         # dino hits robot
    #         self.dinosaur.attack(self.robot.name)
    #         battle_four_results=battle_two_results-self.dinosaur.attack_power
    #         print(f'Sheeesh! That was a doozy! I never saw a robot leak until today! Hang in there bro! Health is down to {battle_four_results}%!!!')
    #         battle_scores.append(battle_four_results)
            
    #         # robo hits dino
    #         self.robot.attack(self.dinosaur.name)
    #         battle_five_results= battle_three_results-self.robot.active_weapon.attack_power
    #         print(f'I think this may be it you guys. Let me go and calculate and come back to you')
    #         battle_scores.append(battle_five_results)
                
    #             #I want the dinosaur to hit the robot and the health go down
    #             #then take the total of the new health amount 
    #             #then have the robot hit the dinosaur and display the new health from that
                
    #             # 100-20=total_new new_health
    #         # new_health- new damage= new health
    #         # pass
    
   