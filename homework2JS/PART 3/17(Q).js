// 17. Высота body 2000px. По нажатию на кнопку прокрутите страницу до самого низа.

document.body.clientHeight = '2000px'

myunique.onclick = function() {
    window.scrollTo({
        top: document.body.scrollHeight,
        behavior: "smooth"
    });
}