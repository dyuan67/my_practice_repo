class Student:
    def __init__(self, fname, lname, id, energy_level = 10):
        self.fname = fname
        self.lname = lname
        self.id = id
        self.energy_level = energy_level
            # If you want the user to choose energy level, just initialize it to energy_level 
                # Can set it to an inital value also
            # But if you want it set at 10 regardless of value they put, set it equal to 10
                # Or don't let them choose a value and just have it set to 10,
                    #self.energy_level = 10 (don't include in inital list)
    
    def __str__(self):
        return f"{self.lname}:{self.id}"
    
    def greeting(self):
        print("Hello, how are you?")
    
    def take_exam(self):
        self.energy_level-=1
    
    def get_energy_level(self):
        return self.energy_level