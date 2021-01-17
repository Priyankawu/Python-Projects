

    
            
#Parent class
class Bread:
    cuisine = "Human"
    flour=""
    shape=""
    equipment=""

    def how_to_make(self):
        msg = "Prepare dough. Give it shape. Cook on the equipment."
        print(msg)
    def how_to_eat(self):
        msg = "Be grateful for the good food and enjoy!"
        print(msg)
    
#Child class 1
class Roti(Bread):
    cuisine = "Indian"
    flour= "Whole Wheat"
    shape= "Round"
    seasoning="salt"
    equipment="tawa, chakla, belan"
    condiments = "subji, chutney, butter"
    def how_to_make(self):
        msg = "Prepare tight dough by adding water and salt to the flour. Make small balls. \
            Roll into round thin shape."
    def how_to_cook(self):
        msg = "Heat tawa. Place roti on the tawa and cook on both sides."
        print(msg)


#Child class 2
class Parantha(Bread):
    cuisine = "Indian"
    flour = "Half whole wheat, half all-purpose flour"
    shape = "round"
    seasoning = "salt"
    filling = "spice and boiled potato mixture"
    tawa_spread = "butter"
    equipment = "tawa, chakla, belan"

    def how_to_make(self):
        msg = "Prepare tight dough by adding salt and water to the flours. Make small balls.\
               Add filling in the middle of the balls. Roll flat into round shape."
        print(msg)
    def how_to_cook(self):
         msg = "Heat tawa. Place parantha on the tawa. Spread butter on it. Cook on both sides."
         print(msg)

br = Bread()
br.how_to_eat()
    
roti = Roti()
roti.how_to_cook()

parantha = Parantha()
parantha.how_to_make()
parantha.how_to_eat()
    
