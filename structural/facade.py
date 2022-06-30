

class Lights():

    def light_on(self):
        print('Light ON')

    def light_off(self):
        print('Light Off')
class Smoke():

    def smoke_on(self):
        print('Smoke ON')

    def smoke_off(self):
        print('Smoke Off')
    
class FireAlertFacade():

    def __init__(self) -> None:
        self.lights = Lights()
        self.smoke = Smoke()

    def alert(self):
        self.lights.light_on()
        self.smoke.smoke_on()

    def alert_off(self):
        self.lights.light_off()
        self.smoke.smoke_off()

if __name__ == '__main__':
    alert = FireAlertFacade()
    alert.alert()
    alert.alert_off()
