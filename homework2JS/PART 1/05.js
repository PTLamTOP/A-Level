/*5. Нужно взять и сделать функцию getInnerTextOfElement, которая принимает в качестве аргумента название например '#name'. 
То внутри делает поиск по getElementById и берет innerText и возварашает. НЕ МОЖНО использовать querySelector. 
Првоверяете аргумент. Начинается на точку или на #, чтобы вызвать тот метод, который вам нужен.*/

// Function 
let getInnerTextOfElement = (idName) => {
    let idFixed = idName.slice(1) //remove #
    let element = document.getElementById(idFixed)
    let text = element.innerText
    return text
}


// Test
getInnerTextOfElement('#i')