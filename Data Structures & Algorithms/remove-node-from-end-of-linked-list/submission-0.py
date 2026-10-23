class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        c = 0

        # Count total nodes
        while temp:
            c += 1
            temp = temp.next

        # Remove the first node
        if c == n:
            return head.next

        l = 0
        st = head
        prev = None

        # Reach the node before the target
        while l < c - n:
            prev = st
            st = st.next
            l += 1

        prev.next = st.next

        return head