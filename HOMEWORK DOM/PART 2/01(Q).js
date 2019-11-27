// 1. Высота body 4000px; Через каждые 3 секунды плавно крутите "ползунок" вниз и так же через секунду вверх. И так бесконечно раз
setInterval(function() {
    window.scrollTo({
        top: document.body.scrollHeight,
        behavior: "smooth"
    });
}, 3000)

setInterval(function() {
    window.scrollTo({
        top: -document.body.scrollHeight,
        behavior: "smooth"
    });
}, 1000)