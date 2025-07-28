//animation scripts


//hamburguer navbar menu
var hamburguer = document.querySelector('.ham-button');
var navlinks = document.querySelector('.nav-anchors');
var menuUp = false;
hamburguer.addEventListener('click', () => {
    menuUp == false ? navlinks.style.display = "block" : navlinks.style.display = "none";
    menuUp = !menuUp;
});


//formulary label text animation
function login_focus(n){
    var labels = document.getElementsByClassName("form_label")[n];
    labels.style.color = '#1fff7c'
    labels.style.textShadow = '0px 0px 10px #1fff7c'
}
function login_blur(n){
    var labels = document.getElementsByClassName("form_label")[n];
    labels.style.color = '#313538'
    labels.style.textShadow = '0px 0px 0px'
}