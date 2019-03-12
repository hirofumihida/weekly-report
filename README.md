# weekly-report

- tech elements
    - python3
    - jinja2
        - http://jinja.pocoo.org/docs/2.10/api/
    - yaml
        - https://yaml.org/spec/1.2/spec.html

- main function
    - parse yaml
    - replace template to weekly report format with jinja2

- operation
    1. write yaml
    2. execute python3 script
    3. output weekly report

## prerequisites

- PyYAML

```
$ python3.7 -m pip install PyYAML --user
```

- jinja2

```
$ python3.7 -m pip install Jinja2 --user
```

## output sample

```
$ python3.7 parse.py

MailTo:  hoge@example.com

MailCc: fuga1@example.com; fuga2@example.com

Subject: weekly report by Hirofumi Hida, actual week start from 2019-03-11

Body:

- Notation:
    - actual starts from 2019-03-11 Monday
    - forecast starts from 2019-03-18 Monday

- Delivery (Billable):

    - Actual

        Project Name: Project A
        Customer Name: Customer A
        Actual Working:
            Monday: dev
            Friday: dev2
      
        Project Name: Project C
        Customer Name: Customer C
        Actual Working:
            Monday: dev
            Friday: dev2
      
    - Forecast

        Project Name: Project A
        Customer Name: Customer A
        Forecast Working:
            Friday: dev3
      
- Delivery (Un-Billable):

    - Actual

        Project Name: Project B
        Customer Name: Customer B
        Actual Working:
            Monday: dev
            Friday: dev2
      
    - Forecast

        Project Name: Project B
        Customer Name: Customer B
        Forecast Working:
            Friday: dev3
      
- Meeting (Billable):

    - Actual

        Project Name: Project A
        Customer Name: Customer A
        Actual Working:
            Monday: Daily MTG
            Friday: WeekLy MTG
      
  
        Project Name: Project C
        Customer Name: Customer C
        Actual Working:
            Monday: Daily MTG
            Friday: WeekLy MTG
      
  
    - Forecast

        Project Name: Project A
        Customer Name: Customer A
        Forecast Working:
            Friday: Monthly MTG
      
  
  
- Meeting (Un-Billable):

    - Actual

        Project Name: Project B
        Customer Name: Customer B
        Actual Working:
            Monday: Daily MTG
            Friday: WeekLy MTG
      
  
    - Forecast

        Project Name: Project B
        Customer Name: Customer B
        Forecast Working:
            Friday: Monthly MTG
      
  
- Training:

    - Actual

            No Actual Trainings
  
    - Forecast

            No Forecast Trainings
  
- Leave:

    - Actual

        Project Name: Sick Leave
        Actual Working:  Tuesday
  
    - Forecast

        Project Name: Paid Leave
        Forecast Working:  Friday
  
        Project Name: Holiday
        Forecast Working:  Thursday
  
```

## git command memo

```
git status ; git add . ; git status
git commit -m "edit files" ; git push origin master
```


