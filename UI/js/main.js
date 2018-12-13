const publicRoutes = [
  {
    href: "index.html",
    classname: "active",
    title: "Home",
    text: "Home"
  },
  { href: "login.html", classname: "btn", title: "login", text: "Sign In" },
  { href: "register.html", classname: "btn", title: "register", text: "Signup" }
];
const adminRoutes = [
  {
    href: "admin.html",
    classname: "",
    title: "admin",
    text: "Admin dashboard"
  }
];
const privateRoutesRoutes = [
  {
    href: "index.html",
    classname: "active",
    title: "Home",
    text: "Home"
  },
  {
    href: "create-incident.html",
    classname: "",
    title: "New Incident",
    text: "New Incident"
  },
  { href: "profile.html", classname: "", title: "profile", text: "Profile" },
  { href: "records.html", classname: "", title: "reports", text: "Incidents" },

  { href: "logout.html", classname: "btn", title: "logout", text: "Logout" }
];

function parseJwt(token) {
  var base64Url = token.split(".")[1];
  var base64 = base64Url.replace("-", "+").replace("_", "/");
  return JSON.parse(window.atob(base64));
}

function createList(routes) {
  Object.values(routes).map(url => {
    const navul = document.getElementById("nav_list");
    const newli = document.createElement("li");
    const a = document.createElement("a");
    a.setAttribute("href", url.href);
    a.className = url.classname;
    a.innerText = url.text;
    a.setAttribute("title", url.title);
    newli.appendChild(a);
    navul.appendChild(newli);
  });
}

// Check for token
if (localStorage.jwtToken) {
  // Decode token and get user info and exp
  // Check for expired token
  const currentTime = Date.now() / 1000;
  const decoded = this.parseJwt(localStorage.jwtToken);
  // Create Routes
  createList(privateRoutesRoutes);
  if (decoded.exp < currentTime) {
    // Logout user
    // Remove token from localStorage
    localStorage.removeItem("jwtToken");
    // Redirect to login
    window.location = `${window.location.origin}/UI/login.html`;
  }
} else {
  // Create Routes
  createList(publicRoutes);
}

if (window.location.pathname !== "/UI/index.html" && !localStorage.jwtToken) {
  window.location = `${window.location.origin}/UI/login.html`;
}

class Logout {
  logOut() {
    // Remove token from localStorage
    localStorage.removeItem("jwtToken");
    // Redirect to login
    window.location = `${window.location.origin}/UI/login.html`;
  }
}

if (window.location.pathname === "/UI/logout.html") {
  const logout = new Logout();
  logout.logOut();
}
