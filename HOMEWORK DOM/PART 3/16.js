// 16. Дан input. Дана кнопка. По нажатию на кнопку клонируйте этот input и вставляйте рядом

// creating input and buttin via Js
let input1 = document.createElement('input')
let button1 = document.createElement('button')
button1.innerHTML = 'Button'

document.body.appendChild(input1)
document.body.appendChild(button1)


// creating event handler
let eventHandler = function() {
    let newInput = input1.cloneNode()
    document.body.insertBefore(newInput, button1)
}


// adding event handler
button1.onclick = eventHandler
