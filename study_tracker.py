from colorama import Fore, init
init()

from plyer import notification
    
def send_notification():
    notification.notify(
        title="Study Reminder",
        message="Time to study! Future Cryptographer!💕",
        timeout=10
    )
study_hours = {}
goal = 5
print(Fore.CYAN + "Welcome Shobiye to your study tracker")
send_notification()
while True:
    print(Fore.MAGENTA +"\n === STUDY TRACKER ===")
    print("1. Add Study Session")
    print("2. View Progress")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        subject = input("Enter Subject: ")
        hours = float(input("Hours Studied: "))

        if subject in study_hours:
            study_hours[subject] += hours
        else:
            study_hours[subject] = hours

        print(f"{hours} hours added to {subject}!")

    elif choice == "2":
        print("\n=== YOUR PROGRESS ===")

        total_hours = 0

        for subject, hours in study_hours.items():
            print(f"{subject}: {hours} hours")
            total_hours += hours

        print(f"\nTotal Study Time: {total_hours} hours")

        if total_hours >= goal:
            print(Fore.GREEN + f"Congratulations🤩! You have reached your goal of {goal} hours.")
        else:
            print(Fore.RED + f"You are {goal - total_hours} hours away from your goal😡.")

    elif choice == "3":
        print(Fore.GREEN + "Goodbye! Keep studying Temmy😁!")
        break

    else:
        print("Invalid option")
