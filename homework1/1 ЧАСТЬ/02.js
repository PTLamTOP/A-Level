/* 02. Создайте три переменные с любыми числовыми значениями. 
Используя условный оператор  и не используя логические, найдите минимальное число и отобразите на экране имя переменной и ее значение*/

let number1 = 50
let number2 = 20
let number3 = 30

if (number1>number2) {
    if (number1>number3) {
        console.log(number1)
    } else {
        console.log(number3)
    }
} else if (number2>number3) {
    console.log(number2)
} else {
    console.log(number3)
}