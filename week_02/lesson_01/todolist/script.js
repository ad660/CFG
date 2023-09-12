const buttonElements = document.querySelectorAll('button')
const listContainer = document.querySelector('#list-container')


const buttonElement = buttonElements[0]


buttonElement.addEventListener('click', () => {
    userInput = document.querySelector('#text').value
    const newListItem = document.createElement('li')
    newListItem.innerText = userInput
    listContainer.append(newListItem)
 

    const deleteButton = document.createElement('button')
    deleteButton.innerText = 'Delete'
    newListItem.innerText = `${userInput} `
    newListItem.append(deleteButton)
    
deleteButton.addEventListener('click', () => {
    console.log('clicked')
})
    // for (i = 0, i > )
})