// Дан элемент с верстке с id #myunique. Узнайте количество его классов при нажатие и вставляйте в innerText

//creating element via js
let elemTest = document.createElement('p')
elemTest.id = 'myunique'
elemTest.classList.add('www', '1')
elemTest.innerHTML = 'Click me'
elemTest.style.cursor = 'pointer'
document.body.appendChild(elemTest)


// event handler function
let eventHandler = function(event) {
    let classList = event.target.classList
    let quantityClass = classList.length
    event.target.innerHTML = quantityClass
}


// adding event handler to element
elemTest.onclick = eventHandler