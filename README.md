# Banking-System-python 
#video presentation
https://drive.google.com/file/d/1FEW8Z9TiwT6U2fAYMoyJSHLlvJquBC0-/view?usp=sharing

## Explanation

Logging into your existing account, creating a new account, to know balance of the account, to deposit the cash, to withdraw the cash are the features that are included in this code. 

In-built modules that are inserted here is 'random', and 'sys'. User-defined module name is 'details'. The function defined in the random module is randint(), which help to generate a random integer between initial number and final number. From the module sys the function defined in the code is exit(), which is to exit from the running command. Here, the data structure called from the user-defined module 'details' is 'Account', which is a dictionary. The dictionary contains a set of private data of each and every person that have account in that certain bank. 

Another important feature that added to this code is data handling. Data handling method adopted mainly for handling the data like editing the code in the different file. The changes that made in the file named 'details' from 'banking system' (both files' extensions are .py) are updating the account balance of the user after they deposit or withdraw their cash, append the details of the new user who is creating a new account. 

The classes created here is named as Bank and has many methods. Seven methods are been introduced in this class. First method is __init__() which gives accessibility to run in different methods of that class i.e., every other method can read as well as run the body of __init__(). Next method is login() which analyse the correctness of the username and password that entered by the user. The method home() shows the list of options the user might need and they will be redirected to the page according to their selection. The method home() may redirected to the methods like deposit() which is for depositing the cash, withdraw() for withdrawing the cash, balance() for knowing the account balance. A person with no accounts can create a new account by proceeding to the method new_account(). The function used for log out or exit is exit().
