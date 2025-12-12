#My aim is to get k most frequent numbers from the list

nums = [1,1,1,2,3,4,5,6,7,7]
k = 2                       #i need to get 2 most frequent elements

def frequensy(nums, k):
    count = {}                         #  hashmap
    freq = [[] for i in range(len(nums) + 1)]  # i created 11 "buckets" for our elements

    # i count how many times simmilar elements appeared in the list
    for n in nums:
        count[n] = 1 + count.get(n, 0)  #turn into hashmap

    #Putting numbers from the hashmap to buckets by comparing idex to the frequensy 
    for n, c in count.items(): #separating the key value pairs
        freq[c].append(n) # assigning c to the index of the bucket and giving n value 

    # Choosing k most frequent elements
    res = []
    #First -1 to erase 1 bucket because thre is only 10 elements while we have 11 buckets
    # 0 aimed to stop looping when "for" reach the index 0, for we don't have element 0
    # Second -1 to turn over our elements so we get most frequent elements not least
    for i in range(len(freq) - 1, 0, -1): 
        for n in freq[i]: #cheack each frequensy that appeared  once
            res.append(n)
            if len(res) == k:
                return res


print(frequensy(nums, k))