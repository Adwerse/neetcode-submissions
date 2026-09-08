# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None

        fast, slow = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None
        temp = None
        prev = None

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        p1, p2 = head, prev   # prev — та самая развёрнутая вторая половина

        while p2:
            n1 = p1.next   # сохраняем оба "следующих" ДО того как начнём перевешивать
            n2 = p2.next

            p1.next = p2   # узел из первой половины указывает на узел из второй
            p2.next = n1   # узел из второй указывает на СЛЕДУЮЩИЙ из первой

            p1 = n1        # оба указателя сдвигаются по сохранённым, а не испорченным значениям
            p2 = n2

        return


