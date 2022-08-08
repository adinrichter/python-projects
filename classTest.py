class enemy:
    health = 100
    damage = 30
    speed = 20
    attackType = 'normal'
    abilities = 'none'

class wizard(enemy):
    magicDamage = 20
    mana = 100

class assassin(enemy):
    jumpSpeed = 40
    stealthDuration = 10
    
