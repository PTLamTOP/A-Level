// 15. Дан ol. По нажатию на любой li, эта li удалялась.

// creating ol with li, button via JS
let ol1 = document.createElement('ol')
document.body.appendChild(ol1)

for(let i=1; i<10; i++) {
    let elemLi = document.createElement('li')
    elemLi.innerHTML = `li${i}`
    elemLi.style.cursor = 'pointer'
    ol1.appendChild(elemLi)
}

// getting li as js array
let listOfLi = document.getElementsByTagName('li')
let arrLi = Array.from(listOfLi)



// creating event handler
let eventHandler = function(event) {
    ol1.removeChild(event.target)
}

// adding event handler to button
arrLi.forEach(elem => elem.onclick = eventHandler)