class Engine:
    def start(self):
        print(" Engine Started")


class Car:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        self.engine.start()


engine = Engine()
my_car = Car(engine)
my_car.start()
