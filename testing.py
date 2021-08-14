# print ("hi")

# name = "Gio"
# age = 33

# def hello(name="Gogia", age=111):
#     return "Hello {} you are {} years old".format(name,age)


# sentence = hello()

# print (sentence)

# def tripleprint(someword):
#     return someword *3

# printdef = tripleprint("gio")

# print (printdef)


# L I S T S 


# dogs = ["Jeka", "roky", "Lula"]
# del(dogs[0])
# print (dogs)
# print (len(dogs))

# shoes = ["Spizikes", "Air Force 1", "Curry 2", "Melo 5"]

# for i in shoes:
#     print i



# L O O P S

# dogsloop = ["Jekaa", "dato22", "jeny22", "12"]

# for dog in dogsloop:
#     if len(dog) <= 4:
#         print (dog)

# for x in range(1,10):
#     print (x)


# age = 0
# while age < 10:
#     print (age)
#     age += 1

# numbers = [76, 83, 16, 69, 52, 78, 10, 77, 45, 52, 32, 17, 58, 54, 79, 72, 55, 50, 81, 74, 45, 33, 38, 10, 40, 44, 70, 81, 79, 28, 83, 41, 14, 16, 27, 38, 20, 84, 24, 50, 59, 71, 1, 13, 56, 91, 29, 54, 65, 23, 60, 57, 13, 39, 58, 94, 94, 42, 46, 58, 59, 29, 69, 60, 83, 9, 83, 5, 64, 70, 55, 89, 67, 89, 70, 8, 90, 17, 48, 17, 94, 18, 98, 72, 96, 26, 13, 7, 58, 67, 38, 48, 43, 98, 65, 8, 74, 44, 92]

# for num in numbers:
#     if num > 90:
#         print (num)



# D I C T I O N A R Y
# dogs = {
#     "Jeka": 8,
#     "Dato": 12,
#     "Jeny": 22
# }

# print (dogs)
# print (dogs["Jeka"])

words = ["PoGo","Spange","Lie-Fi"]
definitions = ["Slang for Pokemon Go","To collect spare change, either from couches, passerbys on the street or any numerous other ways and means","When your phone or tablet indicates that you are connected to a wireless network, however you are still unable to load webpages or use any internet services with your device"]


# for word in words:
#     for defin in definitions:
#         cooldictionary = {
#             word : defin
#         }
#         print (cooldictionary)


# cooldict = {}
# for i in range(0,3):
#     print (words[i])
#     cooldict[words[i]] = definitions[i]

# print (cooldict)


# C L A S S E S 


class Dog:

    def bark(self):
        print ("BARK!")


mydog = Dog()

mydog.bark()
