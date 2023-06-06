//This is the javascript that runs the verification of the sign up page.


/*Checking if the value of password is less than 8 
characters and if less than 8 characters, doesn't
 validate the form and asks the users to update their
  password to 8 digits and above. */




// Selecting the password input field
const password = document.querySelector('body > section > div > div > form > div:nth-child(2) > input[type=password]');

// Selecting the error message element
const passwordError = document.querySelector('body > section > div > div > form > div:nth-child(2) > input[type=password]');

// Checking if the password length is less than 8 characters
if (password.value.length < 8) {
    passwordError.innerHTML = '<b style="color: red;">Password must be at least 8 characters</b>';
} else if (password.value.length >= 8) {
    passwordError.innerHTML = '<b style="color: green;">Valid!</b>';
}


