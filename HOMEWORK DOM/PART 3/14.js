// 14. Дан ol. По нажатию на кнопку получите его последнего потомка и удалите его

// creating ol with li, button via JS
let ol1 = document.createElement('ol')
document.body.appendChild(ol1)

for(let i=1; i<10; i++) {
    let elemLi = document.createElement('li')
    elemLi.innerHTML = `li${i}`
    ol1.appendChild(elemLi)
}

let button1 = document.createElement('button')
button1.innerHTML = 'Remove li'
document.body.appendChild(button1)


// creating event handler
let eventHandler = function() {
    let lastLi = ol1.lastChild
    ol1.removeChild(lastLi)
}

// adding event handler to button
button1.onclick = eventHandler