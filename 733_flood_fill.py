from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        x = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        #track the starting pixel. we only change if the neighboring pixel
        #is the same as the starting pixel.
        starting_pixel = image[sr][sc] 

        #base case for recursion
        if image[sr][sc] == color:
            return image
        
        else:
            image[sr][sc] = color
            for i,j in x:
                new_sr = sr + i
                new_sc = sc + j
                if (0 <= new_sr < len(image)) and (0 <= new_sc < len(image[0])):
                    if image[new_sr][new_sc] == starting_pixel:
                        self.floodFill(image, new_sr, new_sc, color)
        return image
