def reverseInParentheses(inputString):
    index_left = []
    index_right = []
    
    inputString = list(inputString)
    
    for i in range(0, len(inputString)):
        if inputString[i] == "(":
            index_left.append(i)
        elif inputString[i] == ")":
            index_right.append(i)
    print(index_left)
    print(index_right)
    
    
    for i in range(0, len(index_left)): #共有幾對
        indexrange = [i for i in range(index_left[i]+1, index_right[i])]
        print(indexrange)
        for i in range(0,len(indexrange)//2):
            tempchar = inputString[indexrange[i]]
            inputString[indexrange[i]] = inputString[indexrange[len(indexrange)-1-i]]
            inputString[indexrange[len(indexrange)-1-i]] = tempchar
                
    while "(" in inputString:
        inputString.remove("(")
    while ")" in inputString:
        inputString.remove(")")
        
    result = "".join(inputString)  
    return result
        
