str1 = input("Enter time in this format HH:MM:SS AM/PM  ")
if str1[-2:] == 'AM' and str1[:2] == "12":
    print ("00" + str1[2:-2])
elif str1[-2:] == "AM":
    print (str1[:-2])
elif str1[-2:] == "PM" and str1[:2] == "12":
    print (str1[:-2])
else:
    print (str(int(str1[:2]) + 12) + str1[2:8])
input("Enter any key to exit")