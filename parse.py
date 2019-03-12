import os, yaml, json, time
from jinja2 import Environment, FileSystemLoader
from datetime import datetime
from json import load

f = open("weekly-report.yml", "r+")
data = yaml.load(f)
print(data[0])
print(data[0]['name'])
print(data[0]['author'])
print(data[0]['sendto'])
print(data[0]['sendcc'])

sendTo = data[0]['sendto']
sendCc = data[0]['sendcc']

PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH, 'templates')),
    trim_blocks=False)

def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)

def create_weeklyreport():
    datalist = [sendTo, sendCc]
    context = {
        'mailreceive': datalist
    }
    print(render_template('weekly-report.txt', context))

def main():
    create_weeklyreport()

########################################

if __name__ == "__main__":
    main()

