centimes = int(input("Veuillez entrer le nombre de centimes que vous avez : "))

print("Vous avez", centimes, "centimes, pour faire cette somme il faut :")
print("- Soit",centimes//2, "pièces de 2 centimes et restera donc", centimes%2, "pièces de 1 centime")
print("- Soit",centimes//5, "pièces de 5 centimes et restera donc", centimes%5, "pièces de 1 centime")
print("- Soit",centimes//10, "pièces de 10 centimes et restera donc", centimes%10, "pièces de 1 centime")
print("- Soit",centimes//20, "pièces de 20 centimes et restera donc", centimes%20, "pièces de 1 centime")
print("- Soit",centimes//50, "pièces de 50 centimes et restera donc", centimes%50, "pièces de 1 centime")