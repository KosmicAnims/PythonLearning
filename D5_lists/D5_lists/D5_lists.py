#random bird calass lol
class bird:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def fly(self):
        return f"{self.name} is flying!"

    def sing(self):
        return f"{self.name} is singing!"

a = bird("sayo","sparo")
print(a.fly())

#list lesson below
lis_a = []
lis_b = [1, 2, 3, 4, 5, 6,]
lenb = lis_b.__len__()
print(lis_b[0], lis_b[lenb//2], lis_b[lenb-1])

wakes_early = bool()
mixed = ['name', 1, wakes_early]

_comp = ['Google','facebook','insta','youtube']
print(_comp)
print(_comp[0],_comp[(_comp.__len__())//2],_comp[(_comp.__len__()) - 1])

_comp[1] = 'asesprite'
print(_comp)

_comp.append('ITcomp')
_comp[3] = _comp[3].upper()

_comp.insert(_comp.__len__()//2, 'ITdynamic')

_comp.index('Google') != -1
# I understand it now
#Tuples - simple lists
tlp = tuple()
tlp1 = (11,22,33,44,55)
brothers = ('kane','tiin')
sisters = ('liora','vera')
sibilings = brothers + sisters

print(sibilings,'you have this many siblings:', len(sibilings) )
sibilings = list(sibilings)
family_members = sibilings
family_members.insert(0,"unknown parents")
print(family_members)

 
