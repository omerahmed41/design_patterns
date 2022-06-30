from abc import ABCMeta, abstractstaticmethod


class IObserver(metaclass=ABCMeta):

    @abstractstaticmethod
    def notfiy(self, *args, **kwargs):
        ''''''
    
class IObserverable(metaclass=ABCMeta):

    @abstractstaticmethod
    def notfiy(self, *args, **kwargs):
        ''''''

    @abstractstaticmethod
    def subscribe():
        ''''''

    @abstractstaticmethod
    def un_subscribe():
        ''''''

class Subject(IObserverable):

    def __init__(self) -> None:
        self.observers = set()

    def subscribe(self, observer):
        self.observers.add(observer)
        print('new subscribe', len(self.observers))

    def un_subscribe(self, observer):
        print('new un_subscribe', len(self.observers))
        self.observers.remove(observer)

    def notfiy(self, *args, **kwargs):
        for observer in self.observers:
            observer.notfiy( *args, **kwargs)


class Observer(IObserver):

    def __init__(self, subject:IObserverable) -> None:
        subject.subscribe(self)

    def notfiy(self, *args, **kwargs):
        print(f'message recived:', args)

if __name__ == "__main__":
    subject = Subject()
    observer = Observer(subject)
    observer2 = Observer(subject)


    subject.notfiy("I'm happy and I know it ")
