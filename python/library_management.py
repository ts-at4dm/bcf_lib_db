import json

class Library_Management():
    def __init__(self, inventory, filename="mappings.json"):
        self.inventory = inventory
        self.filename = filename
        self.inventory = self.load_from_file()
        
    def get_books(self):
        return list(self.inventory.keys())
        pass
    
    def add_book(self, book):
        if book not in self.inventory:
            self.inventory[] = {}
            self.save_to_file()
            
    def delete_book(self, book):
        pass
            
    def save_to_file(self):
        with open(self.filename, "w") as file:
            json.dump(self.inventory, file, indent=2)
            
    def load_from_file(self):
        with open(self.filename, "r") as file:
            return json.load(file)