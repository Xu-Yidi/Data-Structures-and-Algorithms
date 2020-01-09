import random

class Solution:
    def sumZero(self, n: int) -> List[int]:
        array = [0 for i in range(n)]
        if n % 2 == 0:
            temp_array = random.sample(range(1,n+1), int(n/2))
            temp_array1 = [-i for i in temp_array]
            return temp_array1 + temp_array
        else:
            temp_array = random.sample(range(1,n+1), int((n-1)/2))
            temp_array1 = [-i for i in temp_array]
            return temp_array1 + [0] + temp_array      
            
            
            
            
            
