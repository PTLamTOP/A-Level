let button1 = document.getElementById('button1');
let button2 = document.getElementById('button2');

let displayButton = function (event) {
    event.preventDefault();
    event.target.style.display = 'none';
};

button1.onclick = displayButton;
button2.onclick = displayButton;
