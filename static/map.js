function initMap() {
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 14,
        center: {lat: 51.5195786, lng: -0.0606907}
    });

    var vehiclesData = document.getElementById('vehicles-data').value;
    var vehicles = JSON.parse(vehiclesData);
    
    // Array to store markers
    var markers = []; 

    for (var i = 0; i < vehicles.length; i++) {
        var vehicle = vehicles[i];
        var marker = new google.maps.Marker({
            position: {lat: vehicle.latitude, lng: vehicle.longitude},
            map: map,
            icon: 'car.webp',
            title: vehicle.place
        });
       // Store the marker in the array
        markers.push(marker); 
    }

}
