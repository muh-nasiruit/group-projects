from abc import ABC, abstractmethod

class Deals(ABC):
    
    def add(self):
        pass
    
  
class Deal1(Deals):
    
    def add1(self):
        n = self.chBUF.get() +1
        self.chBUF.set(n)        
    

    
class Deal2(Deals):
    
    def add2(self):
        n = self.veg.get() +1
        self.veg.set(n)   

    
class Deal3(Deals):
    
    def add3(self):
        n = self.chTPT.get() +1
        self.chTPT.set(n) 
    

























