def calculator(a,b,operation):
    if operation == "add" :
        return a+b
    elif operation == "subtract":
        return a-b
    elif operation == "multiply":
        return a*b
    elif operation == "devide":
        if b == 0 :
            return "Erroe"
        else:
            return a/b
    else:
        return "invalid operation"
    
print(calculator(5,6,"add"))    
print(calculator(22,10,"subtract"))    
print(calculator(5,6,"multiply"))    
print(calculator(5,0,"devide"))    
print(calculator(5,1,"devide")) 
print(calculator(5,6,"ad"))    


    
    
    