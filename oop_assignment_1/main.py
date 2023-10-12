class Car:
    def __init__(self, t_speed):
        self.t_speed = t_speed
        self.location = 0

    def show_speed(self):
        print(self.t_speed)

    def drive(self):
        self.location += 10

    def stop(self):
        print(self.location)
        self.location = 0

sedan = Car(140)
sedan.show_speed()
sedan.drive()
sedan.drive()
sedan.stop()