from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Это длина массива
        n = len(nums)
    
        # Шаг 1: считаем частоту каждого элемента
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        # Шаг 2: создаём массив корзин размером n+1
        # buckets[i] будет хранить список элементов, встретившихся РОВНО i раз
        buckets = [[] for _ in range(n + 1)]
        for num, count in freq.items():
            buckets[count].append(num)
        
        # Шаг 3: идём с конца (от самой высокой частоты к самой низкой)
        result = []
        for count in range(n, 0, -1):
            for num in buckets[count]:
                result.append(num)
                if len(result) == k:
                    return result
        
        return result