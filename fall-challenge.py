import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

class item:
    def __init__(self, item_details : str):
        """
        Initializing item
        """
        self.action_id, self.action_type, self.delta_0, self.delta_1, self.delta_2, self.delta_3, self.price, self.tome_index, self.tax_count, self.castable, self.repeatable = item_details.split()
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
        self.total_delta = ( self.delta_0 * 1 ) + ( self.delta_1 * 2 ) + ( self.delta_2 * 3 ) + ( self.delta_3 * 4 ) 


class witch:
    def __init__(self, witch_details: str):
        """
        Initializing witch
        """
        self.inv_0, self.inv_1, self.inv_2, self.inv_3, self.score = [int(j) for j in witch_details.split()]
        self.total_inv = (self.inv_0 * 1) + (self.inv_1 * 2) + (self.inv_2 * 3) + (self.inv_3 * 4) 

    def find_best_item(self, list_of_items : item):
        """
        To search for best item to create
        """
        best_price = -1
        best_item = list_of_items[0]
        for item in list_of_items:
            if self.total_inv > item.total_delta and item.price > best_price:
                if item.delta_0 < self.inv_0 and item.delta_0 < self.inv_0 and item.delta_0 < self.inv_0 and item.delta_0 < self.inv_0:
                    best_price = item.price
                    best_item = item
        if best_price == -1:
            return None
        else:
            return best_item




# game loop

while True:
    action_count = int(input())  # the number of spells and recipes in play
    list_of_items = []

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

        list_of_items.append(item(input()))

    # for i in range(2):
    #     inv_0: tier-0 ingredients in inventory
    #     score: amount of rupees
    #     inv_0, inv_1, inv_2, inv_3, score = [int(j) for j in input().split()]

    me = witch(input())
    opponent = witch(input())
    best_item = me.find_best_item(list_of_items)

    print("All details in debug", list_of_items[0].action_id, me.score, opponent.score, file=sys.stderr, flush=True)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)


    # in the first league: BREW <id> | WAIT; later: BREW <id> | CAST <id> [<times>] | LEARN <id> | REST | WAIT
    if best_item != None:
        print(f"BREW {best_item.action_id}")
    else:
        print("WAIT")
