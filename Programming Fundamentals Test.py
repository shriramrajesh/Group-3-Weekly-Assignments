class Pet:
    def __init__(self, species=None, name=""):
        self.species=species
        self.name=name
        if(self.species!="dog" and self.species!="cat" and self.species!="horse" and self.species!= "hamster"):
            print("Error")
    def __str__(self):
        if(len(self.name)!=0):
            return ("Species of %s:named %s" %(self.species,self.name))
        else:
            return ("Specis of %s: unamed" %(self.species))
class Dog(Pet):
    def __init__(self,species="dog",name="",chases="cats"):
        self.chases=chases
        Pet.__init__(self,species,name)
    def __str__(self):
        if (len(self.name)!=0):
            return ("Species of: Dog, named %s, chases %s" %(self.name,self.chases))
        else:
            return ("Species of: Dog, unnamed,chases %s" % (self.chases))
class Cat(Pet):
    def __init__(self,species="cat",name="",hates="dogs"):
        self.hates=hates
        Pet.__init__(self,species,name)
    def __str__(self):
        if (len(self.name)!=0):
            return ("Species of: Cat, named %s, hates %s" %(self.name,self.hates))
        else:
            return ("Species of: Dog, unnamed,chases %s" % (self.hates))

d1= Dog("dog","Sammy","Felix")
d2= Dog("dog","Frankie","Mr. Kat")
d3= Dog("dog","Louis","Sprinkles")
c1= Cat("cat","Felix", "Sammy")
c2=Cat("cat", "Mr. Kat","Frankie")
d={}
d["dogs"]=[d1,d2,d3]
d["cats"]=[c1,c2]
print(d["dogs"][0],d["dogs"][1],d["dogs"][2],d["cats"][0],d["cats"][1])
