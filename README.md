# weekly-report

- tech elements
    - python3
    - jinja2
    - yaml

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
MailTo:  hoge@example.com

MailCc: fuga1@example.com; fuga2@example.com

Subject: weekly report by Hirofumi Hida, actual week start from 2019-02-25

Body:

- Delivery:

    - Actual:

        Project Name: Project A
        Customer Name: Customer A
        Actual Working: Monday, Friday
        Descriptions: development, trouble shooting, handle support cases


- Forecast:

        Project Name: Project A
        Customer Name: Customer A
        Forecast Working: Monday, Friday
        Descriptions: development, trouble shooting, handle support cases


        Project Name: Project B
        Customer Name:
        Forecast Working:  Wednesday
        Descriptions: flow development

- Meeting

(snip)
```

## git command memo

```
git status ; git add . ; git status
git commit -m "edit files" ; git push origin master
```


