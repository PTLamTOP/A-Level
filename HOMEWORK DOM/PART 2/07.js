// 7. Дан элемент #myunique. Добавьте ему класс www, если его нет и удалите - если есть. | Вы зарание не знаете, есть тамм этот класс или нету

let element = document.getElementById('myunique7')

// checking if class 'www' is existed. add/remove
if (element.classList.contains('www')) {
    element.classList.remove('www')
} else {
    element.classList.add('www')
}