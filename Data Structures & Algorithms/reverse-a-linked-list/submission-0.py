# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next_node = curr.next # сохраняем "следующий", пока не потеряли его
            curr.next = prev # разворачиваем стрелку в обратную сторону
            prev = curr # сдвигаем prev вперёд
            curr = next_node # сдвигаем curr вперёд по сохранённому значению
        self.head = prev # новый head — это бывший последний узел
        return prev