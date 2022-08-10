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
    name = 'Steve Jobs'
    species = 'Human'
    legs = 2
    arms = 2
    origin = 'Earth'

    def information(self):
            return '\nCreated the company computer company Apple.'

        

if __name__ == '__main__':
    human = Human()
    print(human.information())


