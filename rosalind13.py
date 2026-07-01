file = open('rosalind13test.txt', "r")
nums = file.read().split()
file.close()

nums = list(map(int,nums))

print(nums)
#nums0 AA-AA    nums1 AA-Aa    nums2 AA-aa
#nums3 Aa-Aa    nums4 Aa-aa    nums5 aa-aa

domkids = 0
for x in range(len(nums)):
    print(x, nums[x])
    if x <= 2:
        domkids = domkids + nums[x]*2
    elif x == 3:
        domkids = domkids + 0.75*nums[x]*2
    elif x == 4:
        domkids = domkids + 0.5*nums[x]*2
    else:
        domkids = domkids + 0*nums[x]*2

print(domkids)

h = open("rosalind13ans.txt", "w+")
h.write(str(domkids))
h.close()
