def countRange(list, min, max):
    output = []
    list = [input("enter numbers: ") for i in range(int(input("enter n: ")))]
    min, max = float(input("enter min: ")), float(input("enter max: "))
    for i in range(len(list)):
        if round(float(list[i])) in range((int(min)),int(max)):
            output.append(list[i])  
    return(output)

print(countRange(list, min, max))