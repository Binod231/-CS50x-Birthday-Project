This project is based on the CS50x Problem Set: Birthdays, part of Harvard University's Introduction to Computer Science course.
The original problem requires building a simple Flask web application to manage a list of birthdays. 
The application allows users to add, view, and delete birthdays stored in a SQLite database.

Core Features (As Required by the Problem Set)

Add Birthdays:
Users can add a new birthday by entering a name, month, and day.
The data is validated to ensure all fields are filled before being stored in the SQLite database.

View Birthdays:
A table displays all the birthdays stored in the database, showing the name and date (month/day).

Delete Birthdays:
Users can delete a specific birthday from the database using a "Delete" button.

Edit Birthdays:
You implemented an "Edit" feature that allows users to update an existing birthday's name, month, or day.
The /edit/<int:id> route handles both GET and POST requests:
GET: Displays a pre-filled form with the current birthday details.
POST: Updates the birthday in the database after validating the input.

Responsive Design:
You added responsive CSS to ensure the application works well on different screen sizes, including mobile devices.
Features like full-width forms, scalable buttons, and scrollable tables improve usability on smaller screens.

Improved Error Handling:
You added validation to ensure that all fields (name, month, and day) are filled before adding or editing a birthday.
If validation fails, the user is shown an appropriate error message.

Dynamic Page IDs:
You passed a body_id variable to templates to allow page-specific styling using CSS.

![Screenshot 2025-04-05 072908](https://github.com/user-attachments/assets/015d1873-8989-45e0-b568-9d5702c7d005)
![Screenshot 2025-04-05 072920](https://github.com/user-attachments/assets/30beb325-708b-4a7a-917a-7baa1a35dee2)
![Screenshot 2025-04-05 073015](https://github.com/user-attachments/assets/97a96f63-f148-4fb1-8d59-db2f91441e84)


