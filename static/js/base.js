/* jshint esversion: 8, jquery: true */
// Show toast messages
$('.toast').toast('show');

// Scroll to page top button
$('.top-link').click(function(e) {
    window.scrollTo(0,0);
});

$(document).ready(function() {
    // messages timeout for 10 sec 
    setTimeout(function() {
        $('.message-container').fadeOut('slow');
    }, 5000);
