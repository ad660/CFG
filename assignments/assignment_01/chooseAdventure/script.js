let welcomeMessage = document.querySelector('#welcome')
let mainParagraph = document.querySelector('#text')
let optionOne = document.querySelector('#option_1')
let optionTwo = document.querySelector('#option_2')


function nextQuestion() {
    optionOne.addEventListener('click', () =>{
        handleOptions()
    })
    optionTwo.addEventListener('click', () =>{
        handleOptions()
    })

}

function handleOptions() {

    for (let i = 1; i < options.length + 1; i++) {

        console.log(i)
    }
}

function startGame() {
    welcomeMessage.textContent = 'Welcome to the Game'
    mainParagraph.textContent = 'You and 3 friends are in a cabin in the woods but suddenly, all the electricity goes out...you hear a chilling noise amongst the strong wind outside. Do you investigate?'
    optionOne.textContent = 'Go investigate the noise'
    optionTwo.textContent = 'Stay inside and lock the door'
    nextQuestion()
}
 startGame()
