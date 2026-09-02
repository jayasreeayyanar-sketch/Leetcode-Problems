class Node:
    def __init__(self, count=0):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None

class AllOne(object):

    def __init__(self):
        # Dummy head and tail to easily fetch Min and Max in O(1)
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        
        # Maps key -> Node
        self.key_to_node = {}

    def _add_node_after(self, new_node, prev_node):
        """Helper to insert a new node into the doubly linked list."""
        new_node.prev = prev_node
        new_node.next = prev_node.next
        prev_node.next.prev = new_node
        prev_node.next = new_node

    def _remove_node(self, node):
        """Helper to remove an empty node from the doubly linked list."""
        node.prev.next = node.next
        node.next.prev = node.prev

    def inc(self, key):
        """
        :type key: str
        :rtype: None
        """
        if key not in self.key_to_node:
            # Key is new, target count is 1
            first_node = self.head.next
            if first_node == self.tail or first_node.count > 1:
                new_node = Node(1)
                self._add_node_after(new_node, self.head)
                first_node = new_node
            
            first_node.keys.add(key)
            self.key_to_node[key] = first_node
        else:
            # Key exists, increment its count
            curr_node = self.key_to_node[key]
            next_node = curr_node.next
            
            if next_node == self.tail or next_node.count != curr_node.count + 1:
                new_node = Node(curr_node.count + 1)
                self._add_node_after(new_node, curr_node)
                next_node = new_node
                
            next_node.keys.add(key)
            self.key_to_node[key] = next_node
            
            # Clean up the old node if it is now empty
            curr_node.keys.remove(key)
            if not curr_node.keys:
                self._remove_node(curr_node)

    def dec(self, key):
        """
        :type key: str
        :rtype: None
        """
        # Guaranteed that key exists per problem constraints
        curr_node = self.key_to_node[key]
        curr_node.keys.remove(key)
        
        if curr_node.count == 1:
            del self.key_to_node[key]
        else:
            prev_node = curr_node.prev
            if prev_node == self.head or prev_node.count != curr_node.count - 1:
                new_node = Node(curr_node.count - 1)
                self._add_node_after(new_node, prev_node)
                prev_node = new_node
                
            prev_node.keys.add(key)
            self.key_to_node[key] = prev_node
            
        # Clean up the old node if it is now empty
        if not curr_node.keys:
            self._remove_node(curr_node)

    def getMaxKey(self):
        """
        :rtype: str
        """
        if self.tail.prev == self.head:
            return ""
        # Return any element from the set of the max node (before tail)
        return next(iter(self.tail.prev.keys))

    def getMinKey(self):
        """
        :rtype: str
        """
        if self.head.next == self.tail:
            return ""
        # Return any element from the set of the min node (after head)
        return next(iter(self.head.next.keys))
