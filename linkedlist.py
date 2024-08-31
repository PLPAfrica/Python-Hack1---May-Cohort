class Link:
    def __init__(self, num):
        self.num = num
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, num):
        newlinkedlist = Link(num)

        if self.head is None:
            self.head = newlinkedlist
            return
        
        last = self.head
        while last.next:
            last = last.next


        last.next = newlinkedlist

    def find_max(self):
        if self.head is None:
            return "No list is provided"
        

        max_value = self.head.num
        current = self.head.next


        while current:
            if current.num > max_value:
                max_value = current.num
            current = current.next
        return max_value
    

def find_max():
    STRG = LinkedList()

    for item in input_list:
        STRG.append(item)


    return STRG.find_max()


input_list = [34,54,1,222,55,3,9]
max_intr = find_max()


print(f"The maximum value is: ", max_intr)

