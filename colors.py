import random

colorList = ["red", "green", "blue"]
userFavoriteColor = ""
appFavoriteColor = colorList[random.randint(0,2)]

for color in colorList:
	answer = input("Is " + color + " your favorite color (y/n)")
	if answer == "y":
		userFavoriteColor = color
		break

print("Your favorite color is " + userFavoriteColor)

if userFavoriteColor == appFavoriteColor:
	print("Mine too!")
else:
		print("Mine is " + appFavoriteColor)
