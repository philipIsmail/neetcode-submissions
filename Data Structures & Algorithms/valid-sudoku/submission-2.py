class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row = defaultdict(set)
        col = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):

                curr = board[r][c]

                if curr == ".":
                    continue
                
                box = r // 3 * 3 + c // 3 

                if curr in row[r] or curr in col[c] or curr in boxes[box]:
                    return False

                row[r].add(curr)
                col[c].add(curr)
                boxes[box].add(curr)

        return True