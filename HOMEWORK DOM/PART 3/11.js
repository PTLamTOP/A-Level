// Дан элемент с верстке с id #myunique. Добавьте ему класс www, если есть, то удалить класс.

//creating element via js
let elemTest = document.createElement('p')
elemTest.id = 'myunique'
elemTest.innerHTML = 'Click me'
elemTest.style.cursor = 'pointer'
document.body.appendChild(elemTest)


// event handler function
let eventHandler = function(event) {
    let classListHTML = event.target.classList
    let arrayClassList = Array.from(classListHTML)
    
    if (!arrayClassList.includes('www')) {
        alert(`Class 'www' was added`)
        event.target.classList.add('www')
    } else {
        alert(`Class 'www' was deleted`)
        event.target.removeAttribute('class')
    }
        
}


// adding event handler to element
elemTest.onclick = eventHandler