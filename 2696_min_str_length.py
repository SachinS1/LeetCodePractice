class Solution:
    def minLength(self, s: str) -> int:
        
        substrings = ["AB", "CD"]


        # for i in range(0,len(s)-1):

        #     if s[i] + s[i+1] in substrings:
        #         return self.minLength(s[:i] + s[i+2:])

        # return len(s)

        if not s:
            return 0

        track_list = [s[0]]

        for i in range(1, len(s)):

            track_list.append(s[i])
            if len(track_list) > 1 and track_list[-2] + track_list[-1] in substrings:
                track_list.pop()
                track_list.pop()
        return len(track_list)
            