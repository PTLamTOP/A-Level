// Дан элемент с верстке с id #myunique. Добавьте ему класс www. при нажатии через js.

//creating element via js
let elemTest = document.createElement('p')
elemTest.id = 'myunique'
elemTest.innerHTML = 'Click me'
elemTest.style.cursor = 'pointer'
document.body.appendChild(elemTest)


// event handler function
let eventHandler = function(event) {
    alert('Class was added')
    event.target.classList.add('www')
}


// adding event handler to element
elemTest.onclick = eventHandler