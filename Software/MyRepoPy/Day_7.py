def check_pal(x):
    x = x.replace(' ','')
    return x == x[::-1]