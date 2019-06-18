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
    $('.menu').toggleClass("open", 500);

})
$('.menu_close_btn').click(function () {
    $('.menu').toggleClass("open");
})