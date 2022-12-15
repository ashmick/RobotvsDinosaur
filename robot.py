from weapon import Weapon

class Robot:
    

    def __init__(self,name,health) :
        self.name=name
        self.health=health
        self.active_weapon= Weapon("sword",40)

    
    def attack (self,dinosaur):
        dinosaur.health -= self.active_weapon.attack_power
        print(f'{self.name} has made an attack with a {self.active_weapon.name} and has damaged the opponent by {self.active_weapon.attack_power}%!!!')
        # dinosaur_health_decline=self.active_weapon.attack_power
        # total= self.attack   - self.active_weapon.attack_power
        pass