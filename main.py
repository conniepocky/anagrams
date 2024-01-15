def heapPermutation(a, size):
 
    if size == 1:
        print(a)
        return
 
    for i in range(size):
        heapPermutation(a, size-1)
 
        # if size is odd, swap 0th i.e (first)
        # and (size-1)th i.e (last) element
        # else If size is even, swap ith
        # and (size-1)th i.e (last) element
        if size & 1:
            a[0], a[size-1] = a[size-1], a[0]
        else:
            a[i], a[size-1] = a[size-1], a[i]
 
 
a = [*input("enter some text...")]
n = len(a)
heapPermutation(a, n)
