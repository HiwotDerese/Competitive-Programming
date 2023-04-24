class Solution:
    def fill(self, image, row, col, original, color):
        # print(col, row, image)
        if row < 0 or col < 0 or row >= len(image) or col >= len(image[0]):
            return
        
        elif color == image[row][col]:
            return
        
        elif image[row][col] == original:
            image[row][col] = color

            self.fill(image, row + 1, col, original, color)
            self.fill(image, row - 1, col, original, color)
            self.fill(image, row, col + 1, original, color)
            self.fill(image, row, col - 1, original, color)
        
        
        
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]
        
        self.fill(image, sr, sc, original_color, color)
        
        return image
        
        