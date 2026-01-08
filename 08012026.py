# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         return f"{self.name} издаёт какой-то звук"
#
# my_cat = Cat("Мурчик")
# print(my_cat.speak())
# my_cat.name = "Барсик"
# print(my_cat.name)
# class Zombie:
# #     pass
# # zombie1 = Zombie()
# # zombie2 = Zombie()
# # print(zombie1)
# # print(zombie2)
# # print(type(zombie1)
# #   def __init__(self, name):
# #     self.name = name
# #     self.health = 50
# # z1 = Zombie("Loodik")
# # print(z1.name)
# # print(z1.health)
#     def __init__(self, name):
#         self.name = name
#         self.health = 50
#     def growl(self):
#         return f"{self.name} рычит: УУУУ!"
# z1 = Zombie("dodik")
# print(z1.growl())
print('Bitva Geroev')
class Character:
    def __init__(self, name, health=100, max_health=None, damage=20):
        self.name = name
        self.health = health
        self.max_health = max_health or health
        self.damage = damage
    def status(self):
        percent = (self.health / self.max_health) * 100
        return f"⚔ {self.name} бьёт {target.name} на {self.damage}!"
    def attack(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        return f"🎇 {self.name} получил {damage} урона! Осталось: {self.health} HP"
    def is_alive(self):
        return self.health > 0