class LRUCache:
    class Node:
        def __init__ (self, key, val):
            self.key = key
            self.val = val
            self.prev = self.next = None

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.head = self.Node(0, 0)
        self.tail = self.Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        prev, nextNode = node.prev, node.next
        prev.next = nextNode
        nextNode.prev = prev

    def insert(self, node):
        nextNode = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = nextNode
        nextNode.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val

        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        node = self.Node(key, value)
        self.insert(node)
        self.cache[key] = node

        if len(self.cache) >self.cap:
            last = self.tail.prev
            self.remove(last)
            del self.cache[last.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)