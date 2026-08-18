# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        length = 0

        current = head
        while current:
            length += 1
            current = current.next

        remove = length - n

        if remove == 0:
            return head.next

        print(remove)

        i = 0
        dummy = node = head
        while node:
            if i == remove - 1:
                node.next = node.next.next
            node = node.next
            i += 1

        return dummy