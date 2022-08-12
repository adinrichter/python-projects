# creates a class to store private information
class Protected:
    def __init__(self):
        # creates protected and private variables
        self._protectedInfo = 'secret information'
        self.__privateInfo = 'even more secret information'

    def getPrivate(self):
        return self.__privateInfo

    def setPrivate(self, input):
        self.__privateInfo = input
        


usingSecret = Protected()

print(usingSecret._protectedInfo)
usingSecret._protectedInfo = 'not so secret anymore'
print(usingSecret._protectedInfo)

print(usingSecret.getPrivate())
usingSecret.setPrivate('not even you are safe')
print(usingSecret.getPrivate())

