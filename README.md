# Simple-Restaurant-Table-Reservation-System-


# Booking a table in a restaurant

#### Video Demo: [https://youtu.be/uH6qufEfmG4](https://youtu.be/-xDy-BncTcE?si=cAfg6YlxpVMhPpKc)

#### Description:
 An application to book a table in a restaurant, change your book info like the book name, and people's number based on the name that you
 Enter at the booking process, or you can cancel your booking also based on the name you enter at the booking process.
 When you are done booking, changing your book info, or canceling your book you can close the app.

 I used dictionaries to save the info on tables like table number, name of the booker, state of the table free or not ( True = not free, False = free ), and number of people who are coming ( number of chairs ).

 I made 3 main functions " booking " to book a table, " Change the book " to change the book, " Cancel the book " to cancel the book, and
 " Exiting " to close the app.

 I used 2 libraries, " sys " to close the app via the " Exit " function, and " tabulate " to print the schedules of the 4 processes" booking
 A table ", " change the book ", " cancel the book ", and " exit ".

 The info gets deleted when you close the app.

 This Python code simulates a restaurant table booking system. It offers functionalities for making reservations, modifying existing ones, and canceling bookings. The program maintains information about five tables (Table 1 to Table 5) and their booking status (available or occupied), along with the name of the person who has booked it and the number of people in their party.

 Initialization:

    The code imports the tabulate module for printing tables in a formatted way and sys for system exit.
    It creates five dictionaries (Table1 to Table5) with initial values for BookingName (empty string), BookState (False), and PeopleNumber (0).

 Main Loop:
    The main function starts an infinite loop using while True.

 Inside the loop:
    The process_menu function displays a menu of options using tabulate.
    The program prompts the user to enter a number for their desired action.
    It uses a try-except block to handle invalid input (non-numeric values).
    Depending on the user's choice (matched using a match statement), different functions are called:

    1- (Book a table):
        - The Table_menu function displays a list of tables.
        - The take_table_num function ensures a valid table number is chosen.
        - The take_inputing function gets the user's name and the number of people.
        - The Booking function updates the chosen table's dictionary with the booking information.

    2- (Change the book):
        - The get_Name function gets the name of the person whose booking needs modification.
        - The Change_the_book function iterates through tables to find the matching name.
        - If found, it prompts the user to enter new name and number of people (using take_inputing) and updates the table's dictionary.

    3- (Cancel the book):
        - Similar to option 2, it gets the name using get_Name and check_cancel_Name.
        - If found, it asks for confirmation (check_sure).
        - Upon confirmation (Cancel_the_book), it resets the table's dictionary to indicate it's available.

    4- (Exit): The Exiting function displays a goodbye message and exits the program using 'sys.exit.'

        If the user enters an invalid number, an error message is shown.

 Additional Functions :

    take_table_num: Validates the chosen table number (between 1 and 5) and ensures it's available.

    take_inputing:  Gets valid user input for name (alphabetical characters only) and number of people (positive integer).

    get_Name: Gets the user's name, ensuring it only contains alphabetical characters.

    Booking, Change_the_book, Cancel_the_book: Update the corresponding table's dictionary based on the action.

    check_cancel_Name: Checks if a name exists in any table's booking.

    check_sure: Ensures the user confirms cancellation with 'Y' or 'N'.

    process_menu and Table_menu: Display formatted menus using tabulate.
