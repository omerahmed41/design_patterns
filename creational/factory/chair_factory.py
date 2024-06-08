from abc import ABCMeta, abstractmethod, abstractstaticmethod, ABC

pattern_name = 'Chair Factory pattern'


class IChair(ABC):

    @abstractmethod
    def get_dimensions(self):
        ''''''


class BigChair(IChair):

    def get_dimensions(self):
        return "I'm a Big Chair"


class SmallChair(IChair):

    def get_dimensions(self):
        return "I'm a small Chair"


class ChairFactory():
    chairs = dict(big=BigChair(),
                  small=SmallChair())

    def get_chair(self, chair_type):
        try:
            return self.chairs[chair_type]
            raise chair_type
        except Exception as e:
            print(f'can not find a chair with this type {e}')


if __name__ == '__main__':
    print(f'{pattern_name} example:')

    chairFactory = ChairFactory()
    smallChair = chairFactory.get_chair('small')
    bigChair = chairFactory.get_chair('big')
    # medChair = chairFactory.get_chair('med')

    print(bigChair.__class__, bigChair.get_dimensions())
    print(smallChair.__class__, smallChair.get_dimensions())
