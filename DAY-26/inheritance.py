#Simple Inheritance
class Whatsappv1:
    def message(self):
        print("You can send a message")

class whatsappv2(Whatsappv1):
    def status(self):
        print("U can kepp ur status for 24 hours")

class whatsappv3(whatsappv2, Whatsappv1):
    def group(self):
        print("U can talk with multiple people at once")

class whatsappv4(Whatsappv1):
    def community(self):
        print("U can have multiple groups")

class whatsappv5(whatsappv3, whatsappv4, whatsappv2, Whatsappv1):
    def channels(self):
        print("You can post regular with huge crowd")

Vishnu = Whatsappv1()
Vishnu.message()

Teja = whatsappv2()
Teja.message()
Teja.status()

#Multi-Level
Dinesh = whatsappv3()
Dinesh.group()
Dinesh.message()

#Multiple Inheritance
Dileep = whatsappv5()
Dileep.group()
Dileep.status()
Dileep.message()
Dileep.channels()
Dileep.community()

#Hiearchy Inheritance
