# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast, slow = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        temp = None
        prev = None
        slow.next = None 

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        p1, p2 = head, prev # p1 — первая половина, p2 — развёрнутая вторая

        while p2:
            n1 = p1.next # СНАЧАЛА спасаем оба "следующих" — иначе потеряешь их после перевешивания
            n2 = p2.next

            p1.next = p2 # вот она, сама линковка: узел первой половины теперь ведёт на узел второй
            p2.next = n1 # а узел второй — обратно на СЛЕДУЮЩИЙ из первой (не на p1!)

            p1 = n1 # сдвигаем оба указателя по спасённым значениям
            p2 = n2

        return




