


#ini adalah string formating dalam Python 3.6


size_in_meters = int(input("Please input the zie of your house: "))

print(size)
size_in_meters = size_in_feet/10.8

#Mencetak menggaunakan template format

template  = "Your house in feet is {} that is {:.2f} in meters" #perhatikan cara formatting floating number disini.
template = template.format(size_in_feet, size_in_meters)
print(template)

