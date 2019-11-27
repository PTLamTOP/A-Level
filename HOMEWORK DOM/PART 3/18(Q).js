// 18. Дан элемент #myunique. По клику на него увеличьте его ширину и высоту и шрифт в 2 раза. Делайте это анимировано.

// creating elem
let elemTest = document.createElement('p')
elemTest.id = 'myunique'
elemTest.innerHTML = 'Hello world!'
elemTest.style.cursor = 'pointer'
elemTest.style.width = '50px'
elemTest.style.height = '50px'
elemTest.style.fontSize = '10px'
document.body.appendChild(elemTest)


// creating event handler
let eventHandler = function(event) {
    let elemWidth = event.target.style.width 
    let elemHeight = event.target.style.height
    let elemFontSize = event.target.style.fontSize
    event.target.style.width  = `${parseInt(elemWidth)*2}px`
    event.target.style.height = `${parseInt(elemHeight)*2}px`
    event.target.style.fontSize = `${parseInt(elemFontSize)*2}px`
}

// adding event handler
elemTest.onclick = eventHandler