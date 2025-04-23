"""
code

Description:
"""

# Initial data: List of guests and their RSVP status
guests = ["Sir-Meows-A-Lot", "Mr. Whiskers", "Lady Glitter", "Fluffy Snowball"]
rsvp = ["Confirmed", "Confirmed", "Pending", "Pending"]

# Show current guest list and RSVP status
print("\nCurrent RSVP Status:")
i = 0
while i < len(guests):
    print(guests[i], "-", rsvp[i])
    i += 1

# Ask user if they'd like to RSVP
user = input("\nWould you like to RSVP for this cat celebration? (yes/no): ").strip().lower()

if user == "yes":
    user_name = input("Please enter your name: ").strip().title()  # Format name with title case
    
    if user_name in guests:
        print("Hello, " + user_name + "! Your current RSVP status is " + rsvp[guests.index(user_name)] + ".")
        update_status = input("Would you like to update your RSVP status? (yes/no): ").strip().lower()
        
        if update_status == "yes":
            new_rsvp = input("Enter your new RSVP status (Confirmed/Pending): ").strip().capitalize()
            while new_rsvp != "Confirmed" and new_rsvp != "Pending":
                print("Invalid RSVP. Please enter 'Confirmed' or 'Pending'.")
                new_rsvp = input("Enter your new RSVP status (Confirmed/Pending): ").strip().capitalize()
            rsvp[guests.index(user_name)] = new_rsvp
            print("Your RSVP has been updated to " + new_rsvp + ".")
    
    else:
        add_user = input("Sorry, " + user_name + ", you're not on the list. Add yourself? (yes/no): ").strip().lower()
        if add_user == "yes":
            guests.append(user_name)
            new_rsvp = input("Enter your RSVP status (Confirmed/Pending): ").strip().capitalize()
            while new_rsvp != "Confirmed" and new_rsvp != "Pending":
                print("Invalid RSVP. Please enter 'Confirmed' or 'Pending'.")
                new_rsvp = input("Enter your RSVP status (Confirmed/Pending): ").strip().capitalize()
            rsvp.append(new_rsvp)
            print("Welcome, " + user_name + "! You have been added with RSVP status " + new_rsvp + ".")

# Show updated guest list and RSVP status
print("\nUpdated RSVP Status:")
i = 0
while i < len(guests):
    print(guests[i], "-", rsvp[i])
    i += 1
