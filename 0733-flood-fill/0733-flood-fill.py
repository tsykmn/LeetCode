class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """

        def dfs(x, y):
            if x < 0 or y < 0 or x >= len(image) or y >= len(image[0]):
                return
            elif (image[x][y] != startColor):
                return
            image[x][y] = color
            dfs(x-1, y)
            dfs(x+1, y)
            dfs(x, y-1)
            dfs(x, y+1)
        startColor = image[sr][sc]
        if startColor != color:
            dfs(sr, sc)
        return image