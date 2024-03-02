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
    if (amount > 1) {
        $n.val(amount - 1);
    }
});
