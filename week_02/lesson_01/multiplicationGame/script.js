// Variables 
const firstRandomNumber = randomInteger()
const secondRandomNumber = randomInteger()



// Get a random number 

function randomInteger() {
    const randint = Math.floor(Math.random() * 12) + 1 
    return randint
}

// Get a second random number 

console.log(firstRandomNumber, secondRandomNumber)