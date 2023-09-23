import urllib.request

url = 'http://www.hrecos.org//images/Data/forweb/HRTVBSH.Metadata.pdf'
urllib.request.urlretrieve(url, "filename.pdf")