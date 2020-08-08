def find(array, idx):
    l, r = -1, -1
    if array[idx]==1:
        l, l_idx=1, idx
    num=1
    l_idx=r_idx=idx
    if idx!=0:
        while(array[l_idx-1]==num+1):
            l_idx-=1
            num+=1
            l=num
            if l_idx==0:
                break
    num=1
    if idx!=len(array)-1:
        while(array[r_idx+1]==num+1):
            r_idx+=1
            num+=1
            r=num
            if r_idx==len(array)-1:
                break
    if l>=r:
        return l, l_idx
    else:
        return r, r_idx

num=int(input())
for idx in range(1, num+1):
    _=input()
    leng=int(input())
    data=[int(x) for x in input().split()]
    ans=[-1, -1]
    for _i, item in enumerate(data):
        if item==1:
            n, i=find(data, _i)
            if n>ans[0]:
                ans=[n, i]
    print('Case #{}: {} {}'.format(idx, ans[0], ans[1]))