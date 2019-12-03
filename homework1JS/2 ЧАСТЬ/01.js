/*1. Напишите код вычисления суммы всех нечетных чисел от 0 до заданного числа N
- Спрашиваем у пользователя через prompt
- Переводим в number(потому что из prompt мы получаем строку)
- Дальше думаем сами
В конце просто я должен увидеть сумму от 0 до N числа, который я ввёл*/

let number = +prompt('Give me a number: ')
let arr = []

for (let i=0; i < number; i++) {
  if (i%2!==0) {
    arr.push(i)
  }
}

// 1 variant

let result1 = 0;
for (element of arr) {
  result1 += element
}


// 2 variant
let result2 = 0
arr.reduce(function(prev, current) {
    result2 = prev + current
    return result2
})