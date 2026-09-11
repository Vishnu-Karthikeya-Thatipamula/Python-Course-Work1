'''
class whatsappv1:
    def status(self):
        print("You can upload the ststus for 24hrs")
class whatsappv2(whatsappv1):
    def status(self):
        super().status()
        print("You can add music and you can react")
a = whatsappv1()
a.status()
b = whatsappv2()
b.status()


class whatsappv1:
    def status(self):
        print("You can upload the ststus for 24hrs")
class whatsappv2:
    def status(self):
        print("You can add music and you can react")
class whatsappv3( whatsappv1,whatsappv2):
    def status(self):
        whatsappv1.status(self)
        whatsappv2.status(self)
        print("You can add to thr cross platforms")

a = whatsappv1()
a.status()
b = whatsappv2()
b.status()
c = whatsappv3()
c.status()
'''  

class Hotstar:
    def __init__(self, name):
        print(f'Welcome to the hotstar, {name} ----------------------------')
    def auth(self):
        print("You can login/register")
    def dashboard(self):
        print("You can access the dashboard")
    def search(self):
        print("You can search")
    def history(self):
        print("You can see the history")
    def playercontrollers(self):
        print("You have the player controller")
    def ads(self):
        print("You can see ads")
    def access(self):
        print("You have limited access")
    def quality(self):
        print("You have the limitied access")
    def devices(self):
        print("Single Login")
    def download(self):
        print("You cannot download")

class premiumhotstar(Hotstar):
    def __init__(self, name):
        print(f"Welcome to Premiumhotstar, {name}-----------------")
    def ads(self):
        print("You cannot see ads")
    def access(self):
        print("You have unlimited access")
    def quality(self):
        print("You have the higher Quality")
    def devices(self):
        print("Multiple Login")
    def download(self):
        print("You can download")

Vishnu = Hotstar('Vishnu')
Vishnu.auth
Vishnu.access()
Vishnu.ads()
Vishnu.dashboard()
Vishnu.devices()
Vishnu.download()
Vishnu.history()
Vishnu.playercontrollers()
Vishnu.quality()
Vishnu.search()

Karthikeya = premiumhotstar('Karthikeya')
Karthikeya.ads()
Karthikeya.quality()
Karthikeya.access()
Karthikeya.download()
Karthikeya.devices()




