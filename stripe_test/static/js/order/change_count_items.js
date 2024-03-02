var buttonPlus = $(".qty-btn-plus");
var buttonMinus = $(".qty-btn-minus");
var incrementPlus = buttonPlus.click(function() {
    var $n = $(this)
        .parent(".col")
        .find(".input-qty");
    $n.val(Number($n.val()) + 1);
});
var incrementMinus = buttonMinus.click(function() {
    var $n = $(this)
        .parent(".col")
        .find(".input-qty");
    var amount = Number($n.val());
    1
    if (amount > 0) {
        $n.val(amount - 1);
    }
});

$(document).ready(function() {
    $(".qty-btn-plus, .qty-btn-minus").click(function() {
        var cartItemId = $(this).data("order-id");
        var id = $(this).data("id");
        var quantity = $(this).closest('.row').find(".input-qty").val();

        console.log(quantity);
        $.ajax({
            url: "/update_order_item/",
            method: "GET",
            data: {
                'id': id,
                'quantity': quantity,
                'order_id': cartItemId,
            },
            success: (data) => {

                var newTotalPrice = data.cart_item_total_price;
                var newOrderTotalPrice = data.order_total_price;
                $('.cart-item-total-price[data-cart-item-id="' + cartItemId + '"]').text(newTotalPrice);
                $('#order-total-price').text(newOrderTotalPrice);
                if (quantity == 0) {
                    location.reload();
                }
            },
            error: (error) => {
                console.log(error);
            }
        });
    });
});
