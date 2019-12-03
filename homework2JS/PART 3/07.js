/* 7. Создать button и повесить обработчик нажатие. По нажатию на кнопку должно поменться ее текст. По умолчанию Кнопка. После нажатие Кирпич
*/

// creating element by js
let button1 = document.createElement('button')
button1.innerHTML = 'Кнопка'
button1.id = 'button1'
document.body.appendChild(button1)

// event handler
let changingButton = function(event) {
    event.target.innerHTML = 'Кирпич'
}

// adding event handler to button
button1.onclick = changingButton