class Player:
    def _init_(self):
        self.health = 100
        self.ammo = 10

        self.move()
        self.shoot()

    def move(self):
        print('Moving..')
    
    def shoot(self):
        print('Shooting..')
