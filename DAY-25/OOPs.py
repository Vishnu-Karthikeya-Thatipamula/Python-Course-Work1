class Flipkart:
    discount = 30
    @classmethod
    def updateddiscount(cls):
        cls.discount = 40
        print("Updated Discount",cls.discount)
    @staticmethod
    def banner():
        print(f"{Flipkart.discount}% discount is on, grab before it ends")


    def info(self, name, mobile, address):
        self.name = name
        self.mobile = mobile
        self.address = address


    

Teja = Flipkart()
Teja.info('Teja',555555555,'HYD')
Teja.updateddiscount()
Teja.banner()
Dinesh = Flipkart()
Dinesh.info('Dinesh',984455675, 'CH')
Dinesh.updateddiscount()
Dinesh.banner()
Vishnu = Flipkart()
Vishnu.info('Vishnu',7989646678,'DLH')
Vishnu.updateddiscount()
Vishnu.banner()

