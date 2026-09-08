# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None

        # --- Стадия 1: найти середину (fast/slow, тот же паттерн что в hasCycle) ---
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # после цикла slow стоит на границе разреза

        # --- Стадия 2: разрезать список на две половины ---
        second = slow.next   # сохраняем вторую половину
        slow.next = None     # обрубаем первую половину — теперь это два независимых списка
        temp = None
        prev = None

        # --- Стадия 3: развернуть вторую половину (тот же reverseList) ---
        while second:
            temp = second.next     # сохраняем "следующий" до того как испортим ссылку
            second.next = prev     # разворачиваем стрелку
            prev = second           # сдвигаем prev вперёд
            second = temp            # сдвигаем second по сохранённому значению
        # prev теперь — голова развёрнутой второй половины

        # --- Стадия 4: слить обе половины через одну ---
        p1, p2 = head, prev   # p1 — первая половина, p2 — развёрнутая вторая
        while p2:
            n1 = p1.next   # сохраняем оба "следующих" ДО перевешивания указателей
            n2 = p2.next

            p1.next = p2   # узел первой половины указывает на узел второй
            p2.next = n1   # узел второй половины указывает на следующий из первой

            p1 = n1
            p2 = n2
        # цикл кончается, когда исчерпывается p2 (вторая половина всегда <= первой) —
        # оставшийся хвост первой половины (если он есть) уже был правильно связан
        # изначальными указателями и просто "доедет" в конец сам собой

        return


