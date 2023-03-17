"""https://leetcode.com/problems/longest-substring-without-repeating-characters/

Find the length of the longest substring without repeating characters

s = "abcabcbb"

Observations:
    
    When we scan an input string, we can count the characters, so we know if we
    have seen the same character before.

    For every next character ci, it may appear anywhere in the history.

    Since we are looking for the longest substring but not subsequence, we need
    to cut the history from the point where the same character was seen.

Ideas:

    Consider a window with a head and a tail.

    For each new character C at i,
        
        Expand the tail to i
        
        If C has been seen before at location j,
            Make the head to j (cut the history)
        
        Save the length of the current window

    Example 
        
        "abcabcbb"

        a   [a]
        b   [a,b]
        c   [a,b,c]
        a   [b,c,a]
        b   [c,a,b]
        c   [a,b,c]
        b   [c,b]
        b   [b]

        "pwwkew"

        p   [p]
        w   [p,w]
        w   [w]
        k   [w,k]
        e   [w,k,e]
        w   [k,e,w]

"""

# %%

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_winsize = 0
        win_head, win_tail = 0, 0
        history = {}

        for i in range(len(s)):
            # Move the tail
            win_tail = i + 1
            
            # If we have seen the s[i] before and its in the window, move the head
            if s[i] in history and history[s[i]] >= win_head:
                win_head = history[s[i]] + 1
            
            # Save the location of s[i] in the history
            history[s[i]] = i

            # Compute the max window size
            print("Read", s[i], history[s[i]], "window", win_head, win_tail, s[win_head:win_tail], "\nhistory", history)
            max_winsize = max(max_winsize, win_tail - win_head)

        return max_winsize
    
Solution().lengthOfLongestSubstring("abcabcbb")
# Solution().lengthOfLongestSubstring("bbbbb")
# Solution().lengthOfLongestSubstring("pwwkew")
# Solution().lengthOfLongestSubstring("abba")
# Solution().lengthOfLongestSubstring("")