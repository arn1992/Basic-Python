from urllib import request

goog_url="http://chart.finance.yahoo.com/table.csv?s=GOOG&a=9&b=23&c=2016&d=10&e=23&f=2016&g=d&ignore=.csv"

def download_data(csv_url):
    response=request.urlopen(csv_url)
    csv=response.read()
    csv_str=str(csv)
    lines= csv_str.split("\\n")
    dest_url=r"E:\goog1.csv"
    fw=open(dest_url,"w")
    for line in lines:
        fw.write(line+ "\n")
    fw.close()


download_data(goog_url)