class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            temp = curr.next # the next step
            curr.next = prev # breaks the list into 2
            prev = curr # the current one becomes the prev
            curr = temp # the prev of the next one
        return prev