import json
import os
from flask_simple_geoip import SimpleGeoIP
from flask import Flask
from flask import request
app = Flask(__name__)

# Set up SimpleGeoIP
app.config.update(GEOIPIFY_API_KEY='at_nlWt2rBzMMHmD1whpY8YZFDoZ893b')
geo_ip = SimpleGeoIP(app)


#RESPONSE = os.environ["RESPONSE"]

# Set up the status routes
@app.route("/status")
def root():
	ret = {
		'result': 'status'
	}

	return json.dumps(ret)

# Set up the ip routes
@app.route("/ip")
def ip():
	geo_data = geo_ip.get_geoip_data()
	keys = ['ip']
	ip_addr = {key: geo_data[key] for key in keys}
	ctr_keys = ['country', 'city']
	location = {key: geo_data['location'][key] for key in ctr_keys}
	ip_addr.update(location)
	return json.dumps(ip_addr)

if __name__ == "__main__":
	app.run()
