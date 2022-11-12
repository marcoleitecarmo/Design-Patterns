class Animal:
    def mak_noise(self) -> None:
        raise NotImplementedError('You have to implement make_noise')

    def move(self) -> None:
        raise NotImplementedError('You have to implement move')


class Dog(Animal):
    def mak_noise(self) -> None:
        print('Au Au')

    def move(self) -> None:
        print('Dog esta se movendo')


dog = Dog()
dog.mak_noise()
dog.move()
