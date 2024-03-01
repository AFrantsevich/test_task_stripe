$(document).ready(function() {
    $(".send-quantity").click(function() {
        var id = $(this).data("id");
        var quantity = $(this).closest('.card-body').find(".input-qty").val();

        console.log($(this));
        $.ajax({
            url: "/add/",
            data: {
                'id': id,
                'quantity': quantity,
            },
        });
    });
});
