# CyberShield

## Student Project

**Student Name:** Bhakti Kundalik Avhad  
**Course:** B.Sc. Information Technology - Second Year  
**College:** SCB College of Arts & Commerce, Churchgate  
**University:** SNDT Women's University, Mumbai

## About the Project

CyberShield is a simple web-based cybersecurity awareness project. It helps a user understand two common security topics:

1. Password strength
2. Phishing messages

The project uses simple rules instead of advanced machine learning. The purpose is to demonstrate programming, web development and database concepts learned during the B.Sc. IT course.

## Technologies Used

- Python
- Flask
- HTML
- CSS
- MySQL

## Main Modules

### 1. Password Check
The program checks password length, uppercase letters, lowercase letters, numbers and special characters.

### 2. Phishing Check
The program checks a message for common words such as urgent, verify, OTP, prize, click and account.

### 3. MySQL Database
The result of each check is saved in the MySQL database.

### 4. Dashboard
The dashboard displays recent scan results.

## How to Run

1. Install Python and MySQL.
2. Open CMD inside the CyberShield folder.
3. Create a virtual environment:

   python -m venv venv

4. Activate it:

   venv\Scripts\activate

5. Install packages:

   pip install -r requirements.txt

6. Open `schema.sql` in MySQL Workbench and run it.
7. Open `app.py`.
8. Replace `YOUR_MYSQL_PASSWORD` with your MySQL password.
9. Run:

   python app.py

10. Open:

   http://127.0.0.1:5000

## Student Note

This project is made for educational purposes. It is a rule-based awareness tool and is not a professional cybersecurity scanner.

Do not enter real passwords or private information.
