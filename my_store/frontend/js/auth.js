function saveAuth(data) {
  localStorage.setItem('access_token',  data.access  || data.token);
  localStorage.setItem('refresh_token', data.refresh || '');
  localStorage.setItem('user', JSON.stringify(data.user || {}));
}

function clearAuth() {
  localStorage.removeItem('access_token');
  localStorage.removeItem('refresh_token');
  localStorage.removeItem('user');
}

function isLoggedIn() {
  return !!localStorage.getItem('access_token');
}

function getUser() {
  return JSON.parse(localStorage.getItem('user') || '{}');
}

function requireAuth() {
  if (!isLoggedIn()) {
    window.location.href = 'login.html';
  }
}

function updateNavbar() {
  const navAuth = document.getElementById('nav-auth');
  if (!navAuth) return;
  if (isLoggedIn()) {
    const user = getUser();
    navAuth.innerHTML = `
      <span style="color:#666;font-size:14px">Hi, ${user.username || 'User'}</span>
      <a href="orders.html">My Orders</a>
      <a href="#" onclick="logout()">Logout</a>
    `;
  } else {
    navAuth.innerHTML = `
      <a href="login.html">Login</a>
      <a href="register.html">Register</a>
    `;
  }
}

function logout() {
  clearAuth();
  window.location.href = 'index.html';
}