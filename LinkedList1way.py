class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def addNode(self, node):
        if self.next:
            self.next.addNode(node)
        else:
            self.next = node
    
    def insertNode(self, node, n_find):
        curr = self
        prev = None

        while curr != None:
            if curr.value == n_find:
                prev.next = node
                node.next = curr
                curr = None
            else:
                prev = curr
                curr = curr.next

    def deleteNode(self, n_find):
        curr = self
        prev = None

        while curr != None:
            if curr.value == n_find:
                prev.next = curr.next
                curr = None
            else:
                prev = curr
                curr = curr.next

    def searchNode(self, n_find):
        if self.value == n_find:
            return self
        else:
            if self.next:
                return self.next.searchNode(n_find)

            else:
                return "Not Found"
            
        
        
    def printinfo(self):
        print(self.value, end=" => ")
        if self.next:
            self.next.printinfo()
        else:
            print("end")
        
if __name__ == "__main__":

    head = Node(10)

    database = [Node(i) for i in range(11,30,3)]

    for n in database:
        head.addNode(n)
    print(head)
    head.insertNode(Node(28),29)
    head.printinfo()
    head.deleteNode(22)
    head.printinfo()


    print(head.searchNode(29))
