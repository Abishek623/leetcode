class Solution:
    def floodFill(self, image, sr, sc, color):
        if image[sr][sc] == color:
            return image

        self.helper(image, sr, sc, color, image[sr][sc])

        return image

    def helper(self, image, i, j, color, orgCol):
        if (i < 0 or j < 0 or i >= len(image) or
            j >= len(image[0]) or image[i][j] != orgCol):
            return

        image[i][j] = color

        self.helper(image, i - 1, j, color, orgCol)
        self.helper(image, i + 1, j, color, orgCol)
        self.helper(image, i, j - 1, color, orgCol)
        self.helper(image, i, j + 1, color, orgCol)