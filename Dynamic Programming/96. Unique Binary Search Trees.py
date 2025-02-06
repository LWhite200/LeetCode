" Triangles chanhge this "

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rs = [[1]]

        for _ in range(numRows - 1):
            dummy_row = [0] + rs[-1] + [0]
            row = []

            for i in range(len(rs[-1]) + 1):
                row.append(dummy_row[i] + dummy_row[i+1])
            rs.append(row)
        
        return rs