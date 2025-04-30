"""
If you're familiar with Flask, build a basic web app with a single endpoint like
/weather?city=London, which returns weather info (based on your API from Task 1). You can
return results in JSON or display in a simple HTML page.

"""
from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# Mock function simulating weather data
def get_weather_data(city):
    # In a real scenario, this would query a weather API
    mock_data = {
        "London": {"temperature": "15°C", "description": "Cloudy"},
        "New York": {"temperature": "10°C", "description": "Sunny"},
        "Paris": {"temperature": "12°C", "description": "Rainy"}
    }
    return mock_data.get(city, {"error": "City not found"})

@app.route('/weather')
def weather():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "Please provide a city"}), 400
    
    weather_data = get_weather_data(city)

    # If the request accepts JSON, return JSON
    if request.headers.get("Accept") == "application/json":
        return jsonify({"city": city, "weather": weather_data})
    
    # Otherwise, render as simple HTML
    if "error" in weather_data:
        html_content = f"<h2>Error: {weather_data['error']}</h2>"
    else:
        html_content = f"""
            <h2>Weather in {city}</h2>
            <p>Temperature: {weather_data['temperature']}</p>
            <p>Description: {weather_data['description']}</p>
        """

    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(debug=True)
