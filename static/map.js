function initMap() {
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 12,
        center: {lat: 51.5195786, lng: -0.0606907}
    });

    var vehicles = JSON.parse('{{ vehicles|safe }}');

    for (var i = 0; i < vehicles.length; i++) {
        var vehicle = vehicles[i];
        var marker = new google.maps.Marker({
            position: {lat: vehicle.latitude, lng: vehicle.longitude},
            map: map,
            icon: 'static/car.webp',
            title: vehicle.place
        });
    }
    
}
