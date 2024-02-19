# Assumption: No two Phones have the same price in our store. => Key is Phone's price

class BST:
    # Binary Search Tree
    def __init__(self) -> None:
        self.root = None # Node() # pointer to root's node of the BST
        self.no_of_phones = 0 # the total number of Phones

    def __str__(self) -> str:
        print("Root node = ", self.root)
        print("Total number of Phones in the store = ", self.no_of_phones)


class Phone:
    def __init__(self) -> None:
        self.name = '' # type of phone
        self.price = 0 # price
        self.quantity = 0 # Quantity in stock

    def __str__(self) -> str:
        print("Phone name : ", self.name, ", Price : ", self.price, ", Quantity left in stock : ", self.quantity)


class Node:
    def __init__(self) -> None:
        item = None # Phone()

    def __str__(self) -> str:
        print("TODO")


def command_prompt():
    # Get the choice from user

    while (True):
        # Loop till the user enters valid input               
        option = input("Enter your value: ")

        # TODO: Validate option

        if option == 'INPUT_FILE':
            # File input: (Input and Output file names should be taken from user)
            #     3
            #     Samsung Galaxy M34, 17950, 20
            #     OnePlus Nord CE 3, 21999, 10
            #     Apple Iphone 14, 65999, 50
            pass
        elif option == 'EXIT':
            return


if __name__ == "__main__": 
    command_prompt()
