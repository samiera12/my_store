function getCart() {
  return JSON.parse(localStorage.getItem('cart') || '[]');
}

function saveCart(cart) {
  localStorage.setItem('cart', JSON.stringify(cart));
  updateCartCount();
}

function addToCart(product, qty = 1) {
  const cart = getCart();
  const existing = cart.find(i => i.id === product.id);
  if (existing) {
    existing.qty += qty;
  } else {
    cart.push({
      id:    product.id,
      name:  product.name,
      price: parseFloat(product.price),
      image: product.image_url,
      qty:   qty
    });
  }
  saveCart(cart);
  alert(product.name + ' added to cart!');
}

function removeFromCart(productId) {
  const cart = getCart().filter(i => i.id !== productId);
  saveCart(cart);
}

function clearCart() {
  saveCart([]);
}

function getCartTotal() {
  return getCart().reduce((sum, i) => sum + i.price * i.qty, 0);
}

function updateCartCount() {
  const badge = document.getElementById('cart-count');
  if (!badge) return;
  const total = getCart().reduce((sum, i) => sum + i.qty, 0);
  badge.textContent = total;
  badge.style.display = total > 0 ? 'inline' : 'none';
}