class Node:
    def __init__(self,key=0,val=0):
        self.key=key
        self.val=val
        self.next=None
        self.prev=None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.hashmap={}

        self.head=Node() #sentinel MRU side
        self.tail=Node() #sentinel LRU side
        self.head.next=self.tail
        self.tail.prev=self.head

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        
        node=self.hashmap[key]
        #remove node from its current position
        node.prev.next=node.next
        node.next.prev=node.prev
        #insert at front
        node.next=self.head.next
        self.head.next.prev=node
        self.head.next=node
        node.prev=self.head
        #return the value
        return node.val
    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            node=self.hashmap[key]
            node.val=value
            #remove node from its current position
            node.prev.next=node.next
            node.next.prev=node.prev
            #insert at front
            node.next=self.head.next
            self.head.next.prev=node
            self.head.next=node
            node.prev=self.head
            return
        node=Node(key,value)
        self.hashmap[key]=node
        #insert at front
        node.next=self.head.next
        self.head.next.prev=node
        self.head.next=node
        node.prev=self.head

        if len(self.hashmap)>self.cap:
            lru=self.tail.prev
            lru.prev.next=self.tail
            self.tail.prev=lru.prev

            del self.hashmap[lru.key]

    
