class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Бинпоиск всегда ведём по МЕНЬШЕМУ массиву — так гарантируется log(min(m,n)),
        # а не log(max(m,n)). Если nums1 длиннее — просто меняем местами.
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total = m + n
        half = total // 2   # сколько элементов должно попасть в "левую" половину

        l, r = 0, m   # l/r — сколько элементов берём из nums1 в левую часть (от 0 до m)
        
        while l <= r:
            i = (l + r) // 2     # берём i элементов из nums1 в левую часть
            j = half - i         # остаток левой части добираем из nums2 — j не выбирается отдельно!

            # значения ровно на границе разреза
            # если разрез в самом начале/конце массива — подставляем -inf / +inf,
            # чтобы сравнение ниже не сломалось на "несуществующем" элементе
            left1  = nums1[i - 1] if i > 0 else float('-inf')
            right1 = nums1[i]     if i < m else float('inf')
            left2  = nums2[j - 1] if j > 0 else float('-inf')
            right2 = nums2[j]     if j < n else float('inf')


            if left1 <= right2 and left2 <= right1:
                # разрез верный: вся левая часть <= всей правой части
                if total % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2
                else:
                    return min(right1, right2)
            elif left1 > right2:
                r = i - 1   # взяли слишком МНОГО из nums1 в левую часть — сдвигаем разрез влево
            else:
                l = i + 1   # взяли слишком МАЛО из nums1 — сдвигаем разрез вправо

        return 0.0  # сюда не дойдём при корректном вводе