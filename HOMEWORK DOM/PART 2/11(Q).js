// 11. Даны элементы с классом www. Добавьте каждому элементу в конец название его тега в нижнем регистре.

let elements = document.getElementsByClassName('www')


elements.array.forEach(element => {
    let elementText = element.innerText
    let newText = `${elementText} ${element.tagName}`
    element.innerHTML = newText
});