import NavLinks from "./components/layout/NavLinks";

// Initialize classes
const nav = new NavLinks();

// Initializing functions.
nav.onClick();

const button = document.getElementById("myLocation");
const x = document.getElementById("locationList");

const textarea = document.getElementById("report-address");

function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.watchPosition(showPosition);
  } else {
    x.innerHTML = "Geolocation is not supported by this browser.";
  }
}

function showPosition(position) {
  x.innerHTML =
    "Latitude: " +
    position.coords.latitude +
    "<br>Longitude: " +
    position.coords.longitude;

  textarea.value =
    "Latitude: " +
    position.coords.latitude +
    "<br>Longitude: " +
    position.coords.longitude;
}

button.addEventListener("click", a => {
  //Adding active class
  getLocation();
  a.target.className = "active";
});
