#coding:utf-8
import httplib2

def fetch(url):
        http_header = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1',
        'Referer':'https://www.sportsdatallc.org/',
        'Host':'api.sportsdatallc.org'}

        h = httplib2.Http('.cache')

        print ("Start downloading data....")
        response, content = h.request(url,headers = http_header)
        print ("Finish downloading data...")

        # print(response['-content-encoding'])
        print(response['status'])
        print(content)
        try:
                with open('baidu.html',"w") as dig:
                        print(content,file = dig)
        except IOError as err:
                print('File error: ' + str(err))

if __name__ == "__main__":
        fetch("http://api.sportsdatallc.org/nba-t3/games/2013/reg/schedule.xml?api_key=9ur3zyfemmyeaeqjqv3zekrz")