name = "umer"
ticket_price = 50.00
destination = "New York"
is_available = True
number_of_tickets = 5

print("Name:", name)
print("Ticket Price: $", ticket_price)
print("Destination:", destination)
print("Available?", is_available)
print("Number of Tickets:", number_of_tickets)

total_cost = ticket_price * number_of_tickets
print("Total Cost: $", total_cost)
print("Discounted Price: $", ticket_price - 10.00)


print("is ticket price under 500$:", ticket_price < 500)
print("is the destination New York? :", destination == "New York")
print("is the number of tickets more than 3? :", number_of_tickets > 3)

plane_ticket_price = 50.00
train_ticket_price = 30.00
print("Before:", plane_ticket_price, "and", train_ticket_price)

print("Traveling to " + destination + " with " + str(number_of_tickets) + " tickets at a total cost of $", total_cost)





