from flask import Flask, render_template, request
import re
import bleach

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template('index.html')
    else:
        name = request.form["name"]
        lastname = request.form["lastname"]
        email = request.form["email"]
        country = request.form["country"]
        message = request.form["message"]
        gender = request.form["gender"]
        option = request.form["option"] 

        nameError = False
        lastNameError = False
        messageError = False

        if name == "":
            nameError = True
        if lastname == "":
            lastNameError = True
        if message == "":
            messageError = True

        # Validations       
        if name == "" or lastname =="" or message =="":
            return render_template('index.html', nameError=nameError, lastNameError=lastNameError, messageError=messageError)
        
        if validate_email(email):
            return render_template('index.html', emailformaterror=True)
        
        # Sanitization
        sanitedName = bleach.clean(name)
        sanitedLastName = bleach.clean(lastname)
        sanitedEmail = bleach.clean(email)
        sanitedCountry = bleach.clean(country)
        sanitedMessage = bleach.clean(message)
        sanitedGender = bleach.clean(gender)
        sanitedOption = bleach.clean(option)

    
        return render_template('success.html', sanitedName=sanitedName, sanitedLastName=sanitedLastName, sanitedEmail=sanitedEmail, sanitedCountry=sanitedCountry, sanitedMessage=sanitedMessage, sanitedGender=sanitedGender, sanitedOption=sanitedOption)


def validate_email(email):
    # Regular expression for validating an email address
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$'
    
    # Match the email with the regex
    if re.match(email_regex, email):
        return True
    else:
        return False