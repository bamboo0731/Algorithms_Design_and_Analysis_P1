# method 1: 162085
# method 2: 164123
# method 3: 138382

def run():
    method = 1
    f = open('QuickSort.txt')
    nums = []
    for line in f:
        nums.append(int(line[0:-1]))
    a, b = QuickSort(nums, method)
    print b
    
def QuickSort(nums, method):
    l = len(nums)
    if l == 1:
        return nums, 0

    if method > 1:
        if method == 2:
            p = -1
        else:
            p = l/2 if l%2 else l/2 - 1
            a = nums[0] - nums[-1]
            b = nums[-1] - nums[p]
            c = nums[p] - nums[0]
            if a*b > 0:
                p = -1
            elif c*a > 0:
                p = 0
        temp = nums[0]
        nums[0] = nums[p]
        nums[p] = temp
    pivot = nums[0]
    m = 0
    count = l-1
    for i in xrange(1,l):
        if nums[i] < pivot:
            m += 1
            temp = nums[m]
            nums[m] = nums[i]
            nums[i] = temp
            
    nums[0] = nums[m]
    nums[m] = pivot
    if m != 0:
        nums[:m], lc = QuickSort(nums[:m], method)
        count += lc
    if nums[m] != nums[-1]:
        nums[m+1:], rc = QuickSort(nums[m+1:], method)
        count += rc
    return nums, count