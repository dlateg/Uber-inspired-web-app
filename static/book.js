let map;
let directionsService;
let directionsRenderer;


async function initMap() {
    const { Map } = await google.maps.importLibrary("maps");
    directionsService = new google.maps.DirectionsService();
    directionsRenderer = new google.maps.DirectionsRenderer();
    var mapOptions = {
      zoom:7,
      center: {lat: 51.5195786, lng: -0.0606907}
    }
    map = new google.maps.Map(document.getElementById('map'), mapOptions);
    directionsRenderer.setMap(map);
    directionsRenderer.setPanel(document.getElementById('directionsPanel'));

    calculateAndDisplayRoute();
  }
  

  function calculateAndDisplayRoute() {

    var driver = JSON.parse(document.getElementById('nearest_driver').value);
    const startLat = parseFloat(driver.latitude);
    const startLong = parseFloat(driver.longitude);
    

    const endLat = parseFloat(latitude);
    const endLong = parseFloat(longitude);
  
    
   directionsService.route(
    {
        origin: new google.maps.LatLng(startLat, startLong),
        destination: new google.maps.LatLng(endLat, endLong),
        travelMode: google.maps.TravelMode.DRIVING
    },
    function (response, status) {
        if (status === 'OK') {
            directionsRenderer.setDirections(response);
        } else {
            window.alert('Directions request failed due to ' + status);
        }
    }

    
);
    const image = 'static/img/car.png';
    var marker; 

    marker = new google.maps.Marker({
    position: { lat: startLat, lng: startLong },
    map: map,
    icon: image,
});

openModal();
    document.getElementById('driverID').innerText = driver.vehicle_id;
    document.getElementById('driverLatitude').innerText = driver.latitude;
    document.getElementById('driverLongitude').innerText = driver.longitude;
  
}

initMap()

  
