class Node:
    def __init__(self, value):
        self.precede = None
        self.value = value
        self.next = None

    def addNode(self, node):
        if self.next:
            self.next.addNode(node)
        else:
            node.precede = self
            self.next = node
    
    def insertNode(self, node, n_find):
        curr = self
        prev1 = None
        prev2 = None

        while curr != None:
            if curr.value == n_find:
                prev2 = curr.next
                prev1.next = node
                node.precede = prev1
                node.next = prev2
                prev2.precede = node
                curr = None
            else:
                prev1 = curr
                curr = curr.next
        
    def searchNode(self,n_find):
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

def reverseNode(node):
    path = [node.value]
    l = node.precede
    while l != None:
        path.append(l.value)
        l = l.precede
    return path

if __name__ == "__main__":
    head = Node(10)
    database = [Node(i) for i in range(11,30,3)]

    for n in database:
        head.addNode(n)
    
    head.printinfo()
    node_find = head.searchNode(26)
    head.insertNode(Node(12),14)
    head.printinfo()