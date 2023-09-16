let fruit = ['cherries', 'grapes', 'strawberries', 'lychees'];
let string = "This is a string for example purposes"


// Unshift adds new items to the beginning of an array and returns the length of the array


unshifted = fruit.unshift('new fruit')
console.log(unshifted)

// This returns 5 

//Shift removes the first element from an array, since the previous command added 'new fruit' to the array as the first element this means that .shift removes it and returns what it removed turning the array back it its original state. 

shift = fruit.shift()
console.log(shift)

//Split splits a string into substrings of that array. "" = splits into character " " = splits into each word " ", num = splits into the first (num) words e.g. if num = 3 then it will return 'This is a'

let newString = string.split(" ", 3)
console.log(newString)

// this returns 'this is a'


// OBJECTS
// Object methods are 

const programmingLanguanges = {
    
    frontEnd: 'Javascript', 
    backend: ['Python', 'NodeJS', 'Javascript', 'PHP'],
    loveIt: function() {
        console.log('Javascript is fun')
    },
    hateIt: function() {
        console.log('But its so damn confusing')
    }
}

// So in this instance to find an object property e.g. Python you can access it like this: 

const python = programmingLanguanges.backend[0]
console.log(python)

// As it is the first item in the array of objects
// To call an object method you can do the following: 

programmingLanguanges.loveIt();

// You dont need to console.log this as the object method itself contains a function that console.log's 'Javascipt is fun' 


// DOM EVENTS

// addeventlistener: We use this a lot in the first week it allows you to put a 'listener' on an element to have it perform an action. For example to have it do something when it is clicked with addEventListener('click') or when the mouse is hovered over with addEventListener('mouseover'). These are generally accomanped by a function

// onmouseover does what addEventListener('mouseover) does. it changes an element when you hover your mouse over it 

// onfocus: This changes an element when it is 'focused on' or clicked. This means you can set the onfocus to change an input field to a different color for example.  





