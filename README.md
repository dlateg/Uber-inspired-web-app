# A web app similar to uber
A web app inspired by uber that stores vehicle data in the db. User enters their location and the nearest vehicle to user's location is displayed on the map. 
The app uses flask to render the html and for the api interaction and also utilises google maps api to display the map along with markers or the path. 

Steps for running:
1. Make sure to update the google api key in config.py with your own key
2. Ensure you have atleast python 3.10.0 installed on your system
3. Clone this repository into your local
4. Install the required modules if necessary using pip (e.g pip install flask, pip install sqllite)
5. Run the app using command - > set FLASK_APP=main then - > flask run
6. Browse to http://127.0.0.1:5000/ 
