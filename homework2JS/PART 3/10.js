// Дан элемент с верстке с id #myunique. Удалите ему класс www. с атрибутом при нажатии через js.

//creating element via js
let elemTest = document.createElement('p')
elemTest.id = 'myunique'
elemTest.classList.add('www')
elemTest.innerHTML = 'Click me'
elemTest.style.cursor = 'pointer'
document.body.appendChild(elemTest)


// event handler function
let eventHandler = function(event) {
    alert(`Class 'www' was deleted`)
    event.target.removeAttribute('class')
}


// adding event handler to element
elemTest.onclick = eventHandler
