from cmath import inf


tests = int(input())

for test in range(tests):
    n = int(input())
    nums = list(map(int, input().split()))

    pend, nend, pan,nan, pl, nl = -inf, -inf, 0, 0,0,0

    for idx in range(n):
        if nums[idx] > 0:

            if nend == -inf:
                pend = max(pend, nums[idx])
                pl = 1
                pan = pend  
            elif pl == nl + 1:
                pend = max(pend, nend + nums[idx])
                pl = nl + 1
                pan = pend 

            elif pl < nl + 1:
                pend = nend + nums[idx] 
                pl = nl + 1
                pan = pend         
            

        else:
            if pend == -inf:
                nend = max(nend, 0 + nums[idx])
                nl += 1
                nan = nend
            elif nl == pl + 1:
                nend = max(nend, pend + nums[idx])
                nl = pl + 1
                nan = nend
            elif nl < pl + 1:
                nend = pend + nums[idx]
                nl = pl + 1
                nan = nend

  
    if nl > pl:
        ans = nan
    elif pl > nl:
        ans = pan
    else:
        ans = max(pan,nan)
    print(ans)

