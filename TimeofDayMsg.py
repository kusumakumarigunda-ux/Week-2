hour = int(input("Enter Hour (0-23): "))
if hour < 6:
     print("GOOD MORNING")
elif hour > 12:
     print("GOOD AFTERNOON")
else:
     print("GOOD NIGHT")
