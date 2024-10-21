
# weather/alerts.py

class WeatherAlerts:
    def __init__(self):
        self.thresholds = {}

    def set_threshold(self, city, threshold):
        self.thresholds[city] = threshold

    def check_alert(self, city, temperature):
        if city in self.thresholds:
            if temperature > self.thresholds[city]:
                return True  # Alert condition met
        return False
