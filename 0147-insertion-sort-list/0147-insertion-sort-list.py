class Solution(object):
    def insertionSortList(self, head):
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        curr = head        
        while curr:
            next_to_process = curr.next
            prev = dummy
            while prev.next and prev.next.val < curr.val:
                prev = prev.next
            curr.next = prev.next
            prev.next = curr
            curr = next_to_process            
        return dummy.next