

class Solution:
    def isValid(self, s: str) -> bool:
        openings = ['(', '{', '[']

        pairings = {')':'(', '}':'{', ']':'['}

        tracks = []

        for bracks in s:
            #if length of string is 0 or 1 return false
            if len(s) == 0 or len(s) == 1: 
                return False

            #check for a open bracket
            if bracks in openings:
                tracks.append(bracks)
            
            else:
                #if encountered a close bracket before open
                if len(tracks) == 0:
                    return False
                elif pairings[bracks] == tracks[-1]:
                    tracks.pop()
                else:
                    return False

        return True if len(tracks) == 0 else False