# parent class
class Organism:
    name = 'Unknown'
    species = 'Unknown'
    legs = None
    arms = None
    dna = 'Sequence A'
    origin = 'Unknown'
    carbon_based = True

    def information(self):
        return '\nName: {}\nSpecies: {}\nLegs: {}\nArms: {}\nDna: {}\nOrigin: {}\nCarbon Based: {}'.format(self.name, self.species, self.legs, self.arms, self.dna, self.origin, self.carbon_based)


# child class instance
class Human(Organism):
    name = 'MacGuyver'
    species = 'Homosapien'
    legs = 2
    arms = 2
    origin = 'Earth'

    def ingenuity(self):
            return '\nCreates a deadly weapon using only a paper clip, chewing gum, and a roll of duct tape!'


# another child class instance
class Dog(Organism):
    name = 'Spot'
    species = 'Canine'
    legs = 4
    arms = None
    dna = 'Sequence B'
    origin = 'Earth'

    def bite(self):
        return '\nEmits a loud, menacing growl and bites down ferociously on its target!'


# another child class instance
class Bacterium(Organism):
    name = 'X'
    species = 'Bacteria'
    legs = None
    arms = None
    dna = 'Sequence C'
    origin = 'Mars'

    def replication(self):
        return '\nThe cells begin to devide and multiple into two seperate organisms!'
        

if __name__ == '__main__':
    human = Human()
    print(human.information())
    print(human.ingenuity())

    dog = Dog()
    print(dog.information())
    print(dog.bite())

    bacteria = Bacterium()
    print(bacteria.information())
    print(bacteria.replication())


