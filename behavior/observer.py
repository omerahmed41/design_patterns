from abc import ABCMeta, abstractstaticmethod


class IObserver(metaclass=ABCMeta):

    @abstractstaticmethod
    def notify(self, *args, **kwargs):
        ''''''
    
class IObserverable(metaclass=ABCMeta):

    @abstractstaticmethod
    def notify(self, *args, **kwargs):
        ''''''

    @abstractstaticmethod
    def subscribe(observer):
        ''''''

    @abstractstaticmethod
    def un_subscribe(observer):
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

    def notify(self, *args, **kwargs):
        for observer in self.observers:
            observer.notify(*args, **kwargs)


class Observer(IObserver):

    def __init__(self, subject:IObserverable) -> None:
        subject.subscribe(self)

    def notify(self, *args, **kwargs):
        print(f'message recived:', args)

if __name__ == "__main__":
    subject = Subject()
    observer = Observer(subject)
    observer2 = Observer(subject)


    subject.notify("I'm happy and I know it ")
