/*3. Проверка на номер. Создать input и каждый раз, когда пользователь печатает текст. 
Проверять на то, что внутри input только число. Если там только число, то светить текст зеленым, если не только число, то светить красным. PS. color: red, green | 
Проверять через setInterval*/


// QUESTION

input.oninput = function() {
    if (isNaN(input.value) == true) {
        input.style.color = 'red'
    } else {
        input.style.color = 'green'
    }
}