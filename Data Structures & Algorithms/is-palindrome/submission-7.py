class Solution:
    def isPalindrome(self, s: str) -> bool:
        lpointer = 0
        rpointer = len(s) - 1
        while lpointer < rpointer:
            while lpointer < rpointer and not s[lpointer].isalnum():
                lpointer +=1
            while lpointer < rpointer and not s[rpointer].isalnum():
                rpointer -=1
            if s[lpointer].lower() != s[rpointer].lower():
                return False
            lpointer += 1
            rpointer -= 1
        return True