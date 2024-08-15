class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five_dollar = 0  # to keep count of $5 bills
        ten_dollar = 0   # to keep count of $10 bills

        for bill in bills:
            if bill == 5:
                five_dollar += 1  # collect the $5 bill
            elif bill == 10:
                if five_dollar > 0:
                    five_dollar -= 1  # give one $5 bill as change
                    ten_dollar += 1  # collect the $10 bill
                else:
                    return False  # can't give change
            elif bill == 20:
                if ten_dollar > 0 and five_dollar > 0:
                    ten_dollar -= 1  # give one $10 bill
                    five_dollar -= 1  # give one $5 bill
                elif five_dollar >= 3:
                    five_dollar -= 3  # give three $5 bills
                else:
                    return False  # can't give change
        
        return True  # all customers received correct change
