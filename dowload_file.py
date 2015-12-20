from urllib import request

def download_file(url):
    response = request.urlopen(url)

    file = str(response.read())
    sort_file = file.split("\\n")
    new_file = r'new_file.txt'
    fxle = open(new_file,"w")
    for file_data in sort_file:
        fxle.write(file_data + "\n")
    fxle.close()
download_file("http://real-chart.finance.yahoo.com/table.csv?s=GOOG&d=11&e=19&f=2015&g=d&a=2&b=27&c=2014&ignore=.csv")


