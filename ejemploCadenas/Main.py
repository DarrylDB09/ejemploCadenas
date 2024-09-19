text1 = "Fundamentos con "
text2 = "Python"
#text 5 da error por que es de tipo numerico
result = text1 + text2
print (result)

nombre = "Darryl"
apellido = "Bolaños"
fullName = nombre + " " + apellido
print (fullName)

price = 97
text3 = f"The price is {price:.2f} dollars"
print(text3)

text4 = f"La multiplicacion es {20*59}"
print(text4)

text5 = "python es un lenguaje de alto nivel de programacion"
result1 = text5.capitalize()
print(result1)

texto6 = "Cien Años de Soledad"
titleConvert = texto6.casefold()
print(titleConvert)

fruit = "banana"
textCenter = fruit.center(20, "-")
print (textCenter)

title1 = "I love apples, apple are my favorite fruit"
result2 = title1.count("apple")
print(result2)

text6 = "Curso, fundamentos con Python."
result3 = text6.endswith(".")
print(result3)

#secuencia de escape
letter = "F\tU\tP"
letterScape = letter.expandtabs(2)
print(letterScape)

text7 = "Hola, bienvenidos a Colombia."
resul4 = text7.find("bienvenidos")
print(resul4)

text8 = "welcome to my wordl"
result5 = text8.title()
print(result5)

alphanumeric = "Python312"
result6 = alphanumeric.isalnum()
print(result6)

letters = "Space X"
result7 = letters.isalpha()
print(result7)