/*18. Дана строка 'я учу javascript!'. Вырежите из нее слово 'учу' и слово 'javascript' тремя разными способами (через substr, substring, slice).*/
let str = 'ya uchu javascript!'

let uchuSubstr = str.substr(3, 4)
let uchuSubstring = str.substring(3, 6)
let uchuSlice = str.slice(3, 7)

let jsSubst = str.substr(8, 10)
let jsSubstring = str.substring(8)
let jsSlice = str.slice(8, (str.length-1))