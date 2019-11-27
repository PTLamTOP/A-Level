// 1. Даны 5 ссылок. Привяжите всем ссылкам событие - при клике на ссылку в конец ее текста дописывается ее href в круглых скобках

// getting element from DOM
let yt = document.getElementById('yt')
let fb = document.getElementById('fb')
let ig = document.getElementById('ig')
let gl = document.getElementById('gl')
let yn = document.getElementById('yn')


// writting function for event Handler
let eventHandlerAddHref = function(event) {
    let oldText = event.target.innerText
    let elemHref = event.target.href 
    let newText = `${oldText} (${elemHref})`
    if (!oldText.includes(elemHref)) {
        event.target.innerHTML = newText
    }
}

// adding event handler to elements
yt.onclick = eventHandlerAddHref
fb.onclick = eventHandlerAddHref
ig.onclick = eventHandlerAddHref
gl.onclick = eventHandlerAddHref
yn.onclick = eventHandlerAddHref


