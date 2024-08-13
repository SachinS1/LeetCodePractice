class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        track = [] # list to keep track of unique elements in s
        max_track_len = 0
        for letters in s:
            # find repeating letters     
            if letters in track:
                track = track[track.index(letters)+1:]
            #append letters to the track list
            track.append(letters)
            max_track_len = max(max_track_len, len(track))
    
        return max_track_len