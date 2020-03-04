# Brute Force



def size2Subsets(s): 
    l = []
    n = len(s) 
    for i in range (n):
        for j in range(i,n,1):
            if i != (n-1): 
                if i != j: l.append((s[i], s[j]))
    print(l)
    return l


class Solution:
    def twoSum(self, nums, target):
            cnt = 0
            lNums = len(nums)
            trials = size2Subsets(nums)
            print ("this is trials : ")
            print (trials)
            for j in range (len(trials)):
                if sum(trials[j]) == target:
                    if trials[j][0] == trials[j][1]: 
                        print ("these are the 2 # : ")
                        print ([trials[j][0],trials[j][0]])
                    
                        cnt += 1
                        i1 = nums.index(trials[j][0])
                        nums[nums.index(trials[j][0])] = target + 1
                        print(nums)
                        return [i1,nums.index(trials[j][1])]
                    else:
                        i1 = nums.index(trials[j][0])
                        return [i1,nums.index(trials[j][1])]