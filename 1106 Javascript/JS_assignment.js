const value = document.getElementById('value')
const btn1 = document.getElementById('btn1')
const btn2 = document.getElementById('btn2')

number = parseInt(value.innerHTML);

function plus(){
    number+=1;
    value.innerHTML = number;
}

function minus(){
    number-=1;
    value.innerHTML = number;
}

btn1.addEventListener('click', plus);
btn2.addEventListener('click', minus);