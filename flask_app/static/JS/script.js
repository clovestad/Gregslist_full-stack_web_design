var map = L.map('map').setView([39.945088, 262.421494], 3.5);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

function onMapClick(e) {
    alert( e.latlng);
}

map.on('click', onMapClick);

var marker = L.marker(onMapClick(e)).addTo(map);


