def bin_expo(a,b):
    ans=1
    while(b>0):
        if b%2==1:
            ans*=a
        a*=a
        b//=2
    return ans
