class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(char for char in s if char.isalnum())
        cleaned = cleaned.lower()
        #print(cleaned)
        lpointer = 0
        rpointer = len(cleaned) - 1
        while lpointer < rpointer:
            if cleaned[lpointer] == cleaned[rpointer]:
                lpointer += 1
                rpointer -= 1
            else:
                return False
        return True