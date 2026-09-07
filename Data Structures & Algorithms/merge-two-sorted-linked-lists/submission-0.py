# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()   # фиктивный узел-заглушка, сам никогда не попадёт в ответ
        tail = dummy         # tail — та самая "подвижная" переменная, которой у тебя не хватало

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1   # подвешиваем меньший узел к концу результата
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next         # сдвигаем tail вперёд — теперь он и есть новый конец цепочки

        # один из списков закончился раньше — второй остаток целиком (уже отсортированный) подвешиваем как есть
        tail.next = list1 if list1 else list2

        return dummy.next   # реальный результат начинается ПОСЛЕ фиктивного узла, поэтому .next, а не dummy
                