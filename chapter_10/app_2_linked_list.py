
# linked list implementation

class ListElement:
    def __init__(self, el, e_prev, e_next):
        print("creating: ", el)
        self.key = el
        self.e_prev = e_prev
        self.e_next = e_next

    def __str__(self):
        res = ""
        if self.e_prev:
            res += "prev: " + str(self.e_prev.key)
        else:
            res += "prev: None"
        res += " key: " + str(self.key)
        if self.e_next:
            res += " next: " + str(self.e_next.key)
        else:
            res += " next: None"
        return res

class ListContainer:
    def __init__(self, arr):
        self.head = None
        self.tail = None
        for i in range(len(arr)):
            self.insert(arr[i])

    def __str__(self):
        x = self.head
        res = "list: (" + str(x.key)
        while x.e_next:
            x = x.e_next
            res += " " + str(x.key)
        res += ")"
        return res

    def insert(self, el):        
        x = ListElement(el, None, self.head)
        if self.head != None:
            self.head.e_prev = x
        self.head = x

        if self.tail == None:
            self.tail = x

    def search(self, k):
        x = self.head
        while x != None and x.key != k:
            x = x.e_next
        return x

A = [1, 2, 3, 4, 5]
list_a = ListContainer(A)
list_a.insert(10)
list_a.insert(20)
print(list_a.search(3))
print(list_a)
