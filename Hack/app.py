import os
import json
import rasterio
from rasterio import warp
import folium
from folium.plugins import HeatMap
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

raster_path = "./Prediction/model/example.tif"
with rasterio.open(raster_path) as dataset:
    min_x, min_y, max_x, max_y = dataset.bounds
    center_x = (min_x + max_x) / 2
    center_y = (min_y + max_y) / 2
    dst_crs = 'EPSG:4326'
    center_lon, center_lat = warp.transform(dataset.crs, dst_crs, [center_x], [center_y])
    center_lon = center_lon[0]
    center_lat = center_lat[0]

with open('./Prediction/data/disasters.json') as f:
    disaster_data = json.load(f)

years = sorted([int(year) for year in disaster_data.keys()])

def generate_map(selected_year):
    m = folium.Map(location=[center_lat, center_lon], zoom_start=5)
    disasters = disaster_data.get(str(selected_year), [])
    fg = folium.FeatureGroup(name=f"Year {selected_year}")
    heat_data = []
    for disaster in disasters:
        lat = disaster["latitude"]
        lon = disaster["longitude"]
        deaths = disaster["Total Deaths"]
        if deaths > 0:
            heat_data.append([lat, lon, deaths])
        popup_text = (
            f"<strong>Total Deaths:</strong> {deaths}<br>"
            f"<strong>Disaster type:</strong> {disaster['Disaster type']}<br>"
            f"<strong>Disaster subtype:</strong> {disaster['Disaster subtype']}<br>"
            f"<strong>Appeal:</strong> {disaster['Appeal']}"
        )
        folium.Marker(location=[lat, lon], popup=popup_text).add_to(fg)
    fg.add_to(m)
    if heat_data:
        HeatMap(
            heat_data,
            gradient={"0.1": "blue", "0.3": "lime", "0.5": "yellow", "0.7": "orange", "1": "red"},
            min_opacity=0.05,
            max_opacity=0.9,
            radius=25,
            blur=15,
            use_local_extrema=False
        ).add_to(m)
    map_dir = "./Prediction/maps"
    if not os.path.exists(map_dir):
        os.makedirs(map_dir)
    map_path = os.path.join(map_dir, f"disaster_map_{selected_year}.html")
    m.save(map_path)
    return map_path

@app.route("/")
def index():
    initial_year = years[0]
    map_file = generate_map(initial_year)
    with open(map_file, "r") as f:
        map_html = f.read()
    return render_template("index.html", initial_year=initial_year, years=years, map_html=map_html)

@app.route("/api/update_map", methods=["GET"])
def update_map():
    selected_year = request.args.get("year", type=int)
    if selected_year not in years:
        return jsonify({"error": "Invalid year"}), 400
    map_file = generate_map(selected_year)
    with open(map_file, "r") as f:
        map_html = f.read()
    return map_html

if __name__ == "__main__":
    app.run(debug=True)
