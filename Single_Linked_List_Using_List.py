class Node:
    def __init__(self,item=None,next=None):
        self.item = item
        self.next = next
class SingleLinkedList:
    def __init__(self,node:Node):
        self.head = list()
        while True:
            self.head.append(Node(node.item, node.next))
            if node.next is None:
                break
            node = node.next

    def insert_at_start(self,item):
        new_node = Node(item,self.head[0])
        self.head = [new_node] + self.head
    def insert_at_end(self,item):
        new_node = Node(item, None)
        self.head[-1].next = new_node
        self.head = self.head + [new_node]
    def insert_after_node(self,after,item):
        found_index = 1
        for ele in self.head:
            if after == ele.item:
                break
            else:
                found_index += 1
        else:
            return "After element not found!!"
        self.head = self.head[0:found_index]+[Node(item,self.head[found_index].item)] + self.head[found_index:]

    def delete_first(self):
        self.head= self.head[1:]
    def delete_last(self):
        self.head = self.head[:-1]
        self.head[-1].next = None
    def delete_node(self,item):
        found_at = 1
        for ele in self.head:
            if ele.item == item:
                self.head = self.head[0:found_at - 1] + self.head[found_at:]
                break
            found_at = found_at + 1
        else:
            return "Node Value not found"

    def is_empty(self):
        if len(self.head) == 0 :
            return "Single Linked List is Empty"
        return "SLL is not empty"
    def count_elements(self):
        return len(self.head)
#10,20,30,40
#---------UT------#
n1 = Node(10,Node(20,Node(30,Node(40))))
start = SingleLinkedList(n1)
# start = SingleLinkedList(Node(10))
start.insert_at_start(20)
start.insert_at_end(200)
for ele in start.head:
    print(ele.item)
print("---==========----")
start.insert_after_node(30,999)
for ele in start.head:
    print(ele.item)
print("---==========----")
print(start.insert_after_node(300,999))
start.delete_first()
for ele in start.head:
    print(ele.item)
print("---==========----")
start.delete_last()
for ele in start.head:
    print(ele.item)
print("---==========----")
start.delete_node(999)
for ele in start.head:
    print(ele.item)
print("---==========----")
# start = start.insert_at_start(250)
# print(start.node.item,start.node.next.item,start.node.next.next.item)
