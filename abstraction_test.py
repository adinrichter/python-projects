
from abc import ABC, abstractmethod

class website(ABC):
    def buyAccess(self, time):
        print('Thank you, you now have access. Your subscription will end in {} days'.format(time))
    @abstractmethod
    def useAccess(self, time):
        pass

class videos(website):
    def useAccess(self, time):
        print('You now have access for {} days.'.format(time))


user = videos()

user.buyAccess('30')
user.useAccess('30')
