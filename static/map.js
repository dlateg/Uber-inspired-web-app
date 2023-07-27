//code adapted from google documentation 
let map;

async function initMap() {
    const { Map } = await google.maps.importLibrary("maps");
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 12,
        center: {lat: 51.5195786, lng: -0.0606907}
    });

    // Get the vehicles data from the hidden input field
    var vehiclesData = document.getElementById('vehicles-data').value;

    try {
        
        var locations = JSON.parse(vehiclesData);

    } catch (error) {
        console.error('Error parsing JSON data:', error.message);
    }

    console.log(locations);

    const image = 'static/img/car.png';
    var marker;                                                             


    locations.forEach(location => {
        const latitude = parseFloat(location.latitude);
        const longitude = parseFloat(location.longitude);
        const vehicle_id = location.vehicle_id;
    
    
        // Use latitude, longitude, and vehicle_id to create a Google Maps marker
         marker = new google.maps.Marker({
            position: { lat: latitude, lng: longitude },
            map: map,
            icon: image,
            title: vehicle_id
        });
    });
    }


initMap();
