const BASE_URL = 'https://my-store-vaa0.onrender.com/api';

function getToken() {
  return localStorage.getItem('access_token');
}

function getAuthHeaders() {
  return {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + getToken()
  };
}

async function getProducts(search = '') {
  const url = search
    ? BASE_URL + '/products/?search=' + encodeURIComponent(search)
    : BASE_URL + '/products/';
  const res = await fetch(url);
  return res.json();
}

async function getProduct(id) {
  const res = await fetch(BASE_URL + '/products/' + id + '/');
  return res.json();
}

async function login(username, password) {
  const res = await fetch(BASE_URL + '/auth/login/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ username, password })
  });
  return { ok: res.ok, data: await res.json() };
}

async function register(username, email, password, password2) {
  const res = await fetch(BASE_URL + '/auth/register/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ username, email, password, password2 })
  });
  return { ok: res.ok, data: await res.json() };
}

async function placeOrder(items) {
  const res = await fetch(BASE_URL + '/orders/', {
    method: 'POST',
    headers: getAuthHeaders(),
    body: JSON.stringify({ items })
  });
  return { ok: res.ok, data: await res.json() };
}

async function getOrders() {
  const res = await fetch(BASE_URL + '/orders/', {
    headers: getAuthHeaders()
  });
  return res.json();
}