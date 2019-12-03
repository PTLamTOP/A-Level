//И так же при попадании на разные круги были разные звуки по дереву или же того, что вы придумаете.(В пределах разумного)
let audio1 = document.getElementById('audio1')
let audio2 = document.getElementById('audio2')
let audio3 = document.getElementById('audio3')
let audio4 = document.getElementById('audio4')
setTimeout(function() {
    document.getElementById("audio").play()
}, 1000);


// Закрепляем картинку дротика на движение мышки. document.body как цель для событие onmousemove, так как будет на все body браузера.
document.body.onmousemove = function (event) {
    dart.style.position = 'absolute'
    dart.style.top = `${event.clientY - 100}px` // clientY - положение мышки пользователя по Y
    dart.style.left = `${event.clientX}px` // clientX - положение мышки пользователя по X
}

// Обработчик событие при нажатие мышки на круги, с подсчетом баллов
round1.onclick = function (event) {
    let current = Number(result.innerText)
    setTimeout(function () {
        audio1.play() // звук при попадание в мишешь
        current += 10
        result.innerText = current
    }, 800)
}

round2.onclick = function (event) {
    let current = Number(result.innerText)
    setTimeout(function () {
        audio2.play() // звук при попадание в мишешь
        current += 8
        result.innerText = current
    }, 800)
}

round3.onclick = function (event) {
    let current = Number(result.innerText)
    setTimeout(function () {
        audio3.play() // звук при попадание в мишешь
        current += 5
        result.innerText = current
    }, 800)
}

round4.onclick = function (event) {
    let current = Number(result.innerText)
    setTimeout(function () {
        audio4.play() // звук при попадание в мишешь
        current += 2
        result.innerText = current
    }, 800)
}


// функция генератор числа от максимального к минимальному
function random(min, max) {
    return Math.round(Math.random() * (max - min) + min)
}

// задаем интервал, когда будет меняться положение мишени каждые 0,3 секунды
setInterval(function () {
    let numberX = random(20, 80)
    round1.style.left = `${numberX}%`
    round2.style.left = `${numberX}%`
    round3.style.left = `${numberX}%`
    round4.style.left = `${numberX}%`

    let numberY = random(20, 80)
    round1.style.top = `${numberY}%`
    round2.style.top = `${numberY}%`
    round3.style.top = `${numberY}%`
    round4.style.top = `${numberY}%`

}, 1000)


// Меняем картинку дротика на gift при нажатия мыши. document.body как цель для событие onclick, так как будет на все body браузера.
document.body.onclick = function () {
    // меняем курсор на gif и меняем положение
    dart.src = 'dart2.gif'
    dart.style.top = `${event.clientY-58}px` 
    dart.style.left = `${event.clientX-25}px`

    // через 0,8 секунд возвращаем обратно предыдущие параметры
    setTimeout(function() {
        dart.src = 'dart.png'
        dart.style.top = `${event.clientY - 100}px` 
        dart.style.left = `${event.clientX}px`
    }, 800)    
}

// И так же у нас ограниченное время игры. 30 секунд. Через 30 секунд игра заканчивается и мы просто играем заново(с нуля)
setInterval(function() {
    let current = Number(result.innerText)
    current = 0
    result.innerText = current
}, 30000)


/*Дополительно(обязательно) - сделать, чтобы вокруг летали птицы рандомно. Можно сделать, чтобы пели(будет плюсиком)
4 - птицы в gif формате. размерами 30на30, 30на30, 40на40, 50на50*/

setInterval(function () {
    let numberX1 = random(10, 80)
    let numberX2 = random(10, 80)
    let numberX3 = random(10, 80)
    let numberX4 = random(10, 80)
    bird1.style.left = `${numberX1}%`
    bird2.style.left = `${numberX2}%`
    bird3.style.left = `${numberX3}%`
    bird4.style.left = `${numberX4}%`

    let numberY1 = random(10, 80)
    let numberY2= random(10, 80)
    let numberY3 = random(10, 80)
    let numberY4 = random(10, 80)
    bird1.style.top = `${numberY1}%`
    bird2.style.top = `${numberY2}%`
    bird3.style.top = `${numberY3}%`
    bird4.style.top = `${numberY4}%`

}, 1000)




