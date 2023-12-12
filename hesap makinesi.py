num1 = int(input("birinci sayiyi girin: "))
num2 = int(input("ikinci sayiyi girin: "))
process = input('toplama için 1 \nÇikarma için 2 \nÇarpma için 3 \nBölme için 4\n')

if process == '1':
    result = num1 + num2
elif process == '2':
    result = num1 - num2 
elif process == '3':
    result = num1 * num2 
elif process == '4':
    result = num1 / num2 
else :
    print("bir şeyler ters gitti")  

print(result)   