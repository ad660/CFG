// Variables

const quizContainer = document.getElementById("quiz-container");
const questionElement = document.getElementById("question");
const indoorButton = document.getElementById("indoor-button");
const outdoorButton = document.getElementById("outdoor-button");
const activityContainer = document.getElementById("activity-container");

// Setting up an empty variable for answer 

let currentChoice = '';

indoorButton.addEventListener("click", () => {
    currentChoice = 'indoor';
    displayActivities(dateOptions.indoor_activities);
    // Removes buttons when finished
    outdoorButton.style.display = 'none'
    indoorButton.style.display = 'none'
});

outdoorButton.addEventListener("click", () => {
    currentChoice = 'outdoor';
    displayActivities(dateOptions.outdoor_activities);
    outdoorButton.style.display = 'none'
    indoorButton.style.display = 'none'
});


// I've passed the activites parameter into the function to make it reusable so that depending on the user selecting 
function displayActivities(activities) {
    // Clear the activity container
    activityContainer.innerHTML = '';

    // Uses ternary opperator to decide if the user selects indoor then says if they don't select indoor that, that will mean outdoor

    const activityType = currentChoice === 'indoor' ? 'relaxingIndoorActivites' : 'relaxingOutdoorActivities';
    const activityList = activities[activityType];

    if (activityList && activityList.length > 0) {
        questionElement.textContent = 'Choose an activity:';
        // Create a button for each of the activities in the array
        activityList.forEach(activity => {
            const button = document.createElement('button');
            button.textContent = activity;
            button.addEventListener('click', () => {
                quizContainer.innerHTML = `
                    <h1>Date Picker Quiz</h1>
                    <p>You selected: ${activity}</p>
                    <p>Have a great date!</p>
                `;
            });
            //Append each of the activities into the container
            activityContainer.appendChild(button);
        });
    } 
}


var checkit = dateOptions.outdoor_activities[currentChoice === 'indoor' ? 'relaxingIndoorActivities' : 'relaxingOutdoorActivities']
console.log(checkit)