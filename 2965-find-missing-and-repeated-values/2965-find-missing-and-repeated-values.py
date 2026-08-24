class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        values=[]
        l=[]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                values.append(grid[i][j])
        for i in values:
            if values.count(i)==2 and i not in l:
                l.append(i)
        for number in range(1,len(values)+1):
            if number not in values:
                l.append(number)
        return l


        