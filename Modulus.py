#01
time = int(input("How much time do you have?"))
hours = time // 60
minute = time % 60
print (f"You have {hours} hours")
print (f"You have {minute} minutes")

#02
total_minutes = int(input())
hours = total_minutes // 60
minute = total_minutes - (hours * 60)
print (f"total hours is {hours}")
print (f"total minute is {minute}")

#03
frame_count = int(input("how many frame do you have?"))
frame = frame_count // 60
remainer = frame_count % 60
if remainer == 0:
  print (f"you have {frame} frames can be used")
else:
  print (f"You have {remainer} remaining")

#04
total_cents = int(input())
dollars = total_cents // 100
cents = total_cents % dollars
print (f"dollars - {dollars}; cents - {cents}")

#05
total_cents = int(input())
tonnies = total_cents // 200
lonnies = total_cents % 200 // 100
quarters = total_cents % 100 // 25
dimes = total_cents % 25 // 10
nickles = total_cents % 10 // 5
pennies = total_cents
print (f"""{total_cents} cents is:
{pennies} - pennies
{nickles} - nickles
{dimes} - dimes
{quarters} - quarters
{lonnies} - lonnies  
{tonnies} - tonnies""")

#06
student_id = int(input("What's your student id?"))
group_number = (student_id + 5) // 5
print (f"you are in group #{group_number}")
