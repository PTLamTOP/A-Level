//01. Напилите кодец, который работает с массивом произвольных целых чисел
var numbers = [ 254, 115, 78, 25, 91, 45, 37 ]

// 1 variant
for (i=0; i < numbers.length; i++) {
  if (numbers[i] > 50) {
    console.log(numbers[i])
  } 
}

// 2 variant
for (var element of numbers) {
  if (element > 50) {
    console.log(element)
  }
}

// 3 variant 

numbers.forEach(function(element, key, array) {
    console.log(`${key}: ${element} from array [${array}]`)
})
