import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

class action(object):
    def __init__(self, action_details : str):
        """
        Initializing brew
        """
        self.action_id, self.action_type, self.delta_0, self.delta_1, self.delta_2, self.delta_3, \
        self.price, self.tome_index, self.tax_count, self.castable, self.repeatable = action_details.split()
        self.action_id = int(self.action_id)
        self.delta_0 = int(self.delta_0)
        self.delta_1 = int(self.delta_1)
        self.delta_2 = int(self.delta_2)
        self.delta_3 = int(self.delta_3)
        self.price = int(self.price)
        self.tome_index = int(self.tome_index)
        self.tax_count = int(self.tax_count)
        self.castable = self.castable != "0"
        self.repeatable = self.repeatable != "0"
        self.action_difficulty = abs(self.delta_0*1 + self.delta_1*2 + self.delta_2*3 + self.delta_3*4)
        self.action_inv_need = abs(self.delta_0 + self.delta_1 + self.delta_2 + self.delta_3)



class witch(action):

    def __init__(self):
        """
        Initialize witch
        """
        self.inv_0 = self.inv_1 = self.inv_2 = self.inv_3 = self.score = 0
        self.spells : action = []
        self.brews : action = []
        self.total_inv : int = self.total_inventory()

    def total_inventory(self) -> int:
        return (self.inv_0 + self.inv_1 + self.inv_2 + self.inv_3)
    
    def inventory_score_details(self, _witch_details : str):
        """
        Initializing witch inventory
        """
        self.inv_0, self.inv_1, self.inv_2, self.inv_3, self.score = [int(j) for j in _witch_details.split()]
        self.total_inv = self.total_inventory()
    
    def add_action(self, _action : action):
        """
        Adding actions for witch
        """
        #print(f"Action type {_action.action_type}", file=sys.stderr, flush=True)
        if _action.action_type == "CAST":
            self.spells.append(_action)
        elif _action.action_type == "BREW":
            self.brews.append(_action)
        

    def find_easiest_brew(self) -> action:
        """
        To search for best brew to create
        """
        
        easiest_brew = self.brews[0]
        for brew in self.brews:
            if brew.action_difficulty < easiest_brew.action_difficulty:
                easiest_brew = brew
        return easiest_brew
    
    def is_brew_possible(self, brew: action) -> bool:
        return (brew.delta_0 + self.inv_0 >= 0) and (brew.delta_1 + self.inv_1 >= 0) and \
              (brew.delta_2 + self.inv_2 >= 0) and (brew.delta_3 + self.inv_3 >= 0)

    def is_cast_possible(self, cast : action) -> bool:
        return (cast.delta_0 + self.inv_0 >= 0) and (cast.delta_1 + self.inv_1 >= 0) and \
              (cast.delta_2 + self.inv_2 >= 0) and (cast.delta_3 + self.inv_3 >= 0) and ((self.total_inv + cast.action_inv_need) <= 10) \
                  and cast.castable

    def is_rest_needed(self) -> bool:
        cast_available = 0
        for spell in self.spells:
            if spell.castable:
                cast_available += 1
        return cast_available == 0


    def missing_brew_inv(self, brew : action) -> str:
        """
        docstring
        """
        pass
 
        missing_3 = brew.delta_3 + self.inv_3
        missing_2 = brew.delta_2 + self.inv_2 + (missing_3 if missing_3 < 0 else 0)
        missing_1 = brew.delta_1 + self.inv_1 + (missing_2 if missing_2 < 0 else 0)
        missing_0 = brew.delta_0 + self.inv_0 + (missing_1 if missing_1 < 0 else 0)
        print(f"{missing_3}, {missing_2}, {missing_1}, {missing_0}", file=sys.stderr, flush=True)
         
        if (missing_0 < 0) and self.is_cast_possible(self.spells[0]):
            return f"CAST {self.spells[0].action_id}"
        if (missing_1 < 0) and self.is_cast_possible(self.spells[1]):
            return f"CAST {self.spells[1].action_id}"
        if (missing_2 < 0) and self.is_cast_possible(self.spells[2]):
            return f"CAST {self.spells[2].action_id}"
        if (missing_3 < 0) and self.is_cast_possible(self.spells[3]):
            return f"CAST {self.spells[3].action_id}"
        return "REST"
    

    def get_action(self):

        easiest_brew = self.find_easiest_brew()
        print(f"Easiest brew - {easiest_brew.action_id}", file=sys.stderr, flush=True)
        if self.is_brew_possible(easiest_brew):
            print(f"BREW {easiest_brew.action_id}")
        elif not self.is_rest_needed():
            print(f"{self.missing_brew_inv(easiest_brew)}")
        elif self.is_rest_needed():
            print("REST")
        else:
            print("WAIT")




# game loop

while True:
    action_count = int(input())  # the number of spells and recipes in play
    me = witch()
    opponent = witch()

    for i in range(action_count):
        # action_id: the unique ID of this spell or recipe
        # action_type: in the first league: BREW; later: CAST, OPPONENT_CAST, LEARN, BREW
        # delta_0: tier-0 ingredient change
        # delta_1: tier-1 ingredient change
        # delta_2: tier-2 ingredient change
        # delta_3: tier-3 ingredient change
        # price: the price in rupees if this is a potion
        # tome_index: in the first two leagues: always 0; later: the index in the tome if this is a tome spell, equal to the read-ahead tax
        # tax_count: in the first two leagues: always 0; later: the amount of taxed tier-0 ingredients you gain from learning this spell
        # castable: in the first league: always 0; later: 1 if this is a castable player spell
        # repeatable: for the first two leagues: always 0; later: 1 if this is a repeatable player spell
        # action_id, action_type, delta_0, delta_1, delta_2, delta_3, price, tome_index, tax_count, castable, repeatable = input().split()
        # action_id = int(action_id)
        # delta_0 = int(delta_0)
        # delta_1 = int(delta_1)
        # delta_2 = int(delta_2)
        # delta_3 = int(delta_3)
        # price = int(price)
        # tome_index = int(tome_index)
        # tax_count = int(tax_count)
        # castable = castable != "0"
        # repeatable = repeatable != "0"

        me.add_action(action(input()))

    # for i in range(2):
    #     inv_0: tier-0 ingredients in inventory
    #     score: amount of rupees
    #     inv_0, inv_1, inv_2, inv_3, score = [int(j) for j in input().split()]

    me.inventory_score_details(input())
    opponent.inventory_score_details(input())

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    # in the first league: BREW <id> | WAIT; later: BREW <id> | CAST <id> [<times>] | LEARN <id> | REST | WAIT
    me.get_action()    
