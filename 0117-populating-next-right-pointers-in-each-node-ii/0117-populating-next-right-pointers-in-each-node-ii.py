class Solution(object):
    def connect(self, root):
        if not root:
            return None        
        curr = root        
        while curr:
            dummy = Node(0) 
            temp = dummy             
            while curr:
                if curr.left:
                    temp.next = curr.left
                    temp = temp.next
                if curr.right:
                    temp.next = curr.right
                    temp = temp.next
                curr = curr.next            
            curr = dummy.next            
        return root
