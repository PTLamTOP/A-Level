/*3. Проверка на номер. Создать input и каждый раз, когда пользователь печатает текст. 
Проверять на то, что внутри input только число. Если там только число, то светить текст зеленым, если не только число, то светить красным. PS. color: red, green | 
Проверять через setInterval*/


// QUESTION

let inputEl = document.getElementById('input')
let value = Number(inputEl.value)

setInterval(() => {
    (value === NaN ) ? inputEl.style.color='red': inputEl.style.color='green'
}, 10)