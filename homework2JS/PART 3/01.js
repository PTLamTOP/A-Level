// 1. Даны ссылки. Привяжите всем ссылкам событие - каждый раз по наведению на ссылку в конец атрибута title запишется ее текст
let yt = document.getElementById('yt')
let fb = document.getElementById('fb')
let ig = document.getElementById('ig')

let oldTitle = document.title
let mouseOut = function() {
    document.title = oldTitle
}

yt.onmouseover = function(event) {
    event.preventDefault()
    document.title = oldTitle + ' ' + yt.innerText
    yt.onmouseout = mouseOut
}

fb.onmouseover = function(event) {
    event.preventDefault()
    document.title = oldTitle + ' ' + fb.innerText
    fb.onmouseout = mouseOut
}

ig.onmouseover = function(event) {
    event.preventDefault()
    document.title = oldTitle + ' ' + ig.innerText
    ig.onmouseout = mouseOut
}

