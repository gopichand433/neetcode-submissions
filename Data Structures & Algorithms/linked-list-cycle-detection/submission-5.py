# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head:
            sl=head
            fst=head
            while sl and fst and fst.next:
                sl=sl.next
                fst=fst.next.next
                if sl==fst:
                    return True
            return False
        else:
            return False