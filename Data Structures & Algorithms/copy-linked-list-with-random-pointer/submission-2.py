"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        curr = head
        pipipupu1 = {}

        while curr:
            pipipupu1[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head

        while curr:
            pipipupu1[curr].next = pipipupu1[curr.next] if curr.next else None
            pipipupu1[curr].random = pipipupu1[curr.random] if curr.random else None
            curr = curr.next
        
        return pipipupu1[head]
