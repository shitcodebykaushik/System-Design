class Node:
    def __init__(self, key=0, val=0):
        self.key = key 
        self.val = val 
        self.prev = None
        self.next = None
    
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Hash map to store {key: Node}
        
        # Dummy nodes for Head and Tail to simplify logic
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def _remove(self, node: Node):
        """Removes a node from its current position in the list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        
    def _insert_front(self, node: Node):
        """Inserts a node right after the dummy head (Most Recently Used)."""
        first_node = self.head.next
        
        node.next = first_node
        node.prev = self.head
        
        self.head.next = node
        first_node.prev = node
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        # Move accessed node to the front (MRU)
        node = self.cache[key]
        self._remove(node)
        self._insert_front(node)
        return node.val
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update existing: remove old position
            self._remove(self.cache[key])
        
        # Create/Update node and move to front
        new_node = Node(key, value)
        self.cache[key] = new_node
        self._insert_front(new_node)

        # Eviction logic if we exceed capacity
        if len(self.cache) > self.capacity:
            # The LRU node is the one right before the dummy tail
            lru_node = self.tail.prev
            self._remove(lru_node)
            del self.cache[lru_node.key]

# --- EXAMPLE USAGE ---

# 1. Initialize a cache with capacity of 2
my_cache = LRUCache(2)

# 2. Put some values
my_cache.put(1, 100) # Cache: {1:100}
my_cache.put(2, 200) # Cache: {2:200, 1:100}

# 3. Get a value (this makes it "recently used")
print(f"Get 1: {my_cache.get(1)}") # Returns 100. Cache: {1:100, 2:200}

# 4. Add a new item that exceeds capacity
my_cache.put(3, 300) # Cache is full! Evicts key 2 (least recently used)

# 5. Check results
print(f"Get 2: {my_cache.get(2)}") # Returns -1 (it was evicted)
print(f"Get 3: {my_cache.get(3)}") # Returns 300