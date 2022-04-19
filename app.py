import flask
import folium

app = flask.Flask(__name__)

@app.route("/")
def index():
    start_coords = (23.000373101863882, 120.18625642830294)
    folium_map = folium.Map(location=start_coords, zoom_start=14)
    return folium_map._repr_html_()

if __name__ == '__main__':
    app.run()