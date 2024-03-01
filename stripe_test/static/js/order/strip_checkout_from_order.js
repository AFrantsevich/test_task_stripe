var stripe = Stripe('pk_test_51Oo6AZG0uu3kb43DoXtaM7xxTXl8do6HM66L1UmO9NXaV0FZe66n69dtB3CVkR5wymIYMXZvNA55EDSc3isXFFXs00JMsUlM8N');
var buyButton = document.getElementById('buy-button');
buyButton.addEventListener('click', function() {
    fetch('/payment_order/', {
            method: 'GET'
        })
        .then(function(response) {
            return response.json();
        })
        .then(function(session) {
            return stripe.redirectToCheckout({
                sessionId: session.sessionId
            });
        })
});