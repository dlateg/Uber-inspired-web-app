function initMap() {
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 14,
        center: {lat: 51.5195786, lng: -0.0606907}
    });

    // Get the vehicles data from the hidden input field
    var vehicles = document.getElementById('vehicles-data').value;
    var vehicles = JSON.parse(vehicles);

    // Array to store markers
    var markers = [];
    const image = "https://apollo-media.codio.co.uk/media%2F1%2F9a9ed3e3e1ee96baf9da3e47d4570c5c-0e41f5b92e883928.webp";

    for (var i = 0; i < vehicles.length; i++) {
        var vehicle = vehicles[i];
        var marker = new google.maps.Marker({
            position: {lat: vehicle.latitude, lng: vehicle.longitude},
            map: map,
            icon: image
        });

        // Store the marker in the array
        markers.push(marker);
    }
}

// Call the initMap function when the Google Maps script is loaded
function loadMap() {
    initMap();
}
