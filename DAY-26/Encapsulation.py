"""
pub -> inclass, childclass, outclass
pri -> inclass
pro -> inclass , childclass, outclass(not recommended)
"""
class Instagram:
    def __init__(self, username, password):
        self.username = username
        self.__password = password
        self._post = []
    def getpassword(self):
        return self.__password

    def setpassword(self, newpassword):
            self.__password  = newpassword

    @property
    def accesspost(self):
        return self._post


    @accesspost.setter
    def accesspost(self, newpost):
         self._post.append(newpost)
    
Vishnu = Instagram('Vishnu', '123456')
print(Vishnu.username)
print(Vishnu.getpassword())
print(Vishnu.accesspost)
Vishnu.username = 'Vishnu_123'
print(Vishnu.username)
Vishnu.setpassword('Vishnu@134')
print(Vishnu.getpassword())
Vishnu.accesspost = 'python intro'
Vishnu.accesspost = 'strings'
Vishnu.accesspost = 'project'
print(Vishnu.accesspost)