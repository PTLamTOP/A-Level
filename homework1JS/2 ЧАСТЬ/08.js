//8. Создайте переменную str и присвойте ей значение 'Привет, Мир!'. Выведите сумму всех charCode этой переменной
let str = 'Привет, Мир!'
let summOfCharCode = 0

// 1 variant
for (element of str) {
  indexOfElem = str.indexOf(element)
  charCodeValue = str.charCodeAt(indexOfElem)
  summOfCharCode += charCodeValue
}

// 2 variant
let strArr = str.split('')
let summary = 0
strArr.forEach(function(element) {
    charCode = element.charCodeAt()
    summary += charCode
})
