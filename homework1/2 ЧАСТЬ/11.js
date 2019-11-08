/*11. Напишите скрипт, который считает количество секунд в часе, в сутках, в месяце.
Спрашиваем у пользователя через prompt число.
Если пользователь ввёл 10h, то мы выводим ему количество секунд за 10 часов.
Если пользователь ввёл 10d, то мы выводим ему количество секунд за 10 дней.
Если пользователь ввёл 10w, то мы выводим ему количество секунд за 10 недел.
Если пользователь ввёл 10m, то мы выводим ему количество секунд за 10 месяц.
Проверяем то, что в конце)*/

let value = prompt('Give me a value(h, d, w, m): ')

let number = parseInt(value)
if (value.includes('h')) {
  result = number * 60 * 60
  alert(value + ' in seconds is:' + result.toString())
} else if (value.includes('d')) {
  result = number * 24 * 60
  alert(value + ' in seconds is:' + result.toString())
} else if (value.includes('w')) {
  result = number * 24 * 7 * 60
  alert(value + ' in seconds is:' + result.toString())
} else if (value.includes('m')) {
  result = number * 24 * 30 * 60
  alert(value + ' in seconds is:' + result.toString())
}
