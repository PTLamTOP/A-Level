// Привязать всем ссылка событие onclick - при нажатие дописывается ее href в круглых скобках. Внутри по умолчанию должно быть https://google.com. Самый короткий код не больше 100 символов на одной строке.

//creating element a via JS
for (let i=1; i<=20; i++) {
    let elem = document.createElement('a')
    elem.href = 'https://google.com'
    elem.innerHTML = 'link'
    document.body.appendChild(elem)
}


let AElements = document.getElementsByTagName('a')
let arrA = Array.from(PElements)


let eventHandler = function (event) {
    event.preventDefault()
    event.target.innerHTML = `${event.target.innerText} (${event.target.href})`
}


arrA.forEach(function(){
    elem.onclick = eventHandler
})
