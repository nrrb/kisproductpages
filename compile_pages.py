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

    if template_type in ('laptop', 'desktop', 'index', 'consulting', 'bundles'):
        template_file_path = 'templates/' + audience + '/' + template_type + '.jinja2'
    else:
        logging.error('The data file says the template_type is "' + template_type + '" but that\'s invalid.')
        exit(1)

    logging.info("Using template file " + template_file_path + ".")
    with open(template_file_path, 'rb') as f:
        template = Environment(loader=FileSystemLoader('templates/' + audience)).from_string(f.read())

    output_path = 'output/' + audience + '/' + data['output_filename']
    logging.info("Outputting to " + output_path + ".")
    with open(output_path, 'wb') as f:
        f.write(template.render(data))


if __name__=="__main__":
    for json_source_file in ('data/products/faculty/T470s.json',
                             'data/products/faculty/X1Carbon5thGen.json',
                             'data/products/faculty/X1Yoga2ndGen.json',
                             'data/products/faculty/M910tDesktop.json',
                             'data/products/faculty/consulting.json',
                             'data/products/faculty/index.json',
                             'data/products/staff/T470s.json',
                             'data/products/staff/Yoga370.json',
                             'data/products/staff/M910qTiny.json',
                             'data/products/staff/bundles.json',
                             'data/products/staff/index.json',
                             'data/products/staff/consulting.json'):
        render_template_to_file(json_source_file)
