/*jshint esversion: 6 */

// Update the item quantity every reload
$('.update-link').click(function (e) {
    var form = $(this).prev('.update-form');
    form.submit();
});

// Remove relevant item and reload on click
$('.remove-item').click(function (e) {
    var csrfToken = "{{ csrf_token }}";
    var itemId = $(this).attr('id').split('remove_')[1];
    var size = $(this).data('size');
    var url = `/basket/remove/${itemId}`;
    var data = {
        'csrfmiddlewaretoken': csrfToken,
        'size': size
    };

    $.post(url, data)
        .done(function () {
            location.reload();
        });
});