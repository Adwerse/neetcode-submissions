# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)   # якорь, как в mergeTwoLists — чтобы не потерять новую голову
        groupPrev = dummy           # последний узел ПЕРЕД текущей группой (изначально сам dummy)

        while True:
            kth = self.getKth(groupPrev, k)   # k-й узел от groupPrev — последний узел этой группы
            if not kth:
                break   # узлов меньше k — неполную группу не трогаем, оставляем как есть

            groupNext = kth.next   # запоминаем, что идёт СРАЗУ ПОСЛЕ группы — пригодится после разворота

            # тот же reverseList, что ты писал раньше, только с одной хитростью:
            # prev стартует не с None, а сразу с groupNext —
            # тогда ПОСЛЕДНИЙ узел группы после разворота сам укажет туда, куда нужно
            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:      # идём, пока не дойдём до конца именно ЭТОЙ группы
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            # после разворота: kth стал головой группы, groupPrev.next (старый) стал её хвостом
            tmp = groupPrev.next        # запоминаем старую голову группы — она и есть новый groupPrev
            groupPrev.next = kth        # пришиваем развёрнутую группу к тому, что было перед ней
            groupPrev = tmp              # сдвигаем groupPrev к следующей группе

        return dummy.next

    def getKth(self, curr, k):
        # просто проходит k шагов вперёд от curr; если узлов не хватило — вернёт None
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr