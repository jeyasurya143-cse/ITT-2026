class Solution(object):
    def buildArray(self, target, n):
        output = list()
        push = "Push"
        pop = "Pop"
        current_index = 0
        
        for i in range(1, n + 1):
            if current_index == len(target):
                break
                
            if i == target[current_index]:
                output.append(push)
                current_index += 1
            else:
                output.append(push)
                output.append(pop)
                
        return output
