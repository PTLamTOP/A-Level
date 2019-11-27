let id = dart

function default_state(id) {
    id.src = 'http://boxtutor.com/images/dart-png-13.png'
    id.width = '60'
    id.height = '40'
    id.style.position = 'absolute'
    return id.src, id.width, id.height, id.style.position
}

function flying_state(id) {
    dart.src = 'http://boxtutor.com/images/animated-clipart-darts-9.gif'
    dart.width = '120'
    dart.height = '120'
    id.style.position = 'absolute'
    return id.src, id.width, id.height, id.style.position
}

document.body.onmousemove = function(e) {
    dart.style.position = 'absolute'
    if (dart.src == 'http://boxtutor.com/images/animated-clipart-darts-9.gif') {
        dart.style.top = `${e.clientY-70}px`
        dart.style.left = `${e.clientX-50}px`
    } else {
        id.style.top = `${e.clientY-8}px`
        id.style.left = `${e.clientX+1}px`
    }
}

round1.onclick = function(e) {
    flying_state(id)
    dart.style.top = `${e.clientY-70}px`
    dart.style.left = `${e.clientX-50}px`
    setTimeout(function() {
        let current = Number(count.innerText)
        current += 10
        count.innerText = current
        default_state(id)
        id.style.top = `${e.clientY-8}px`
        id.style.left = `${e.clientX+1}px`
    }, 800)
    let x = document.getElementById("dart_sound")
    setTimeout(function() {
        x.play();
    }, 500)
}

round2.onclick = function(e) {
    flying_state(id)
    dart.style.top = `${e.clientY-70}px`
    dart.style.left = `${e.clientX-50}px`
    setTimeout(function() {
        let current = Number(count.innerText)
        current += 8
        count.innerText = current
        default_state(id)
        id.style.top = `${e.clientY-8}px`
        id.style.left = `${e.clientX+1}px`
    }, 800)
    let x = document.getElementById("dart_sound")
    setTimeout(function() {
        x.play();
    }, 500)
}

round3.onclick = function(e) {
    flying_state(id)
    dart.style.top = `${e.clientY-70}px`
    dart.style.left = `${e.clientX-50}px`
    setTimeout(function() {
        let current = Number(count.innerText)
        current += 5
        count.innerText = current
        default_state(id)
        id.style.top = `${e.clientY-8}px`
        id.style.left = `${e.clientX+1}px`
    }, 800)
    let x = document.getElementById("dart_sound")
    setTimeout(function() {
        x.play();
    }, 500)
}

round4.onclick = function(e) {
    flying_state(id)
    dart.style.top = `${e.clientY-70}px`
    dart.style.left = `${e.clientX-50}px`
    setTimeout(function() {
        let current = Number(count.innerText)
        current += 2
        count.innerText = current
        default_state(id)
        id.style.top = `${e.clientY-8}px`
        id.style.left = `${e.clientX+1}px`
    }, 800)
    let x = document.getElementById("dart_sound")
    setTimeout(function() {
        x.play();
    }, 500)
}

function random(min, max) {
    return Math.round(Math.random() * (max - min) + min)
}

setInterval(function() {
    let numberX = random(0, 80)
    round2.style.left = `${numberX}%`
    round3.style.left = `${numberX}%`
    round4.style.left = `${numberX}%`
    round1.style.left = `${numberX}%`

    let numberY = random(0, 80)
    round1.style.top = `${numberY}%`
    round2.style.top = `${numberY}%`
    round3.style.top = `${numberY}%`
    round4.style.top = `${numberY}%`
}, 400)

setInterval(function() {
    let bird1X = random(0, 100)
    let bird1Y = random(0, 100)
    birdy1.style.left = `${bird1X}%`
    birdy1.style.top = `${bird1Y}%`

    let bird2X = random(0, 100)
    let bird2Y = random(0, 100)
    birdy2.style.left = `${bird2X}%`
    birdy2.style.top = `${bird2Y}%`

    let bird3X = random(0, 100)
    let bird3Y = random(0, 100)
    birdy3.style.left = `${bird3X}%`
    birdy3.style.top = `${bird3Y}%`
}, 1000)

var seconds = document.getElementById("countdown").textContent;
var countdown = setInterval(function() {
    seconds--;
    document.getElementById("countdown").textContent = seconds;
    document.getElementById("jungle_sounds").play()
    if (seconds <= 0) window.location.reload(true);
}, 1000);