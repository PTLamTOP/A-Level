/*31. Задание на МС.  Создайте пустой массив. В цикле до n на каждой итерации запускайте prompt для ввода любых символов, 
полученное значение добавляйте в конец созданного массива. 
После выхода из цикла посчитайте сумму всех чисел массива и выведите в alert полученный результат*/
let arr = []
let number = 10


for (i=0; i < number; i++) {
    let character = prompt('Please input something!')
    arr.push(character)
}

let result = 0

arr.filter(function(element) {
    return !isNaN(Number(element))
}).forEach(function(element) {
    result += Number(element)
})
alert(result)