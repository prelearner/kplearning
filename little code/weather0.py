import urllib.request
url='http://m.weather.com.cn/data3/city.xml'
content1=urllib.request.urlopen(url).read()
content1=content1.decode()
provinces=content1.split(',')
for i in range(0,10):
    print(i)
url='http://m.weather.com.cn/data3/city%s.xml'
for i in range(0,11):
    print(i)
    content2=urllib.request.urlopen('http://%s')
#print(provinces)
url='http://m.weather.com.cn/data3/city%s.xml'
for p in provinces:
    p_code=p.split('|')[0]
    url2=url%p_code
    #print(url2)
    content2=urllib.request.urlopen(url2).read()
    content2=content2.decode()
    cities=content2.split(',')
    #print(cities)
    for c in cities:
        c_code=c.split('|')[0]
        url3=url%c_code
        #print(url3)
        content3=urllib.request.urlopen(url3).read()
        content3=content3.decode()
        districts=content3.split(',')
        #print(districts)
        for d in districts:
            d_pair=d.split('|')
            d_code=d_pair[0]
            name=d_pair[1]
            url4=url%d_code
            content4=urllib.request.urlopen(url4).read()
            content4=content4.decode()
            #print(content4)
            code=content4.split('|')[1]
            line='%s:%s\n'%(name,code)
            result='city: {\n'
            result+=line
            #print(name+':'+code)

result+='\n}'
f=open('city1.py','w')
f.write(result)
f.close()










