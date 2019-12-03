// 11. Даны элементы с классом www. Добавьте каждому элементу в конец название его тега в нижнем регистре.

let elements = document.getElementsByClassName('www')


elements.array.forEach(element => {
    let elementText = element.innerText
    let newText = `${elementText} ${element.tagName}`
    element.innerHTML = newText
});


myunique.classList.forEach(function(elm) {
	if (elm == 'www') {
        document.getElementsByClassName(elm)[0].innerText += myunique.tagName.toLowerCase()
    } else {
		console.log(false)
	}
});