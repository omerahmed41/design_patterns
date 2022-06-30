from abc import ABCMeta, abstractmethod, abstractstaticmethod

pattern_name = 'Singlton pattern'
print(f'{pattern_name} example:')


class IDBConection(metaclass=ABCMeta):

    @abstractstaticmethod
    def _connect():
            ''''''

class DBConnectionSinglton(IDBConection):
    __instance = None

    def __init__(self):
        if self.__instance:
            raise 'Connection to DB alread instaited'
        DBConnectionSinglton.__instance = self
        self._connect()

    @staticmethod
    def get_instanse():
        if DBConnectionSinglton.__instance is None:
            raise 'No connection setup yet'
        return DBConnectionSinglton.__instance


    def _connect(self):
        print('conecting ...')
        print('connected successfully.')


if __name__ == '__main__':

    dbConnection = DBConnectionSinglton()

    dbConnection1 = DBConnectionSinglton.get_instanse() # this one will fail

    print(dbConnection,dbConnection1)
    dbConnection1 = DBConnectionSinglton() # this one will fail
