/* jshint esversion: 8, jquery: true */
// Show toast messages
$('.toast').toast('show');

// Scroll to page top button
$('.top-link').click(function(e) {
    window.scrollTo(0,0);
});

$(function(){
    setTimeout(function(){
        $('.message-container').fadeOut(1000)
    }, 3000)
})
