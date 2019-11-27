// Даны элементы с классом www$, $ - это инкремент. Добавьте каждому элементу в конец, название его тега в нижнем регистре, при нажатии каждый раз.

// creating elemts via JS
for(let i = 1; i<10; i++) {
    let elem = document.createElement('p')
    elem.classList.add('www')
    elem.style.cursor = 'pointer'
    elem.innerHTML = `p${i}`
    document.body.appendChild(elem)
}

// getting all elements in list
let elemListHTML = document.getElementsByClassName('www')
let arrJS = Array.from(elemListHTML)


// creating event handler
let eventHandler = function(event) {
    let TagName = event.target.tagName
    let currentInnerText = event.target.innerText
    let newInnerText = `${currentInnerText}${TagName.toLowerCase()}`
    event.target.innerHTML = newInnerText
}


// adding event handler via loop
arrJS.forEach(elem => {elem.onclick = eventHandler})
