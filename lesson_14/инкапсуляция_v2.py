from accessify import private, protected, implements


class ICar:
    def show(self):
        pass

    def test(self):
        pass


@implements(ICar)
class Car:
    @private  # доступ будет только внутри этого класса
    def show_secret(self):
        print("Secret token")

    @protected  # доступ будет внутри этого класса и в дочерних
    def show_data_for_child_classes(self):
        print("Data for child classes")

    # доступ будет везде
    def show(self):
        print("Info from secret method")
        self.show_secret()
        print("Info from protected method")
        self.show_data_for_child_classes()

    def test(self):
        print("Test method")


class SuperCar(Car):
    def show_parent_methods(self):
        # print("Info from secret method")
        # self.show_secret()
        print("Info from protected method")
        self.show_data_for_child_classes()


super_car = SuperCar()
super_car.show_parent_methods()
# super_car.show_data_for_child_classes()

# car1 = Car()
# car1.show()
# car1.test()
# car1.show_data_for_child_classes()
# car1.show_secret()
