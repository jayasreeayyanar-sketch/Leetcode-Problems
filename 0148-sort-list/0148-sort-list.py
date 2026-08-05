class Solution(object):
    def sortList(self, head):
        if not head or not head.next:
            return head
        mid = self._get_mid(head)
        left = head
        right = mid.next
        mid.next = None 
        left_sorted = self.sortList(left)
        right_sorted = self.sortList(right)
        return self._merge(left_sorted, right_sorted)        
    def _get_mid(self, head):
        slow = head
        fast = head.next 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next            
        return slow        
    def _merge(self, list1, list2):
        """Merges two sorted linked lists."""
        dummy = ListNode(0)
        tail = dummy        
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        tail.next = list1 if list1 else list2        
        return dummy.next