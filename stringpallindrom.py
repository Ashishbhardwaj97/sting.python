def rev(s):
    return s[::-1]
    
def pal(s):
    r = rev(s)
    
    if s==r:
        return True
    return False
    
s= "dad"
ans= pal(s)

if ans==1:
    print("pallindrom")
    
else:
    print("not pallindrom")

