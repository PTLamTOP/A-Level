//0. http://doc.a-level.com.ua/javascript-types-expression-conditions-logic-homework1

//0. Number: age. promp and alert
let age = prompt('Please let me know your age: ')
alert(age)


//0. Number: temperature. prompt
let tempCelc = prompt('Please input temparature in °C: ')
let tempFar = ((tempCelc * 9/5) + 32)


//0. Number: divide
let number1 = prompt('Number one is : ')
let number2 = prompt('Number two is: ')

function divide(number1, number2) {
  result = number1/number2
  console.log(Math.floor(result))
}
divide(number1, number2)


//0. Number: odd
let number3 = prompt('Please input odd number: ')
let isNumber = number(number3)

if (isNumber%2!==0) {
  console.warn('Выведите четное число или нет!')
}


//0. String: greeting
let name = prompt('What is your name?')
alert(`Nice to meet you ${name}!`)


//0. String: greeting. String: lexics
let str = prompt('Please input text: ')
let strLower = str.toLowerCase()
let badWordArray = ['ass', 'shit', 'fuck you']

for (element of badWordArray) {
  if (strLower.includes(element)) {
    console.log(`${element} is bad word!!!`)
  }
}


//0. Confirm
// confirm is function which ask user for confirmation. Return true if user click 'OK', false if user click 'cancel'
let result = confirm('Click OK if ok')
if (result) {
    return true
} else {
    return false
}


//0. Boolean
let answer1;
let question1 = confirm('Yes/No?')

if (question1) {
  answer1 = 'Yes'
} else {
  answer1 = 'No'
}


//0. Boolean: if
let answer2;
let question2 = confirm('Вы мужчина?')

if (question2) {
  answer2 = 'Вы мужчина'
} else {
  answer2 = 'Вы женщина'
}


//0. Array: plus
let arr1 = [1, 2]
arr1.push(arr1[0]+arr1[arr1.length-1])
console.log(arr1)


//0. Array: plus string
let arr2 = ['hello', 'Dude', '!']
let arrPlus = arr2[0] + arr2[1] + arr2[2]
arr2.push(arrPlus)



//0. Object: real
let obj = {
  name: 'Lam',
  secondName: 'Pham Tung',
  sex: 'man',
}

obj.secondName = 'Pham'
obj['name'] = 'PTLam'