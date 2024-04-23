class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dic = defaultdict(int)
        dic[5] = 0
        dic[10] = 0
        dic[20] = 0

        for i in range(len(bills)):
            if bills[i] == 10 and dic[5] == 0:
                return False

            if bills[i] == 20 and (dic[5] == 0 or (dic[10] == 0 and dic[5] < 3)):
                return False

            if bills[i] == 10:
                dic[5] -= 1
                dic[10] += 1

            if bills[i] == 20:
                if dic[10] == 0:
                    dic[5] -= 3
                else:
                    dic[5] -= 1
                    dic[10] -= 1

            if bills[i] == 5:
                dic[5] += 1

        return True