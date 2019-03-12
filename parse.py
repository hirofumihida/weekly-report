import os, yaml, json, time
from jinja2 import Environment, FileSystemLoader
from datetime import datetime
from json import load

f = open("weekly-report.yml", "r+")
data = yaml.load(f)

subjectName = data[0]['name']
reportAuther = data[0]['author']
startDate = data[0]['start']
sendTo = data[0]['sendto']
sendCc = data[0]['sendcc']

deliveryData = data[0]['delivery']
trainingData = data[0]['training']
meetingData = data[0]['meeting']
leaveData = data[0]['leave']

print(deliveryData)

PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH, 'templates')),
    trim_blocks=False)

def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)

def create_weeklyreport():
    metaData = [reportAuther, subjectName, startDate ]
    mailaddrsList = [sendTo, sendCc]
    context = {
            'headerdata': metaData,
            'mailaddrs': mailaddrsList,
            'deliverydata': deliveryData,
            'trainingdata': trainingData,
            'meetingdata': meetingData,
            'leavedata': leaveData
    }
    print(render_template('weekly-report.txt', context))

def main():
    create_weeklyreport()

########################################

if __name__ == "__main__":
    main()

