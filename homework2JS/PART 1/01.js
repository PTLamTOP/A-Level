/*1. Создайте сами в html Картинку img с айди myimg. Потом уже в js Сделать 2 prompt. 
Где вы будете спрашивать у человека ссылку на картинку. И так же на сколько градусов повернуть. 
Проверяете, чтобы в первом промте была ссылка. А во втором было только число. 
И вставялете пять раз картину с одним и тем же рисунком и каждый раз крутите эту картинку на тот градус, что указали в промт. 

Например ввёл человек 45, то первая картинка с поворотом на 45, вторая на 90, 3 - 135 и т.д.
<img id=myimg src=ssilkaNaImgIzPrompt style=(vspomnite kak krutit v css)>
PS. rotate...*/

// Getting data
let imgSrc = prompt('Please give me URL of image:')
let rotateValue = +prompt('Please give me rotate value:')

let img = document.getElementById('myimg')
img.src = imgSrc

// Checking data and adding pictures
if (imgSrc.slice(0, 4) === 'http' && typeof rotateValue === 'number') {
    insertImgs(img, rotateValue) 
} else {
    alert('Incorrect data!!!')
} 

// Function for adding data
function insertImgs(img, rotate) {
    img.style.margin = '80px'
    for (let i=0; i<4; i++) {
        let imgNew = img.cloneNode(true)
        imgNew.style.transform = `rotate(${rotate}deg)`
        document.body.appendChild(imgNew)
        rotate += rotate
    }
}

