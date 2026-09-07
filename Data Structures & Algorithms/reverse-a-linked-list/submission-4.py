# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = 0
        curr = head
        prev = None

        while curr:
            temp = curr.next # сначала запоминаем настоящий "следующий"
            curr.next = prev # ПОТОМ разворачиваем стрелку — пока curr это ещё тот узел, что нужен
            prev = curr
            curr = temp # двигаемся дальше по СОХРАНЁННОМУ значению, а не по уже испорченному curr.next
        return prev
            