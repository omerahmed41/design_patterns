from abc import ABCMeta, abstractmethod, abstractstaticmethod
from .import chair_factory, table_factory



pattern_name = 'Abstract pattern'


class IFurniture(metaclass=ABCMeta):

    @abstractstaticmethod
    def get_furniture(self, type, size):
           '''''' 


class FurnitureFactory(IFurniture):
    
    def get_furniture(self, type, size):
        try:
            if type == 'table':
                return table_factory.TableFactory().get_table(size)
            elif type == 'chair':
                return chair_factory.ChairFactory().get_chair(size)
            raise (type, size)
        except Exception as e:
            print(f'can not find a frunituer with this type {e}')
 


if __name__ == '__main__':
    print(f'{pattern_name} example:')

    furnitureFactory = FurnitureFactory()
    smallTable = furnitureFactory.get_furniture('table', 'small')
    bigChair = furnitureFactory.get_furniture('chair', 'big')
    # medChair = chairFactory.get_chair('med')


    print(bigChair.__class__, bigChair.get_dimensions())
    print(smallTable.__class__, smallTable.get_dimensions())
