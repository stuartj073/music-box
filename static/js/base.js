/* jshint esversion: 8, jquery: true */
// Show toast messages
$('.toast').toast('show');

// Scroll to page top button
$('.top-link').click(function(e) {
    window.scrollTo(0,0);
});


$(function() {
    $('.message-container').fadeIn(5000, function() {
        $(this).fadeOut(2000)
    });
});
