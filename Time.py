import time
timestamp = time.strftime('%H.%M')
# https://docs.python.org/3/library/time.html#time.strftime

# timestamp = input("Enter the time in this format (00.00): ")
if timestamp == '00.00':
  print("Good night")
  
elif '0.01' >= timestamp <= '06.00':
   print ("It's Night")
elif '06.01' >= timestamp <= '12.00':
  print("Good Morning")

elif timestamp == '12.00':
  print("Good noon")
  
elif '12.01' >= timestamp <= '16.00':
   print ("Good Afternoon")

elif '16.01' >= timestamp <= '19.00':
  print ("Good Evening")

elif '19.01' >= timestamp <= '24.00':
  print ("Good Evening")