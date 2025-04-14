#Function for Leet Translation
def leet(message) :

    message = message.lower()
    message = message.replace("a","@")
    message = message.replace("e","3")
    message = message.replace("i","1")
    message = message.replace("o","0")
    message = message.replace("s","$")
    message = message.replace("u","'-'")

    return message

print("Leet Translator V1.0 💻")
print("Enter any message you want to convert it into leet")
#Ask user for input & Store input into a variable
msg = input("Enter the message : ").strip()
#Pass it to a function
conversion = leet(msg)
#return the leet version using only string methods
print("Hacker Mode:", conversion)

input("Press enter to exit...")