/*6. Делаем функцию $(), которая может принимать аргументом название класса, айди или название просто тега.
Если это тег, то ишем по тегу и выводим эти елементы, которые мы нашли. Если это айди, то ишем по айди. Если это класс. 
Тоооо, если на сайте несколько таких класов, возварашаем как массив елементов, который нашли, если только один клас, то возвараем просто один елемент не в массиве!*/


let elem;

// Function
let getElem = (name) => {
    if (name.slice(0, 1) === '#') { // check if it is ID
        elem = document.getElementById(name.slice(1)).innerText
        alert(elem)
    } else if (name.slice(0, 1) === '.') { // check if it is class
        let arr = document.getElementsByClassName(name.slice(1))
        Array.from(arr).forEach((element) => {
            alert(element.innerText)
        })
    } else { // if it is not ID and class, it is tag
        let arr = document.getElementsByTagName(name)
        Array.from(arr).forEach((element) => {
            alert(element.innerText)
        })
    }
}

// Testing
getElem('div')
getElem('#id')
getElem('.class')
