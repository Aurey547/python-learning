study_hours ={}
print("Welcome Shobiye to your study tracker")
while True:
  print("\n === STUDY TRACKER ===")
  print("1. Add Study Session")
  print("2. View Progress")
  print("3. Exit")

choice = input("Choose an option: ")

if choice == "1"
 subject = input("Enter Subject")
 hours = float(input("Hours Studied"))

if subject in study_hours:
   study_hours[subject] += hours
else:
  study_hours[subject] = hours

print(f"{hours} hours added to {subject}!")

elif choice = = "2":
 print("\n=== YOUR PROGESS ===")

total_hours = 0

for subject,hours in study_hours.items():
  print(f{subject}:{hours} hours")
  total_hours += hours

print(f"\nTotal Study Time: {total_hours} hours")

elif choice = = "3"
 print("Goodbye! Keep studying Temmy!)
  break

else:
 print("Invalid option")
