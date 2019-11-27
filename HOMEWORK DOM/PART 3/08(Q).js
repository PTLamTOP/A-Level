/* 8. Проверка на номер. Создать input и каждый раз, когда пользователь печатает текст. 
Проверять на то, что внутри у input только одни числа. Если там только число, то светить текст зеленым
,если не только число, то светить красным. PS. color: red, green*/

// creating input via JS
let input1 = document.createElement('input')
input1.id = 'input1'
let label1 = document.createElement('label')
label1.innerHTML = 'Input: '
label1.setAttribute('for', 'input1')
document.body.appendChild(label1)
label1.appendChild(input1)


// creating checking function
let checkingFunction = function(input) {
    let inputValue = input.value
    if (isNaN(inputValue)) {
        input.style.color = 'red'
    } else {
        input.style.color = 'green'
    }
}


// setInterval for checking every time
setInterval(checkingFunction(input1), 100)
