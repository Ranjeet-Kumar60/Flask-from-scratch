# Markdown Preview Enhanced Flask App Example

This is a simple Flask web application that demonstrates basic routing and path parameters.

Markdown Preview Enhanced## Features

- **Home Page**: Displays a welcome message.
- **About Page**: Displays a simple about message.
- **Dynamic Welcome Page**: Accepts a name as a path parameter and displays a personalized welcome message.
- **Addition Page**: Accepts an integer as a path parameter and adds 10 to it.
- **Addition of Two Numbers**: Accepts two integers as path parameters and displays their sum.

Markdown Preview Enhanced## Routes

1. **Home Page**
   - **URL**: `/` or `/home`
   - **Description**: Displays the home page with a welcome message.
   - **Example**: 
     ```html
     Welcome to the Home Page!
     ```

2. **About Page**
   - **URL**: `/about`
   - **Description**: Displays a simple message about the page.
   - **Example**: 
     ```html
     Welcome to the About Page!
     ```

3. **Dynamic Welcome Page**
   - **URL**: `/welcome/<name>`
   - **Description**: Displays a personalized welcome message by accepting a string path parameter.
   - **Example**: 
     ```html
     Hi John, you're welcome to this Page!
     ```

4. **Addition Page**
   - **URL**: `/addition/<int:num>`
   - **Description**: Accepts an integer path parameter and adds 10 to it.
   - **Example**: 
     ```html
     Input is 5, Output is 15
     ```

5. **Addition of Two Numbers**
   - **URL**: `/addition_two/<int:num1>/<int:num2>`
   - **Description**: Accepts two integer path parameters and displays their sum.
   - **Example**: 
     ```html
     10 + 20 is 30
     ```

Markdown Preview Enhanced## Requirements

1. Python 3.x
2. Flask

<<<<<<< HEAD
Markdown Preview Enhanced## Demo
=======
## To view the output, either follow the link below or open the OUtput.gif file.
>>>>>>> 190df2b08565318abe4214371b26c3d80643a92a

https://github.com/Ranjeet-Kumar60/Flask-from-scratch/blob/main/basic_with_code/OUtput.gif

Markdown Preview Enhanced## How to Run the App

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/Ranjeet-Kumar60/Flask-from-scratch.git
