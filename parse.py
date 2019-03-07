import yaml

f = open("weekly-report.yml", "r+")
data = yaml.load(f)
print(data)

#if __name__ == "__main__":
    # execute only if run as a script
#    main()

