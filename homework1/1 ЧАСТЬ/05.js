//05. Сформируйте строку вида ".#.#.#.#.#." с помощью цикла for.

// 1 variant
let arr = ['.#', '.#', '.#', '.#', '.#.']
string = ''
for (var element of arr) {
  string += element
}

// 2 variant
str = ''
arr.reduce(function(prev, current) {
    str = prev+current
    console.log(str)
    return str
})