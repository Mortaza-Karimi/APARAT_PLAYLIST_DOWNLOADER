from bs4 import BeautifulSoup
import requests
from time import sleep
import urllib3

def add_to_urls(direct_url):
    with open('urls.txt', 'a') as file:
        file.write(f'{direct_url} \n')


url = input("Paste the url:> ")

page = requests.get(url)
html = page.text

s = BeautifulSoup(html, 'lxml')
playlistT = s.find('div',{'class':'playlist-list'})


playlist = playlistT.find('ol', {'class': 'dd-list'})

all_links = playlist.find_all('h2', {'class': 'title'})
#print(all_links)

links = []
for link in all_links:
    this_link = link.find('a')
    href = this_link.attrs['href']
    links.append({'title':this_link.attrs['title'],'link':f"https://www.aparat.com{href}"})

for link in links:
    if str(link['title']).replace("/","")=="ماینکرافت ندر آپدیت(ورژن 1.16)  قسمت سوم  خانه":
        continue
    if str(link['title']).replace("/","")=="ماینکرافت ندر آپدیت(ورژن 1.16)  قسمت اول  دایموند(الماس)":
        continue
    print(f"getting {link['title']} ...")
    res = requests.get(link['link'])
    html = res.text
    s = BeautifulSoup(html, 'lxml')
    url = s.select_one('li.link:nth-child(3) > a:nth-child(1)').attrs['href']
    

    import sys
    import requests

    # pass URL as first argument
    response = requests.head(url, allow_redirects=True)

    size = response.headers.get('content-length', -1)

    # size in megabytes (Python 2, 3)
    print('{:<40}: {:.2f} MB'.format('FILE SIZE', int(size) / float(1 << 20)))


    import sys
    import requests

    file_name = str(link['title']).replace("/","")
    link = url
    
    with open(file_name, "wb") as f:
        print("Downloading %s" % file_name)
        response = requests.get(link, stream=True)
        total_length = response.headers.get('content-length')

        if total_length is None: # no content length header
            f.write(response.content)
        else:
            dl = 0
            total_length = int(total_length)
            for data in response.iter_content(chunk_size=4096):
                dl += len(data)
                
                f.write(data)
                done = int(50 * dl / total_length)
                
                sys.stdout.write("\r[%s%s] %s" % ('=' * done, ' ' * (50-done),str(done)) )
                sys.stdout.flush()
    #add_to_urls(url)


#print(links)
"""   """ 
