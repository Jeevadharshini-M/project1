from flask import Flask, render_template
import geopandas as gpd
import folium

app = Flask(__name__)

@app.route('/')
def index():
    # Load the GeoJSON files
    shelters = gpd.read_file('data/shelters.geojson')
    food_stations = gpd.read_file('data/food_stations.geojson')
    medical_centers = gpd.read_file('data/medical_centers.geojson')

    # Create a Folium map
    m = folium.Map(location=[37.7749, -122.4194], zoom_start=13)

    # Add shelters to the map
    for idx, row in shelters.iterrows():
        folium.Marker(
            location=[row.geometry.y, row.geometry.x],
            popup=row['name'],
            icon=folium.Icon(color='blue')
        ).add_to(m)

    # Add food stations to the map
    for idx, row in food_stations.iterrows():
        folium.Marker(
            location=[row.geometry.y, row.geometry.x],
            popup=row['name'],
            icon=folium.Icon(color='green')
        ).add_to(m)

    # Add medical centers to the map
    for idx, row in medical_centers.iterrows():
        folium.Marker(
            location=[row.geometry.y, row.geometry.x],
            popup=row['name'],
            icon=folium.Icon(color='red')
        ).add_to(m)

    # Save the map to an HTML file
    m.save("templates/map.html")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
