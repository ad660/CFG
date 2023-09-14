options = [
    {
        choice_00: 'You and 3 friends are in a cabin in the woods but suddenly, all the electricity goes out...you hear a chilling noise amongst the strong wind outside. Do you investigate?',
        options: ['Go investigate the noise', 'Stay inside and lock the door']
    },
    {
        choice_01: 'You have entered the woods, the wind rushes past you, you hear a low growl coming from your right',
        options: ['follow the sound', 'go in the opposite direction'],
        dependsOn: 'Go investigate the noise'
    },
    {
        choice_02: 'You stay indoors and lock them behind you, your friends break out the whiskey for a drinking game',
        options: ['Drink with your friends, the door is locked anyways', 'Refrain from drinking, something does feel right...'],
        dependsOn: 'Stay inside and lock the door'
    },
    {
        choice_03: 'Suddenly you see something move out of the corner of your eye, all of your friends are having fun, you seem to be the only one whose noticed it',
        options: ['ignore it, you\'re drunk anyways it\'s probably nothing', 'Go investigate'],
        dependsOn: 'Drink with your friends, the door is locked anyways'
    },
    {
        choice_04: 'Suddenly, what looks like a man in fur dashes across the window...it happened so quickly...maybe it was nothing and I\'m being paranoid...',
        options: ['trust '],
        dependsOn: 'Refrain from drinking, something does feel right...'

    }
]