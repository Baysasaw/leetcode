n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

ans = []
pointer1 = 0
pointer2 = 0

while pointer1 < n and pointer2 <m:
    if arr1[pointer1] <= arr2[pointer2]:
        ans.append(arr1[pointer1])
        pointer1+=1

    else:
        ans.append(arr2[pointer2])
        pointer2 +=1
    ans.extend(arr1[pointer1:])
    ans.extend(arr2[pointer2:])
print(*ans)