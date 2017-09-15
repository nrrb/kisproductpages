import json
import logging
from jinja2 import Environment, FileSystemLoader

logging.basicConfig(level=logging.INFO)

def render_template_to_file(json_source_file):
	logging.info("Reading data from " + json_source_file + "...")
	with open(json_source_file, 'rb') as f:
	    data = json.load(f)

	audience = data['audience']
	template_type = data['template_type']

	# From the data's template_type value, "laptop", "desktop", or "index", use the appropriate product template file
	if template_type == 'laptop':
	    template_file_path = 'templates/' + audience + '/laptop.jinja2'
	elif template_type == 'desktop':
	    template_file_path = 'templates/' + audience + '/desktop.jinja2'
	elif template_type == 'index':
		template_file_path = 'templates/' + audience + '/index.jinja2'
	else:
	    logging.error('The data file says the template_type is "' + template_type + '" but that\'s invalid. It should be "laptop", "desktop", or "index".')
	    exit(1)

	logging.info("Using template file " + template_file_path + ".")
	with open(template_file_path, 'rb') as f:
	    template = Environment(loader=FileSystemLoader('templates/' + audience)).from_string(f.read())

	output_path = 'output/' + audience + '/' + data['output_filename']
	logging.info("Outputting to " + output_path + ".")
	with open(output_path, 'wb') as f:
	    f.write(template.render(data))


if __name__=="__main__":
	for json_source_file in (	'data/products/faculty/T470s.json',
								'data/products/faculty/X1Carbon5thGen.json',
								'data/products/faculty/X1Yoga2ndGen.json',
								'data/products/faculty/M910tDesktop.json',
								'data/products/faculty/index.json',
								'data/products/staff/T470s.json',
								'data/products/staff/Yoga370.json',
								'data/products/staff/M910qTiny.json',
								'data/products/staff/index.json'	):
		render_template_to_file(json_source_file)
