def is_inside(toado,hcn):
    if hcn[0] <= toado[0] <= hcn[0] + hcn[2] and hcn[1] <= toado[1] <= hcn[1] + hcn[3]:
        return True
    else:
        return False
toado = [200,120]
hcn = [140,60,100,200]

if is_inside(toado,hcn):
    print("Your function is correct")
else:
    print("Oops, there's a bug")


