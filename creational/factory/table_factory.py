from abc import ABCMeta, abstractmethod, abstractstaticmethod, ABC

pattern_name = 'Table factory'


class ITable(ABC):

    @abstractmethod
    def get_dimensions(self):
        ''''''


class BigTable(ITable):

    def get_dimensions(self):
        return "I'm a Big Table"


class SmallTable(ITable):

    def get_dimensions(self):
        return "I'm a small Table"


class TableFactory:
    chairs = dict(big=BigTable(),
                  small=SmallTable(),
                  )

    def get_table(self, table_type):
        try:
            if self.chairs.get(table_type):
                return self.chairs[table_type]
            raise table_type
        except Exception as e:
            print(f'can not find a table with this type {e}')


if __name__ == '__main__':
    print(f'{pattern_name} example:')

    tableFactory = TableFactory()
    smallTable = tableFactory.get_table('small')
    bigTable = tableFactory.get_table('big')
    # medChair = chairFactory.get_chair('med')

    print(bigTable.__class__, bigTable.get_dimensions())
    print(smallTable.__class__, smallTable.get_dimensions())
