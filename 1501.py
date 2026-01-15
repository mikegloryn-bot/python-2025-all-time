# class Sim:
#     def __init__(self, name, energy=50):
#         self.name = name
#         self.energy = energy
# class Bed:
#     def use_for_sleep(self, sim):
#         sim.energy = 100
#
# my_sim = Sim(name='Bob')
# my_bed = Bed()
# my_bed.use_for_sleep(my_sim)
# print(f'Энергия сима {my_sim.name} теперь {my_sim.energy}')
class Home:
    def __init__(self, name):
        self.name = name
    def sleep(self, sim):
        print(f"{sim.name} спит в доме {self.name}")
        sim.energy += 20
class Job:
    def __init__(self, title, salary):
        self.title = title
        self.salary = salary
    def work(self, sim):
        print(f"{sim.name} работает как {self.title}")
        sim.money += self.salary
        sim.energy += 25
class Sim:
    def __init__(self, name, home, job):
        self.name = name
        self.energy = 50
        self.money = 100
        self.home = home
        self.job = job
    def eat(self):
        print(f"{self.name} ест 🍕")
        self.energy += 10
        self.money -= 5
    def show_status(self):
        print("------")
        print(f"Имя: {self.name}")
        print(f"Энергия: {self.energy}")
        print(f"Деньги: {self.money}")
home = Home('Уютный дом')
job = Job("Программист", 50)


sim = Sim('Гена', home, job)

sim.show_status()
sim.job.work(sim)
sim.home.sleep(sim)
sim.eat()
sim.show_status()