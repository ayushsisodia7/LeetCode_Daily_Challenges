class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        c=0
        if len(grid)==1:
            return 1;
        for j in range(len(grid)):
            l=[]
            for i in range(len(grid)):
                l.append(grid[i][j])
            for z in range(len(grid)):
                if l==grid[z]:
                    c+=1
        return c
