/*07. Напишите программу, которая в консоли выводит текстовое поздравление. 
Программа поздравляет того, чье имя определяется в переменной username: Happy birthday dear {{username}}, Например Happy birthday dear Maxim*/

let username = 'Lam'
function congr(username) {
  console.log(`Happy birthday dear ${username}!`)
}

congr(username)
