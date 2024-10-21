from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash  # Import hashing functions
from database.models import get_user_collection, get_weather_data_collection
from weather.weather_api import WeatherAPI
from weather.data_processor import WeatherDataProcessor
from weather.alerts import WeatherAlerts

app = Flask(__name__)
app.secret_key = '95953f0e91c64f0a3c33c17485798124'

# Initialize API and Processor
weather_api = WeatherAPI()
data_processor = WeatherDataProcessor()
weather_alerts = WeatherAlerts()

@app.route('/')
def home():
    return render_template('home.html')  # Render the home page

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        users_collection = get_user_collection()
        
        # Retrieve user and check password
        user = users_collection.find_one({'email': email})
        if user and check_password_hash(user['password'], password):  # Check hashed password
            session['user_email'] = email
            
            return redirect(url_for('dashboard'))
        else:
            return "Invalid credentials", 401
    return render_template('login.html')

@app.route('/register', methods=['POST'])
def register():
    email = request.form['email']
    password = request.form['password']
    
    users_collection = get_user_collection()
    
    # Check if the user already exists
    if users_collection.find_one({'email': email}):
        return "Email already exists", 409
    
    # Hash the password before saving
    hashed_password = generate_password_hash(password)  # Use default hashing method

    # Save the new user to the database
    users_collection.insert_one({'email': email, 'password': hashed_password})
    session['user_email'] = email
            
    return redirect(url_for('dashboard'))

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'user_email' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        city = request.form['city']
        data = weather_api.get_weather_data(city)
        processed_data = data_processor.process_data(data)
        
        # Save processed data in MongoDB
        weather_data_collection = get_weather_data_collection()
        if processed_data:
            weather_data_collection.insert_one(processed_data)  # Insert data into MongoDB
            
        return render_template('dashboard.html', data=processed_data)
    
    return render_template('dashboard.html')

@app.route('/logout')
def logout():
    session.pop('user_email', None)  # Remove user email from session
    return redirect(url_for('home'))  # Redirect to home page


if __name__ == '__main__':
    app.run(debug=True)
