# Banking System

## Overview
This is a console-based banking system that allows users to create accounts, perform banking transactions, and manage their finances. The project includes secure login functionality, transaction logging, and persistent storage of user and transaction data using file handling.

---

## Features

- **Account Creation:** Create a new bank account with a unique account number, password, and initial deposit.
- **Secure Login:** Users can log in using their account number and password.
- **Transactions:**
  - Deposit funds
  - Withdraw funds
  - Check account balance
- **Persistent Storage:**
  - Accounts are stored in `accounts.txt`.
  - Transactions are logged in `transactions.txt`.
- **Error Handling:**
  - Prevents invalid input, incorrect credentials, and overdrafts.

---

## File Structure

### `accounts.txt`
Stores user account details in the following format:

```
Account Number,Name,Password,Balance
123456,John Doe,password123,1500
```

### `transactions.txt`
Logs transactions in the following format:

```
Account Number,Transaction Type (Deposit/Withdrawal),Amount,Date
123456,Deposit,500,2024-12-23
```

---

## How to Run

1. **Clone the repository** or download the script (`banking_system.py`).
2. **Run the script** using Python:

```bash
python banking_system.py
```

---

## Example Console Flow

### Main Menu:
```
Welcome to the Banking System!
1. Create Account
2. Login
3. Exit
Enter your choice: 1
```

### Creating an Account:
```
Enter your name: John Doe
Enter your initial deposit: 1000
Enter a password: password123
Your account number: 123456 (Save this for login)
Account created successfully!
```

### Logging In:
```
Enter your account number: 123456
Enter your password: password123
Login successful!
```

### Performing Transactions:
#### Deposit:
```
Enter amount to deposit: 500
Deposit successful! Current balance: 1500
```

#### Withdrawal:
```
Enter amount to withdraw: 200
Withdrawal successful! Current balance: 1300
```

---

## Notes

- The account number is auto-generated.
- Passwords are stored as plaintext in `accounts.txt`. Consider implementing hashing for enhanced security.
- Extend functionality by adding features such as:
  - Account deletion
  - Enhanced input validation
  - Transaction history viewing

---

## Requirements

- Python 3.x

---

## Future Improvements

- Implement password hashing for security.
- Add single-user session management.
- Enable transaction history retrieval.
- Add unit tests to ensure code robustness.

---
