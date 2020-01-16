    function add_option() {

        let adder = document.getElementById('adder');
        adder.parentNode.removeChild(adder);

        let counter = document.getElementById('count');
        counter.value = Number(counter.value) + 1;

        let p = document.createElement('p');
        p.className = 'card-text';

        inp = document.createElement('input');
        inp.type = 'text';
        inp.name = 'option' + counter.value;
        inp.placeholder = "Введите свой вариант ответа";
        p.appendChild(inp);

        add = document.createElement('button');
        add.type = 'button';
        add.id = 'adder';
        add.className = "btn btn-outline-success ml-2 btn-sm px-2";
        add.onclick = function() { add_option() };
        add.textContent = "+";
        p.appendChild(add);

        let cont = document.getElementById("options_container");
        cont.appendChild(p);
    }