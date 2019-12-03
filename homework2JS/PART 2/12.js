// 12. Дан ol. Вставьте ему в конец li с текстом 'HELLO WORLD!'.

// getting all ol as псвевдо array
let olElem = document.getElementsByTagName('ol')

// select the first ol
let firstOl = olElem[0]

// create li with text
let liElem = document.createElement('li')
liElem.innerHTML = 'HELLO WORLD!'

// append li to ol
firstOl.appendChild(liElem)