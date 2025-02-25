const container = document.querySelector('.container');
const registerBtn = document.querySelector('.register-btn');
const loginBtn = document.querySelector('.login-btn');
document.addEventListener('DOMContentLoaded',  function () {
    let xd = document.getElementById('alerta')
    console.log("entro ");
    if (xd ){
        console.log("entro2 ");
        container.classList.add('active');
    }
})

registerBtn.addEventListener('click', () => {
    container.classList.add('active');
})

loginBtn.addEventListener('click', () => {
    container.classList.remove('active');
})