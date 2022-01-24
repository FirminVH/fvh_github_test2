class persoon:

    pi = 3.1415

    def __init__(self, naam, leeftijd):
        self.naam = naam
        self.leeftijd = leeftijd
        self.email = naam+"."+"student@syntrapxl.be"

    def print_persoon_info(self):
        print("Naam: {} is {} jaar oud".format(p1.naam, p1.leeftijd))


p1=persoon("Firmin", 54)
p1.print_persoon_info() #op instantie van Persoon
persoon.print_persoon_info(p1) #op de klasse met als parameter instantie p1
print(p1.pi)

persoon_dict = p1.__dict__
print(persoon_dict)