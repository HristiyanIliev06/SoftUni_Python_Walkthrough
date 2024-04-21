class Catalogue:
    products = []
    flp = []
    sproducts = []
    
    def __init__ (self, name):
        self.name = name
        
    def add_product(self, product_name:str):
        self.products.append(product_name)
        self.sproducts = sorted(self.products)
        
    def get_by_letter(self, first_letter:str):
        for product in self.products:
           if product[0]==first_letter:
               self.flp.append(product)
        return self.flp
    
    def __repr__(self):
       return "Items in the "+self.name+" catalogue:\n"+'\n'.join(self.sproducts)
        
catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
      