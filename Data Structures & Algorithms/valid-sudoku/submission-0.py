class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        import math
        rows = [[0 for _ in range(9)] for _ in range(9)]
        cols = [[0 for _ in range(9)] for _ in range(9)]
        boxes = [[0 for _ in range(9)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                e = board[i][j]
                if e!='.':
                    r = math.ceil((i+1)/3)
                    c = math.ceil((j+1)/3)
                    if r == 1:
                        box_id = c-1
                    elif r == 2:
                        box_id = c+2
                    else:
                        box_id = c+5
                    idx = int(e)-1
                    if rows[i][idx] == 1 or cols[j][idx]==1 or boxes[box_id][idx]== 1 :
                        # print(boxes)
                        # print(rows[i][idx], cols[j][idx], boxes[box_id][idx])
                        return False
                    else:
                        rows[i][idx] += 1 
                        cols[j][idx]+=1  
                        boxes[box_id][idx]+=1
        return True

                    