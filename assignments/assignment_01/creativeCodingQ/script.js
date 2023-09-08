let nextBtn = document.querySelector('#next1')
let liContainer = document.querySelector('#list-container')
let firstQuestion = document.querySelector('#question1')
let subtext = document.querySelector('#questionSubtext') 



function nextQuestion() {
    const newQ = document.createElement("div")
}


//This is saying that each time the next button is clicked, it will check if active or relaxing is clicked. 
nextBtn.addEventListener('click', () => {
    const question1 = document.querySelector('input[name="dateType"]:checked').value;
    console.log(question1)

// Then this part is saying, if active is clicked run through the array of active indoor activities and return it as clickable list items.

    if (question1 === 'active' || question1 === 'relaxing') {
        inOrOutOptions.forEach(option => {
            
            let inOrOut = document.createElement('button')
            inOrOut.textContent = option
            liContainer.append(inOrOut)
            console.log(liContainer.innerText)
            if (liContainer.textContent === 'IndoorsOutdoors') {
                console.log('true')
                subtext.textContent = ''
                nextBtn.style.display = 'none'
                firstQuestion.style.display = 'none'
            }
        });
    }

    // console.log(question1)
})


// This is the code for looping through activities to pick 

//   activeIndoorActivities.forEach(activity => {
//             let listItems = document.createElement('button')
//             listItems.textContent = activity
//             liContainer.append(listItems)
//         });