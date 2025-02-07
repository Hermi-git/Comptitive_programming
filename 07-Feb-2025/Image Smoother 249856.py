# Problem: Image Smoother - https://leetcode.com/problems/image-smoother/description/

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)
        n = len(img[0])
        smooth_img = [[0]*n for _ in range(m)]

        for row in range(m):
            for col in range(n):
                cells_sum = 0
                count_cell = 0
                for r in range(row-1, row+2):
                    for c in range(col-1, col+2):
                        if r < 0 or r == m or c < 0 or c == n:
                            continue
                        cells_sum += img[r][c]
                        count_cell += 1
                smooth_img[row][col] = cells_sum // count_cell
        
        return smooth_img