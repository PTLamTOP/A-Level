/* 6. Создать button и повесить обработчик нажатие. По нажатию на кнопку должно выдать alert('Hey')
*/

// creating element by js
let button1 = document.createElement('button')
button1.innerHTML = 'Кнопка'
button1.id = 'button1'
document.body.appendChild(button1)

// event handler
let changingButton = function(event) {
    alert('Hey')
}

// adding event handler to button
button1.onclick = changingButton