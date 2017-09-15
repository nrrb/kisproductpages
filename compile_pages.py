from __future__ import print_function
import json
from jinja2 import Template

for product_data_json in (	'data/products/faculty/T470s.json',
							'data/products/faculty/X1Carbon5thGen.json',
							'data/products/faculty/X1Yoga2ndGen.json',
							'data/products/faculty/M910tDesktop.json'	):

	print("Reading data from " + product_data_json + "...")
	with open(product_data_json, 'rb') as f:
	    data = json.load(f)

	audience = data['audience']

	# Use the product data to render the appropriate product template

	# From the data's template_type value, "laptop" or "desktop", use the appropriate product template file
	if data['template_type'] == 'laptop':
	    product_template_file = 'templates/' + audience + '/laptop.jinja2'
	elif data['template_type'] == 'desktop':
	    product_template_file = 'templates/' + audience + '/desktop.jinja2'
	else:
	    print('The data file says the template_type is "' + data['template_type'] + '" but that\'s invalid. It should be "laptop" or "desktop".')
	    exit(1)

	print("Using template file " + product_template_file + ".")
	with open(product_template_file, 'rb') as f:
	    template = Template(f.read())

	output_path = 'output/' + audience + '/' + data['output_filename']
	with open(output_path, 'wb') as f:
	    f.write(template.render(data))
	print("Output to " + output_path + ".")
