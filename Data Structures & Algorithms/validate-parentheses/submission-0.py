class Solution:
    def isValid(self, s: str) -> bool:
        # Setup
        stack = []
        
        opening = {"(":")","[":"]","{":"}"}
        closing = {")":"(","]":"[","}":"{"} 
        # Closing not needed for correspondence, but
        # helpful for checking if it is a closing bracket

        # Iteration
        for char in s:
            
            # Opening bracket, add to list
            if char in opening:
                stack.append(opening[char])

            # Closing bracket, extra checks
            elif char in closing:
                
                # Empty, cannot close and thus false
                if len(stack) == 0:
                    return False

                # It last element, therfore valid bracket
                elif char == stack[-1]:
                    stack.pop()
                
                # Not last element, invalid
                else:
                    return False

            # Final validity statement
        return len(stack) == 0