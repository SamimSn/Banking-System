# Bank
### Video Demo: https://youtu.be/8mPty25KYek
#
### Description:
This is a simple 3-layer-architectured bank simulator software : <br>
- .txt filing as DataBase: (Bank_Account_TXT class)<br>
- Domain: (Bank_Account class)<br>
- Text-based User Interface: (Bank_Account_TUI class)<br>

There's also a test_project.py file that tests some of my software's functionalities.

No pip installation was needed in my project.

You can do the followings in the implemented software:
- print one individual or all accounts in the system
- create/update/delete an account
- sort all accounts by balance or birth date
- calculate point(s) for individual or total of accounts
- deposit money into an account
- save/load txt files as the data base
#
I chose to have a special design in my constructor, which is about the given id. If the input for id is 0, the software will handle it auto-generated; However if the user inputs any other number than 0, then the given id sets to that instance of Bank_Account.
#
I supposed that building an OOP system would be a great solution to designing much more complex environments.
#
I prefer text files to store my data rather than csv. Because the assigned datas are more readable to humen. This helps anyone understand what number or string means in my text file of accounts.<br>
Having a persistance layer advances the software's score higher. Why? well, what if the software crashes during runtime. All the data stored in memory would be gone. However saving them in a seperate file defend my data in a more secure way.
