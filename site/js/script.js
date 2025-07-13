//animation scripts


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