from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        cl = 0
        cr = n-1
        rl = 0
        rr = m-1

        while cl <= cr and rl <= rr:
            midc = cl + (cr - cl)//2
            midr = rl + (rr - rl)//2 

            if matrix[midr][midc] == target:
                return True

            elif matrix[midr][midc] > target:
                if midc > 0 :
                    cr = midc - 1
                elif midc == 0:
                    if rr > 0:
                        rr = midr - 1
                        cr = n-1
                    else:
                        return False    
            else:
                if midc < n-1:
                    cl = midc + 1                 
                elif midc == n-1:
                    if rl < m-1:
                        rl = midr + 1
                        cl = 0
                    else:
                        return False    
        return False                