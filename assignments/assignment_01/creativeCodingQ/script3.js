let description = document.querySelector('#description')
let subtext = document.querySelector('#subtext')
let firstChoice = document.querySelector('#choice_1')
let secondChoice = document.querySelector('#choice_2')
let choiceArray = document.querySelector('#array')
let currentChoice = ''
let newSecondButton = document.querySelector('#newButton')

function handleNextOutdoors() {
    console.log('Handle Next Oudoors has been clicked')
}


function handleNextIndoors(){
    console.log(currentChoice)
    firstChoice.addEventListener('click', () => {
        // This is where they pick relaxing indoors
        console.log('You have picked a relaxing indoors date')
        subtext.textContent = 'Please pick from the following activities'
        
        
        console.log(dateOptions.indoor_activities.relaxingIndoorActivites)

        dateOptions.indoor_activities.relaxingIndoorActivites.forEach(option => {
            const relaxIndoorsArray = document.createElement('button')
            relaxIndoorsArray.textContent = option
            choiceArray.append(relaxIndoorsArray)
            choiceArray.style.display = 'block'
            firstChoice.style.display = 'none'
            secondChoice.style.display = 'none'
            
            // selectArrayItem()
        });
    })
    
}

function nextQuestion() {
    firstChoice.addEventListener('click', () => {
        console.log('You have chosen indoors');
        subtext.textContent = 'Would you like a relaxing activity or an active activity?';
        firstChoice.textContent = 'relaxing';
        secondChoice.textContent = 'active';
        handleNextIndoors();
    });

    secondChoice.addEventListener('click', () => {
        console.log('You have chosen outdoors');
        subtext.textContent = 'Would you like a relaxing activity or an active activity?';
        firstChoice.textContent = 'relaxing';
        secondChoice.textContent = 'active';
        handleNextOutdoors();
    });
}


    description.textContent = 'Welcome to the Date Picker'
    subtext.textContent = 'Please start by choosing from an option below'
    firstChoice.textContent = 'Date indoors'
    secondChoice.textContent = 'Date outdoors'
    nextQuestion()
