// Дано 20 абзацов с числами от 1 до 20. По нажатию на абзац в нем должен появится квадрат числа, которое он сожержит. Так же написать код Emmet(как генерировать 20 абзацов). Писать через let, const и стрелочная функция.
// QUESTION: emmet?

// creating p via JS
for (let i=1; i<=20; i++) {
    let elem = document.createElement('p')
    elem.innerHTML = `${i}` 
    document.body.appendChild(elem)
}


let PElements = document.getElementsByTagName('p')
let arrP = Array.from(PElements)

// function of event handler
let numberChanging = function(event) {
    let number = event.target.innerText
    let newNumber = `${Number(number)**2}`
    event.target.innerHTML = newNumber
}

// adding event handler to Ps
//arrP.forEach(elem => {elem.onclick = numberChanging})

arrP.forEach(elem => {elem.onclick = () => {elem.innerHTML = `${Number(elem.innerText)**2}`}})