class runner:
    def __init__(self, name, experience, speed, medal):
        self.name = name
        self.experience = experience
        self.speed = speed
        self.medal = medal

    def run(self, kilometer):
        if kilometer > 9 and kilometer < 31:
            self.experience += kilometer
            self.level_up()
        else:
            print("10 to 30 kilometers are only allowed value")
            print("___________________")

    def level_up(self):
        if self.experience >= 100:
            self.experience -= 100
            self.medal += 1
            self.speed *= 1.20

    def display(self):
        print("name: ", self.name)
        print("experience: ", self.experience)
        print("speed: ", self.speed)
        print("medal: ", self.medal)
        print("___________________")

runner1 = runner("Wally", 0, 1, 0)
runner2 = runner("Bayoli", 0, 2, 1)

runner1.display()
runner1.run(30)
runner1.run(30)
runner1.run(30)
runner1.run(20)
runner1.display()
runner1.run(31)
runner1.run(30)
runner1.display()

runner2.display()
runner2.run(30)
runner2.run(10)
runner2.run(10)
runner2.run(20)
runner2.run(30)
runner2.display()

