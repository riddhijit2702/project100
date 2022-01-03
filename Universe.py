class Universe(object) :
    def __init__(self,star,blackhole,systems,planets=None):
        self.star = star
        self.blackhole = blackhole
        self.systems = systems
        self.planets = planets
        
    def setStar(self,systems,planets):
        self.planets[systems]=planets
    def getStar(self,systems):
        return self.planets[systems]
    


milkdromeda = Universe(anything,saggiritus,everything,earth)

print(milkdromeda)
