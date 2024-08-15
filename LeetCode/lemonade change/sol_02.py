class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:         
        tenS_change = 0
        fiveS_change = 0

        for bill in bills:
            if bill == 5:
                fiveS_change += 5
            elif bill == 10:
                if fiveS_change >= 5:
                    fiveS_change -= 5
                else:
                    return False

                tenS_change += 10
            else:
                if tenS_change >= 10:
                    if fiveS_change >= 5:
                        tenS_change -= 10
                        fiveS_change -= 5
                    else:
                        return False
                elif fiveS_change >= 15:
                    fiveS_change -= 15
                else:
                    return False

        return True