//This is the javascript that runs the verification of the sign up page.


/*Checking if the value of password is less than 8 
characters and if less than 8 characters, doesn't
 validate the form and asks the users to update their
  password to 8 digits and above. */
const  passWord = document.querySelector ('password');

// passWord.get

if (passWord.innerHTML < 8 ){
    prompt('Please enter more than 8 characters!')
}   else if (passWord.innerHTML >= 8){
    prompt('Password valid!')
}

//


