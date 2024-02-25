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

def insertIntoBST (bst, phone):
    # This function inserts a phone record (as per the price of {phone} variable) at the appropriate position in the BST {bst}, and then returns the same BST (not a copy).

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

    key_node = Node()
    key_node.item = phone

    bst.root, success = insert(bst.root, key_node)

    if success:
        bst.no_of_phones += 1

    return bst

def findInBST (bst, cost): 
    # This function finds whether there exists a Phone of price {cost}, and if there does, return that Phone variable, if not, return null.

    def search(node, key):
        # If node == None, key is not present in BST
        if node is None:
            return None

        # Key found
        if node.item.price == key:
            return node.item

        # If key not found, traverse left/right
        if node.item.price < key:
            # Key is greater than node's key: search right subtree
            if node.right == None:
                return None
            else:
                return search(node.right, key)
        else:
            # Key is lesser than node's key: search left subtree
            if node.left == None:
                return None
            else:
                return search(node.left, key)

    return search(bst.root, cost)

def search_max(node):
    if node.right == None:
        return node
    else:
        return search_max(node.right)

def findMaxPrice (bst):
    # This function returns the Phone with maximum price amongst all phones available in the store.

    if bst.root == None:
        print("No records in BST")
        return None

    return search_max(bst.root).item

def search_min(node):
    if node.left == None:
        return node
    else:
        return search_min(node.left)

def findMinPrice (bst):
    # This function returns the Phone with minimum price amongst all phones available in the store.

    if bst.root == None:
        print("No records in BST")
        return None

    return search_min(bst.root).item

def findSecondMaxPrice (bst):
    # This function returns the Phone with second highest price amongst all phones available in the store.
    if bst.root == None:
        print("No records in BST")
        return None

    if bst.root.right == None and bst.root.left == None:
        # Only one node in this BST. No second largest price.
        print("Only one record is found in the BST, hence second costliest is None")
        return None

    # At this point, BST definitely has more than one phone record
    # Second max element is in left sub tree
    if bst.root.right == None:
        return search_max(bst.root.left).item
    
    # Second max element may be root or on right sub tree of root
    if bst.root.right != None:
        first_largest = bst.root.right
        second_largest = bst.root

        # Traverse till the last right subtree and get largest and second largest nodes in the right links
        while(first_largest.right != None):
            second_largest = first_largest
            first_largest = first_largest.right

        # If the largest element has left subtree, then the second largest element will be the largest element in left subtree
        if first_largest.left != None:
            second_largest = search_max(first_largest.left)

    return second_largest.item

def findSecondMinPrice (bst) :
    # This function returns the Phone with second lowest price amongst all phones available in the store.
    if bst.root == None:
        print("No records in BST")
        return None

    if bst.root.right == None and bst.root.left == None:
        # Only one node in this BST. No second lowest price.
        print("Only one record is found in the BST, hence second cheapest phone is None")
        return None

    # At this point, BST definitely has more than one phone record
    # Second min element is in right sub tree
    if bst.root.left == None:
        return search_min(bst.root.right).item
    
    # Second min element may be root or on left sub tree of root
    if bst.root.left != None:
        first_lowest = bst.root.left
        second_lowest = bst.root

        # Traverse till the last left subtree and get lowest and second lowest nodes in the left links
        while(first_lowest.left != None):
            second_lowest = first_lowest
            first_lowest = first_lowest.left

        # If the lowest element has right subtree, then the second lowest element will be the lowest element in right subtree
        if first_lowest.right != None:
            second_lowest = search_min(first_lowest.right)

    return second_lowest.item

def listAllPrices (bst) :
    # Generate a linked list of prices of all Phones in increasing order, and return the same. You will have to implement all the required functionality of the Linked List data structure independently for this function. Once the Linked List is created, print it in the o/p file.
    pass

def modifyQtyInStock (bst, name, price, new_qty) :
    # Using this function, you should find the entry in the BST {bst} having {name} and {price} and set its quantity left in stock field to new_qty.
    pass

def deleteFromBST (bst, name, price) :
    # This function is responsible for deleting a Phone entry from the BST, having same name and price as {name} and {price} respectively.
    #TO DO need to be tested

    def delete(node, name, price, success=True):
        if node is None:
            print("Node is not found in the BST")
            return node, False
        
        if price < node.item.price:                                 #Check if price is less than current node price
            node.left = delete(node.left, name, price)              #call recursively to delete the node from left sub tree

        elif price > node.item.price:                               #Check if price is greater than current node price
            node.right = delete(node.right, name, price)            #call recursively to delete the node from right sub tree

        else:
            if node.left is None:                                   #Check if node has no left child
                current = node                                #Assign current node to right child
                node = None                                         #delete the node                      
                return current, success
            
            elif node.right is None:                                #Check if node has no right child
                current = node                               #Assign current node to left child
                node = None                                         #delete the node
                return current, success
            else:
                current = findminnode(node.right)                   #find the min value from left sub tree to be replaced
                node.item = current.item                            # replaced the min value from right sub tree
                node.right = delete(node.right, current.item.name, current.item.price)   #delete the min value node from right sub tree
        return node, success
            
    def findminnode(node):                                         
        current = node                                              #find the min node from the right subtree
        while current.left:                                          #check until there is no left node
            current = current.left                                   #fetches the min node     
        return current
        
    node, success = delete(bst.root, name, price)
    if success:
        bst.no_of_phones -= 1
    return node

    

def totalPhones (bst) :

    # This function should return a pair of integers, first being the total different types of Phones currently in the store, and the second integer being the total number of Phones currently in stock in the store i.e sum of quantity left in stock field of each Phone entry in the BST.
    def total_count_qty(node):

        if node is None:
            print("BST is empty")
            return 0, 0
        left_tree_count , left_tree_quantity = total_count_qty(node.left)
        right_tree_count , right_tree_quantity = total_count_qty(node.right)
        cnt = left_tree_count + right_tree_count + 1
        qty = left_tree_quantity + right_tree_quantity + node.item.quantity
        return cnt, qty
    
    count, quantity = total_count_qty(bst.root)
    return count, quantity
# Enum type of choices
class Input(Enum):
    RESTART = 0
    FILE_INPUT = 1
    COMMAND_INPUT = 2
    SEARCH_COST = 3
    FIND_MAX = 4
    FIND_SECOND_MAX = 5
    FIND_MIN = 6
    FIND_SECOND_MIN = 7
    DELETE_RECORD = 8
    UPDATE_STOCK = 9
    LIST_ALL_PRICE = 10
    PHONE_TYPE_AND_STOCK_PAIR = 11
    EXIT = 12


def get_input_from_user():
    print(" 0. Restart Freshly")
    print(" 1. File Input")
    print(" 2. Command line Input")
    print(" 3. Search Cost")
    print(" 4. Find max Price")
    print(" 5. Find second max Price")
    print(" 6. Find min Price")
    print(" 7. Find second min Price")
    print(" 8. Delete record")
    print(" 9. Update stock")
    print("10. List all the prices")
    print("11. Display number of phone type and stock pair")
    print("12. Exit")
    option = int(input("Enter your choice: "))
    return option


def command_prompt():
    # Get the choice from user

    bst = createEmptyBST()

    while (True):
        # Loop till the user enters valid input               
        option = get_input_from_user()

        # TODO: Validate option
        if option == Input.RESTART.value:
            del(bst)
            bst = createEmptyBST()
            print("Operation successful")
        elif option == Input.FILE_INPUT.value:
            filename = input("Enter the name of the file: ")
            f = open(filename, "r")
            no_of_entries = int(f.readline().rstrip('\n'))
            for _ in range(no_of_entries):
                item = f.readline().rstrip('\n').split(", ")
                phone = Phone(item[0], int(item[1]), int(item[2]))
                bst = insertIntoBST(bst, phone)
            f.close()
            print("Insertion successful")
        elif option == Input.COMMAND_INPUT.value:
            no_of_entries = int(input("Enter the number of entries: "))
            print("Enter the details is below format:\n<PHONE_NAME>, <PRICE>, <QUANTITY>")
            for _ in range(no_of_entries):
                item = input("Enter the phone details: ").split(', ')
                phone = Phone(item[0], int(item[1]), int(item[2]))
                bst = insertIntoBST(bst, phone)
        elif option == Input.SEARCH_COST.value:
            cost = int(input("Enter the phone price to search: "))
            phone = findInBST(bst, cost)
            print(phone)
        elif option == Input.FIND_MAX.value:
            phone = findMaxPrice(bst)
            print(phone)
        elif option == Input.FIND_SECOND_MAX.value:
            phone = findSecondMaxPrice(bst)
            print(phone)
        elif option == Input.FIND_MIN.value:
            phone = findMinPrice(bst)
            print(phone)
        elif option == Input.FIND_SECOND_MIN.value:
            phone = findSecondMinPrice(bst)
            print(phone)
        elif option == Input.DELETE_RECORD.value:
            name = input("Enter the name of the phone to be deleted ")
            cost = int(input("Enter the cost pf the phone to be deleted "))
            phone = deleteFromBST (bst, name, cost)
            print("Deleted phone details")
            print(phone)
            # TODO: deleteFromBST(bst, name, price)
            pass
        elif option == Input.UPDATE_STOCK.value:
            # TODO: modifyQtyInStock(bst, name, price, new_qty)
            pass
        elif option == Input.LIST_ALL_PRICE.value:
            # TODO: listAllPrices(bst)
            pass
        elif option == Input.PHONE_TYPE_AND_STOCK_PAIR.value:
            count, quantity = totalPhones (bst)
            print("Phone count and quantity is \n",count, quantity)
            pass
        elif option == Input.EXIT.value:
            return


if __name__ == "__main__": 
    command_prompt()
