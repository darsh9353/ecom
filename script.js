document.addEventListener("DOMContentLoaded", updateCartCount);

function addToCart(id, name, price) {
    let cart = JSON.parse(localStorage.getItem("cart")) || [];
    cart.push({ id, name, price });
    localStorage.setItem("cart", JSON.stringify(cart));
    updateCartCount();
}

function updateCartCount() {
    let cart = JSON.parse(localStorage.getItem("cart")) || [];
    document.getElementById("cart-count").innerText = cart.length;
}

function loadCartItems() {
    let cart = JSON.parse(localStorage.getItem("cart")) || [];
    let cartItems = document.getElementById("cart-items");
    let totalPrice = 0;
    cartItems.innerHTML = "";

    cart.forEach((item, index) => {
        totalPrice += item.price;
        let li = document.createElement("li");
        li.innerText = `${item.name} - $${item.price}`;
        cartItems.appendChild(li);
    });

    document.getElementById("total-price").innerText = totalPrice;
}

function clearCart() {
    localStorage.removeItem("cart");
    updateCartCount();
    loadCartItems();
}

if (document.getElementById("cart-items")) {
    loadCartItems();
}
