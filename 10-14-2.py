def countRange(list, min, max):
    output = []
    #list = [input("enter numbers: ") for i in range(int(input("enter n: ")))]
    #min, max = float(input("enter min: ")), float(input("enter max: "))
    for i in range(len(list)):
        if round(float(list[i])) in range((int(min)),int(max)):
            output.append(list[i])  
    return(output)

print(countRange([1,2,3,4,5,6,7], 2, 6))