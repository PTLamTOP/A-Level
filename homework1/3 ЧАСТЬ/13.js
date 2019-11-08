/*13. Дана строка 'aaa bbb ccc'. Вырежите из нее слово 'bbb' тремя разными способами (через substr, substring, slice).*/
let str = 'aaa bbb ccc'
let strSubstr = str.substr(4, 3)
let strSubstring = str.substring(7, 4)
let strSlice = str.slice(4, 7)