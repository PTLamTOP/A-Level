// 6. Дан элемент #myunique. Проверьте наличие у него класса www.

let element = document.getElementById('myunique')

// adding class
element.className = 'www.'

// checking if class is existed
alert(element.classList.contains('www.'))
alert(element.classList.contains('hello'))