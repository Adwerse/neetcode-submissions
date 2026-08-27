class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n-1):
            if i > 0 and nums[i] == nums[i-1]:
                continue # тот самый пункт про дубликаты i

            left = i + 1
            right = n - 1

            while left < right:
                sum = nums[i] + nums[left] + nums[right]

                if sum < 0:
                    left = left + 1                # мало — двигаем left вправо
                elif sum > 0:
                    right = right - 1               # много — двигаем right влево
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left = left + 1
                    right = right - 1

                    while left < right and nums[left] == nums[left-1]:
                        left = left + 1             # пропускаем дубликаты слева
                    while left < right and nums[right] == nums[right+1]:
                        right = right - 1           # пропускаем дубликаты справа

        return result