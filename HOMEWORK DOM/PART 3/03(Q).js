// 3. Даны 5 ссылок. Только после трех кликов на ссылку следует убрать от нее событие, которое добавляет href в конец текста как в предыдущей задаче
//QUESTION: HOW TO ADD COUNT IN FUNCTION?

// getting element from DOM
let yt = document.getElementById('yt')
let fb = document.getElementById('fb')
let ig = document.getElementById('ig')
let gl = document.getElementById('gl')
let yn = document.getElementById('yn')

let countyt = 0
let countfb = 0
let countig = 0
let countyn = 0
let countgl = 0


// writting function for event Handler
let eventHandlerAddHref = function() {
    let oldText = event.target.innerText
    let elemHref = event.target.href 
    let newText = `${oldText} (${elemHref})`
    event.target.innerHTML = newText
}


// adding event handler to elements
yt.onclick = function (event) {
    event.preventDefault()
    if (countyt<3) {
        eventHandlerAddHref()
    } else {
        yt.removeEventListener('click', eventHandlerAddHref)
    }
    countyt += 1   
}

fb.onclick = function (event) {
    event.preventDefault()
    if (countfb<3) {
        eventHandlerAddHref()
    } else {
        fb.removeEventListener('click', eventHandlerAddHref)
    }
    countfb += 1   
}

ig.onclick = function (event) {
    event.preventDefault()
    if (countig<3) {
        eventHandlerAddHref()
    } else {
        ig.removeEventListener('click', eventHandlerAddHref)
    }
    countig += 1   
}

gl.onclick = function (event) {
    event.preventDefault()
    if (countgl<3) {
        eventHandlerAddHref()
    } else {
        gl.removeEventListener('click', eventHandlerAddHref)
    }
    countgl += 1   
}

yn.onclick = function (event) {
    event.preventDefault()
    if (countyn<3) {
        eventHandlerAddHref()
    } else {
        yn.removeEventListener('click', eventHandlerAddHref)
    }
    countyn += 1   
}
