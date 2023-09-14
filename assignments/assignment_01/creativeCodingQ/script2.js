let nextBtn = document.querySelector('#nextButton')
let btn1 = document.querySelector('#choice_01')
let btn2 = document.querySelector('#choice_02')
let playerValue = 0
let liContainer = document.querySelector('#list-container')
let firstQuestion = document.querySelector('#question1')
let subtext = document.querySelector('#questionSubtext') 
let paragraph = document.querySelector('#paragraph')
let details = document.querySelector('#questionDetail')


// Sorted by numbers so playerValue starts at 0. Key: 
// Indoor = 1, Outdoor = 2
// Relaxing = 10, Active = 20
// Indoor + relax = 11, Indoor + active = 21 
// Outdoor + relax = 12, outdoor + active = 22

function nextQuestion() {
    // Indoor
    btn1.addEventListener('click', () =>{
        playerValue = playerValue + 1
        if (playerValue === 1) {
            details.textContent = dateQuestions[1].question
            btn1.textContent = dateQuestions[1].choices[0];
            btn2.textContent = dateQuestions[1].choices[1];
            console.log(playerValue)
            
        }
        if (playerValue === 2) {
            playerValue = playerValue + 10
            console.log(playerValue)
        }
    })
    // Outdoor 
    btn2.addEventListener('click', () => {
        playerValue = playerValue + 2
        if (playerValue === 2) {
            details.textContent = dateQuestions[1].question
            btn1.textContent = dateQuestions[1].choices[0];
            btn2.textContent = dateQuestions[1].choices[1];
            console.log(playerValue)
            // Relax

            btn1.addEventListener('click', () => {
                playerValue = playerValue + 10
                console.log(playerValue)
            })

            // Active

            btn2.addEventListener('click', () => {
                playerValue = playerValue + 20
                console.log(playerValue)

            })
            // Score 24 with +2 from first btn 
        }
    })
    console.log(playerValue)
}


function startGame() {
    let playerValue  = 0
    let questionCounter = 0
    let chosenButton = nextBtn
    
    
    chosenButton.addEventListener('click', () => { 
        nextBtn.style.display = 'none'
        btn1.style.display = 'block'
        btn2.style.display = 'block'
        if (questionCounter < dateQuestions.length) {
            details.textContent = dateQuestions[questionCounter].question
            btn1.textContent = dateQuestions[questionCounter].choices[0];
            btn2.textContent = dateQuestions[questionCounter].choices[1];
            console.log(dateQuestions[questionCounter])
            questionCounter++
            nextQuestion()
        } 
        
    })
}
startGame()

// let questionIndex = 0; // Keep track of the current question

// function changeText() {
//     btn1.style.display = 'none'
//     btn2.style.display = 'none'
//     nextBtn.addEventListener('click', () => {
//         if (questionIndex < dateQuestions.length) {
//             btn1.style.display = 'block'
//             btn2.style.display = 'block'
//             details.textContent = dateQuestions[questionIndex].question;
//             btn1.textContent = dateQuestions[questionIndex].choices[0];
//             btn2.textContent = dateQuestions[questionIndex].choices[1];
//             questionIndex++;
//         } else {
//             // Handle end of questions or reset if needed
//             // For example, you can reset the questionIndex to 0 to start over
//             // questionIndex = 0;
//         }
//     });
// }

// changeText();