$('.contact_btn').click(function () {
    $('html, body').animate({
        scrollTop: $('.section_contact').offset().top
    }, 1000)
})
$('.section1').click(function () {
    $('html, body').animate({
        scrollTop: $('.section_info').offset().top
    }, 1000)
})
$('.section4').click(function () {
    $('html, body').animate({
        scrollTop: $('.section_tools').offset().top
    }, 1000)
})
$('.btn_scroll').click(function () {
    $('html, body').animate({
        scrollTop: $('.section_info').offset().top
    }, 1000)
})
$('.about_button').click(function () {
    $('html, body').animate({
        scrollTop: $('.section_info').offset().top
    }, 1000)
})
$('.menu_btn').click(function () {
    document.querySelector('.menu').style.transition = "all 0.5s";
    document.querySelector('.menu').style.display = "block";
    document.querySelector('.menu').style.width = "75vw";
    document.querySelector('.menu_btn').style.display = "none";
})
$('.menu_close_btn').click(function () {
    document.querySelector('.menu').style.transition = "all 0.5s";
    document.querySelector('.menu').style.display = "none";
    document.querySelector('.menu').style.width = "0";
    document.querySelector('.menu_btn').style.display = "block";
})