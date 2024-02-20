# Assumption: No two Phones have the same price in our store. => Key is Phone's price
from enum import Enum

class BST:
    # Binary Search Tree
    def __init__(self) -> None:
        self.root = None # Node() # pointer to root's node of the BST
        self.no_of_phones = 0 # the total number of Phones

    def __str__(self) -> str:
        return f'Root node = {self.root}, Total number of Phones in the store = {self.no_of_phones}'


class Phone:
    def __init__(self) -> None:
        self.name = '' # type of phone
        self.price = 0 # price
        self.quantity = 0 # Quantity in stock

    def __init__(self, name, price, quantity) -> None:
        self.name = name # type of phone
        self.price = price # price
        self.quantity = quantity # Quantity in stock

    def __str__(self) -> str:
        return f'Phone name : {self.name}, Price : {self.price}, Quantity left in stock : {self.quantity}'


class Node:
    def __init__(self) -> None:
        self.item = None # Phone()
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return f'Phone node = {self.item}'


def createEmptyBST ():
    # This function creates an empty BST, with root pointing to null initially, and returns this instance of BST class.
    return BST()

def insert (node, key_node, success=True):
    if node == None:
        return key_node, success

    if node.item.price == key_node.item.price:
        print("Duplicate")
        return node, False
    elif node.item.price < key_node.item.price:
        # If phone's price is less than current nodes price: Insert the node at right subtree
        if node.right == None:
            node.right = key_node
        else:
            node.right, success = insert(node.right, key_node, success)
    else:
        # If phone's price is less than current nodes price: Insert the node at left subtree
        if node.left == None:
            node.left = key_node
        else:
            node.left, success = insert(node.left, key_node, success)

    return node, success

def insertIntoBST (bst, phone):
    # This function inserts a phone record (as per the price of {phone} variable) at the appropriate position in the BST {bst}, and then returns the same BST (not a copy).

    key_node = Node()
    key_node.item = phone

    bst.root, success = insert(bst.root, key_node)

    if success:
        bst.no_of_phones += 1
    return bst

def findInBST (bst, cost): 
    # This function finds whether there exists a Phone of price {cost}, and if there does, return that Phone variable, if not, return null.
    pass

def findMaxPrice (bst):
    # This function returns the Phone with maximum price amongst all phones available in the store.
    pass

def findMinPrice (bst):
    # This function returns the Phone with minimum price amongst all phones available in the store.
    pass

def findSecondMaxPrice (bst): #findSecondMinPrice (bst) :
    # This function returns the Phone with second highest price amongst all phones available in the store.
    pass

def listAllPrices (bst) :
    # Generate a linked list of prices of all Phones in increasing order, and return the same. You will have to implement all the required functionality of the Linked List data structure independently for this function. Once the Linked List is created, print it in the o/p file.
    pass

def modifyQtyInStock (bst, name, price, new_qty) :
    # Using this function, you should find the entry in the BST {bst} having {name} and {price} and set its quantity left in stock field to new_qty.
    pass

def deleteFromBST (bst, name, price) :
    # This function is responsible for deleting a Phone entry from the BST, having same name and price as {name} and {price} respectively.
    pass

def totalBooks (bst) :
    # This function should return a pair of integers, first being the total different types of Phones currently in the store, and the second integer being the total number of Phones currently in stock in the store i.e sum of quantity left in stock field of each Phone entry in the BST.
    pass


# Enum type of choices
class Input(Enum):
    FILE_INPUT = 1
    COMMAND_INPUT = 2
    EXIT = 6


def get_input_from_user():
    print("1. File Input")
    print("2. Command line Input")
    print("3. Search Input")
    print("4. Delete Input")
    print("5. Display Input")
    print("6. Exit")
    option = int(input("Enter your choice: "))
    return option


def command_prompt():
    # Get the choice from user

    bst = createEmptyBST()

    while (True):
        # Loop till the user enters valid input               
        option = get_input_from_user()

        # TODO: Validate option

        if option == Input.FILE_INPUT.value:
            # File input: (Input and Output file names should be taken from user)
            #     3
            #     Samsung Galaxy M34, 17950, 20
            #     OnePlus Nord CE 3, 21999, 10
            #     Apple Iphone 14, 65999, 50
            pass
        elif option == Input.COMMAND_INPUT.value:
            no_of_entries = int(input("Enter the number of entries: "))
            print("Enter the details is below format:\n<PHONE_NAME>, <PRICE>, <QUANTITY>")
            for _ in range(no_of_entries):
                item = input("Enter the phone details: ").split(', ')
                phone = Phone(item[0], int(item[1]), int(item[2]))
                bst = insertIntoBST(bst, phone)
        elif option == Input.EXIT.value:
            return


if __name__ == "__main__": 
    command_prompt()
