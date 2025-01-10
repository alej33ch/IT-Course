class Characters:
    def __init__(self, health, damage, speed):
        self.health = health
        self.damage = damage
        self.speed = speed

    def double_speed(self):
        self.speed *= 2

# Characteres
warrior = Characters(100, 50, 30)
ninja = Characters(100, 40, 80)

print(f"Warrior speed: {warrior.speed}")
print(f"Ninja speed: {ninja.speed}")

ninja.double_speed()

print(f"Warrior speed: {warrior.speed}")
print(f"Ninja speed: {ninja.speed}")