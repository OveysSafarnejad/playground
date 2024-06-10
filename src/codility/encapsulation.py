
class Encapsulation:

    def __init__(self, instance_attr: str):
        self.__instance_attr = instance_attr

    def __private_access_controller(self):
        return 'Mr ' + self.__instance_attr

    def public_getter(self):
        return self.__private_access_controller()


if __name__ == '__main__':
    instance = Encapsulation(instance_attr="Oveys")
    print(instance.public_getter())
    # print(instance.__instance_attr) raises error
