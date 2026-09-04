from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        # Бинарный поиск по строкам
        l, r = 0, rows - 1

        while l <= r:
            row = (l + r) // 2

            if target < matrix[row][0]:
                # target находится выше
                r = row - 1

            elif target > matrix[row][cols - 1]:
                # target находится ниже
                l = row + 1

            else:
                # Подходящая строка найдена.
                # Начинаем вложенный бинарный поиск
                l1, r1 = 0, cols - 1

                while l1 <= r1:
                    mid = (l1 + r1) // 2

                    if matrix[row][mid] == target:
                        return True

                    elif matrix[row][mid] < target:
                        l1 = mid + 1

                    else:
                        r1 = mid - 1

                # Строка найдена, но target внутри неё отсутствует
                return False

        # Подходящей строки нет
        return False