class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Initialize two pointers at the start of the list
        slow = head
        fast = head
        
        # Traverse the list as long as the fast pointer can move two steps
        while fast and fast.next:
            slow = slow.next          # Moves 1 node
            fast = fast.next.next     # Moves 2 nodes
            
            # If pointers meet, there is a cycle
            if slow == fast:
                return True
        
        # If fast reaches the end (None), no cycle exists
        return False
