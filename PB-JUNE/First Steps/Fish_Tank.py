#Inputs describe the dimensions of an aquarium in cm
length = int(input())
width = int(input())
height = int(input())
percent = float(input()) / 100

volume = ((length * width * height) - ((length * width * height) * percent)) / 1000

print(volume)
