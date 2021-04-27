def fake_bin(x):
    ans = ''
    for i in x:
        if int(i) < 5:
            ans = ans+'0'
        else:
            ans = ans+'1'
    return ans
