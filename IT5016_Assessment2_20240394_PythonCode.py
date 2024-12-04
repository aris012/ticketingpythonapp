#Help desk ticketing system

#Tickets array
open_tickets = []
closed_tickets = []
reopened_tickets = []
ticket_number = 2000

#Creating ticket user input

def create_ticket(ticket_number):
    staff_id = input("Staff ID: ")
    creator_name = input("Ticket creator name: ")
    contact_email = input("Contact email: ")
    issue_description = input("Description of the issue: ")

    if issue_description.lower() == "password change":
        new_password = staff_id[:2] + creator_name[:3]
        status = "Closed" 
        response = f"New generated password: {new_password}"
    else:
        status = "Open"
        response = "Not Yet Provided"

    ticket_details = {
        "Ticket Number": ticket_number,
        "Staff ID": staff_id,
        "Ticket Creator": creator_name,
        "Email address": contact_email,
        "Description": issue_description,
        "Response": response,
        "Status": status
    }

    return ticket_details

#display ticket statistics with the use of lenght function

def display_ticket_statistics():
    total_tickets_created = len(open_tickets) + len(closed_tickets) + len(reopened_tickets)
    total_tickets_resolved = len(reopened_tickets) + len(closed_tickets)
    total_tickets_solved = len(open_tickets)
    print("Tickets Created:", total_tickets_created)
    print("Ticket Resolved:", total_tickets_resolved)
    print("Ticket to Solve:", total_tickets_solved)

#Print ticket lists 

def print_tickets(ticket_list):
    for ticket in ticket_list:
        print()
        print("Ticket Number:", ticket["Ticket Number"])
        print("Staff ID:", ticket["Staff ID"])
        print("Ticket Creator:", ticket["Ticket Creator"])
        print("Email address:", ticket["Email address"])
        print("Description:", ticket["Description"])
        print("Response:", ticket["Response"])
        print("Status:", ticket["Status"])
        print()

while True:
    print()
    print("HELP DESK TICKETING SYSTEM")
    print()
    ticket_number += 1
    ticket = create_ticket(ticket_number)
    if ticket["Status"] == "Closed":
        closed_tickets.append(ticket)
    elif ticket["Status"] == "Resolved":
        reopened_tickets.append(ticket)
    else:
        open_tickets.append(ticket)

    print(f"Ticket {ticket_number} created successfully!")
    print()
    print("Display Ticket Statistics")
    display_ticket_statistics()
    print()
    print("Printing Tickets")
    print()
    all_tickets = open_tickets + closed_tickets + reopened_tickets
    all_tickets_sorted = sorted(all_tickets, key=lambda x: x["Ticket Number"])
    print_tickets(all_tickets_sorted)
