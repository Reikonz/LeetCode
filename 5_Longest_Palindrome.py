class Solution:
    def longestPalindrome(self, s: str) -> str:        
        palindrome_list = []
        longest_pal = ''
        pal_length = 0
        
        # Find all substrings
        for start in range(len(s)):
            # See if the current substring is worth checking
            if pal_length >= (len(s)-start):
                break
            else:
                # Compare the substrings
                for end in range(len(s)-start):
                    substring = s[start:end+start+1]

                    # Determine if substring is a palindrome
                    if substring == substring[::-1]:
                        if len(substring) > len(longest_pal):
                            longest_pal = substring
                            pal_length = len(longest_pal)
        return(longest_pal)
