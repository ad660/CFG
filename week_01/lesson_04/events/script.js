const button = document.querySelector('#button')
const username = document.querySelector('#username')
const password = document.querySelector('#password')
const correctPassword = 'correctPass'

// Checks if users password is correct 

// If correct console.log (yes) / If incorrect console.log (no)

button.addEventListener('click', (e) => {
    usernameInput = username.value
    passwordInput = password.value
    if (passwordInput === correctPassword) {
        console.log('You have logged on')
    }
    else if (passwordInput === '') {
        console.log("Please enter a password")
    }
    else (
        console.log("You are trying to hack me")
    )
})