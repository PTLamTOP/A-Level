/*2. Делаем функцию, которая принимает аргументом название тега и возварашает созданый тег. 
Потом Делаем функцию, которая принимает этот тег как аргумент и вставляет в body.
PS. createEl..., append...
*/

// Function for creating element
let createElem = (tag) => {
    let newTag = document.createElement(tag)
    return newTag
}

// Function for adding element in body
let appendElem = (tag) => {
    document.body.appendChild(tag)
}


// Test
let paragraph = createElem('p')
paragraph.innerHTML = 'Hello World!'
appendElem(paragraph)
