# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()   # фиктивный узел-якорь; сам никогда не попадёт в ответ, нужен только чтобы не терять начало списка
        tail = dummy         # tail — подвижная переменная, строит цепочку результата шаг за шагом

        while list1 and list2:            # пока оба списка не исчерпаны
            if list1.val < list2.val:
                tail.next = list1          # подвешиваем МЕНЬШИЙ узел к концу результата
                list1 = list1.next         # и сдвигаем именно тот список, откуда взяли узел
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next               # сдвигаем tail на только что подвешенный узел — теперь это новый конец цепочки

        # один из списков закончился раньше — остаток второго (уже отсортированный) подвешиваем целиком, без поэлементного цикла
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next   # настоящий результат начинается ПОСЛЕ якоря — поэтому .next, а не сам dummy