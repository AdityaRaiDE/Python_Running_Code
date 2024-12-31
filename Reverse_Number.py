# reverse a number 
class Reverse:
    def __init__(self,value):
        self.value, self.sign_bit  = (abs(value),True) if value < 0 else (value,False)
    def reverse(self):
        reverse_number = 0 
        while True:
            if self.value > 0:
                reverse_number = (reverse_number * 10 )+(self.value % 10)
                self.value = self.value // 10
            else:
                break
        return -(reverse_number) if self.sign_bit else reverse_number
