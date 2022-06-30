from abc import ABCMeta, abstractstaticmethod

class IFightingStyle(metaclass=ABCMeta):

    @abstractstaticmethod
    def fight():
        ''''''


class DanceFight(IFightingStyle):

    def fight():
        print('Use Dance fighting style with power 300')


class LazyFight(IFightingStyle):

    def fight():
        print('Use Lazy fighting style with power 200')



class KunfoFight(IFightingStyle):

    def fight():
        print('Use Kunfo fighting style with power 250')
    

class IFighter(metaclass=ABCMeta):

    @abstractstaticmethod
    def attack():
        ''''''
    
class Fighter(IFighter):
    fight_style = None
    name = None


    def __init__(self, name, fight_style:IFightingStyle):
        self.fight_style = fight_style
        self.name = name


    def attack(self):
        print(f'{self.name}:')
        self.fight_style.fight()

if __name__ == '__main__':
    fighter1 = Fighter('fighter1',KunfoFight)
    fighter2 = Fighter('fighter2',DanceFight)

    fighter1.attack()
    fighter2.attack()
