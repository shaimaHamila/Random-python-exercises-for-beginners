weight = input("weight: ")
l_or_k = input("(l)bs or (k)g: " )
if l_or_k.upper() == 'L' :
    weight_bs = float(weight)* 0.45
    print("you are" + str(weight_bs) + " kilos" )
elif l_or_k.upper() == 'K' :
    weight_g = float(weight) / 0.45
    print(f"you are {weight_g} pounds" )