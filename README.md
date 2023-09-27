# Email Management System

This Python script simulates an email management system using a `Email` class and a list called `inbox` to store email objects.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Email Class](#email-class)
- [Available Commands](#available-commands)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before you run the script, ensure you have Python installed on your system.

## Getting Started

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/email-management-system.git
   ```

2. Navigate to the project directory:

   ```bash
   cd email-management-system
   ```

3. Run the script:

   ```bash
   python email_management_system.py
   ```

## Usage

The script simulates an email management system where you can perform various actions such as reading emails, marking emails as spam, sending emails, and quitting the program. The available commands are displayed when you run the script.

## Email Class

The `Email` class is defined with the following attributes:

- `from_address`: The email address from which the email is sent.
- `is_spam`: A boolean indicating whether the email is marked as spam (initially False).
- `has_been_read`: A boolean indicating whether the email has been read (initially False).
- `email_contents`: The content of the email.

The class also includes methods to mark an email as read (`mark_as_read`) and mark an email as spam (`mark_as_spam`).

## Available Commands

- `read`: Lists unread emails and allows you to read a specific email.
- `mark spam`: Lists all emails and allows you to mark an email as spam.
- `send`: Allows you to send a new email by specifying the email address and content.
- `quit`: Exits the program.

## Contributing

Contributions are welcome! If you have any improvements or suggestions for this project, please open an issue or a pull request.
