from abc import ABCMeta, abstractstaticmethod

class ISMSManger(metaclass=ABCMeta):

    @abstractstaticmethod
    def send_sms():
        ''''''


class SMSManager(ISMSManger):

    susbcrip_package = None
    def __init__(self, package) -> None:
        self.susbcrip_package = package

    @staticmethod
    def send_sms():
        print('sms has been sent')

class ProxySMSManager(ISMSManger):

    counter = 0
    def __init__(self, cls:ISMSManger) -> None:
        self.cls = SMSManager(cls)

    def send_sms(self):
            if self.counter < 1:
                self.cls.send_sms()
                self.counter +=1
            else:
                print('package limit exsided')


if __name__ == '__main__':
    smsManger = ProxySMSManager('limited')

    smsManger.send_sms()
    smsManger.send_sms()
