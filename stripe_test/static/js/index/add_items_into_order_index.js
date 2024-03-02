$(document).ready(function() {
    $(".send-quantity").click(function() {
        var id = $(this).data("id");
        var quantity = $(this).closest('.card-body').find(".input-qty").val();
        var x = Number(quantity);
                if (isNaN(x)) {
                   alert( "ONLY NUMBER!");
                   location.reload();
                }
                if (isNaN(x)) {
                  alert( "ONLY NUMBER!");
                  location.reload();
                } else if (x < 0) {
                  alert( "ONLY POSITIVE NUMBER!");
                  location.reload();
                }
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
