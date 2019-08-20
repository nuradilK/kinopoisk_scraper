from bs4 import BeautifulSoup
import requests
import html
import csv
from time import sleep
import random

headers = {
"cache-control": "no-store, no-cache, must-revalidate, post-check=0, pre-check=0, no-cache, private",
"content-encoding": "gzip",
"content-security-policy-report-only": "frame-src data: *.yandex.ru yastatic.net awaps.yandex.ru awaps.yandex.net yandexadexchange.net *.yandexadexchange.net api-maps.yandex.ru blob: mc.yandex.ru 'self' media.adrcdn.com *.kinopoisk.ru auth.kinopoisk.ru *.mds.yandex.net tickets.widget.kinopoisk.ru widget.tickets.yandex.ru  forms.yandex.ru *.yandex.net player.vimeo.com yandex.ru *.yandex.by *.yandex.ua *.yandex.kz yandex.net www.youtube.com; script-src 'unsafe-eval' ads.adfox.ru an.yandex.ru yastatic.net mc.yandex.ru 'unsafe-inline' api-maps.yandex.ru suggest-maps.yandex.ru *.maps.yandex.net yandex.ru mc.webvisor.com mc.webvisor.org mc.yandex.com mc.yandex.by mc.yandex.com.tr mc.yandex.kz mc.yandex.ua mc.yandex.az mc.yandex.co.il mc.yandex.com.am mc.yandex.com.ge mc.yandex.ee mc.yandex.fr mc.yandex.kg mc.yandex.lt mc.yandex.lv mc.yandex.md mc.yandex.tj mc.yandex.tm mc.yandex.uz 'self' *.adfox.ru *.adfox.yandex.ru auth.kinopoisk.ru https://ott.kinopoisk.ru:3001 sso.kinopoisk.ru sso.passport.yandex.ru tickets.widget.kinopoisk.ru widget.tickets.yandex.ru  forms.yandex.ru *.kinopoisk.ru *.yandex.net yandex.st *.yandex.ru *.yandex.by *.yandex.ua *.yandex.kz yandex.net *.yastatic.net; style-src 'unsafe-inline' yastatic.net blob: 'self' auth.kinopoisk.ru *.kinopoisk.ru *.yandex.net yandex.st yandex.ru *.yandex.ru *.yandex.by *.yandex.ua *.yandex.kz yandex.net; img-src 'self' data: an.yandex.ru favicon.yandex.net avatars-fast.yandex.net 'unsafe-inline' *.maps.yandex.net api-maps.yandex.ru yandex.ru yastatic.net mc.webvisor.com mc.webvisor.org mc.yandex.com mc.yandex.by mc.yandex.com.tr mc.yandex.kz mc.yandex.ru mc.yandex.ua mc.yandex.az mc.yandex.co.il mc.yandex.com.am mc.yandex.com.ge mc.yandex.ee mc.yandex.fr mc.yandex.kg mc.yandex.lt mc.yandex.lv mc.yandex.md mc.yandex.tj mc.yandex.tm mc.yandex.uz mc.admetrica.ru *.adfox.ru *.adfox.yandex.ru media.adrcdn.com *.adrcntr.com amc.yandex.ru avatars.mdst.yandex.net avatars.mds.yandex.net awaps.yandex.net awaps.yandex.ru rest-api.bannerstorage.yandex.net ext.captcha.yandex.net *.cdn.yandex.net mc.kinopoisk.ru st.kinopoisk.ru st.kp.yandex.net storage.mds.yandex.net ceditor.setka.io sso.kinopoisk.ru sso.passport.yandex.ru https://static-maps.yandex.ru www.tns-counter.ru ar.tns-counter.ru web-metrica.yandex.ru imeem.com *.kinopoisk.ru samsung.com *.yandex.net yandex.st *.yandex.ru *.yandex.by *.yandex.ua *.yandex.kz yandex.net; media-src *.yandex.net yastatic.net *.adfox.ru *.adfox.yandex.ru *.cdn.yandex.net 'self'; connect-src 'self' yastatic.net mc.yandex.ru an.yandex.ru strm.yandex.ru mc.webvisor.com mc.webvisor.org mc.yandex.com mc.yandex.by mc.yandex.com.tr mc.yandex.kz mc.yandex.ua mc.yandex.az mc.yandex.co.il mc.yandex.com.am mc.yandex.com.ge mc.yandex.ee mc.yandex.fr mc.yandex.kg mc.yandex.lt mc.yandex.lv mc.yandex.md mc.yandex.tj mc.yandex.tm mc.yandex.uz mc.admetrica.ru *.adfox.ru *.adfox.yandex.ru csp.yandex.net http-check-headers.yandex.ru jstracer.yandex.ru *.kinopoisk.ru ott-widget.yandex.ru api.passport.yandex.ru sentry.iddqd.yandex.net static-mon.yandex.net yandex.ru forms.yandex.ru *.yandex.net yandex.st *.yandex.ru *.yandex.by *.yandex.ua *.yandex.kz yandex.net; child-src api-maps.yandex.ru blob: mc.yandex.ru; frame-ancestors webvisor.com *.webvisor.com http://webvisor.com http://*.webvisor.com; default-src 'none'; font-src 'self' *.adfox.ru *.adfox.yandex.ru yastatic.net *.kinopoisk.ru *.yandex.net yandex.st yandex.ru *.yandex.ru *.yandex.by *.yandex.ua *.yandex.kz yandex.net; form-action 'self' forms.yandex.ru; object-src 'self' *.adfox.ru *.adfox.yandex.ru rest-api.bannerstorage.yandex.net betastatic.yandex.net storage.mds.yandex.net *.kinopoisk.ru *.yandex.net vesti.ru vimeo.com; manifest-src 'self' *.kinopoisk.ru *.yandex.net yandex.net yastatic.net *.yastatic.net; report-uri https://csp.yandex.net/csp?from=kinopoisk&yandexuid=6521862361535385815&yandex_login=Nur4dil;",
"content-type": "text/html; charset=utf-8",
"date": "Tue, 20 Aug 2019 11:05:46 GMT",
"expires": "Thu, 19 Nov 1981 08:52:00 GMT",
"pragma": "no-cache",
"set-cookie": "user_country=kz; expires=Tue, 20-Aug-2019 12:05:46 GMT; Max-Age=3600; path=/; domain=.kinopoisk.ru; secure; httponly",
"set-cookie": "yandex_gid=163; path=/; domain=.kinopoisk.ru; secure; httponly",
"set-cookie": "tc=5361; expires=Wed, 21-Aug-2019 11:05:46 GMT; Max-Age=86400; path=/; domain=.kinopoisk.ru; secure; httponly",
"set-cookie": "uid=32253335; path=/; domain=.kinopoisk.ru",
"set-cookie": "uid=32253335; path=/; domain=.kinopoisk.ru",
"status": "200",
"strict-transport-security": "max-age=31536000",
"vary": "Accept-Encoding",
"x-consumed-content-encoding": "gzip",
"x-content-type-options": "nosniff",
"x-frame-options": "DENY",
"x-qloud-router": "iva4-5cac700a8fcd.qloud-c.yandex.net",
"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
"accept-encoding": "gzip, deflate, br",
"accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
"cookie": "tc=5361; mobile=no; mda=0; yandexuid=6521862361535385815; yuidss=6521862361535385815; mda_exp_enabled=1; noflash=true; _ym_uid=1566199028800255228; _ym_d=1566199028; refresh_yandexuid=6521862361535385815; yandex_login=Nur4dil; i=nYPYbv8ZG4rwls/1tkxq0lcbp41XHOFEB+stBi3nJwG18uhkAX1zt1PSELTCqpc2w1umzPm/D8QCXNuFlL3ykO/Xhuw=; crookie=I6hHPogPZhLFmOoljCCBuB46wcRyMXF5/46it8Pz6//mfOfxLgl8DDVHEXgiW6o0HfZjwFcV/BKQNh3L75W1JV/ziH8=; cmtchd=MTU2NjE5OTAzNTQ3NA==; technology=1; white_email_status=1:1:1568797992652; my_perpages=%5B%5D; users_info[check_sh_bool]=none; PHPSESSID=tl79a26hhaeo32pb26onrmcib1; yandex_gid=163; uid=32253335; _csrf_csrf_token=JzSvN3s1Lw4N9KfvG3LcrdZ8qVuxQn5n0gTo-z9GKRE; user-geo-region-id=163; user-geo-country-id=122; desktop_session_key=a1a34972d909f2dd91db3c56a22c588a63c048fcc340a1d2e06eff3e2a66ec3ccb2db395a1583980072a35d7fc1750355ef19509baaf923d9e36170a8187c2bde21a6d48d7815446f1cd531c62cacb3171b30948c6a8c89d3cacd05988692f22; desktop_session_key.sig=w49s8ooRo87fxrK3z9PJmu7FHY8; fuid01=5b97e59544a3f7d5.vAwmQdrdCWM0sbqZ23-Afa22MCjtg2R6psJZAunM3gmPvhec9m5nCU9LaH103E4HNfEMuf0Y1NnWbnrmjM8Nfw_Ang7q4b5aHItq7zeb-qEuEbc0QFUUetAlVk02H9rb; user_country=kz; yandex_plus_metrika_cookie=true; _ym_wasSynced=%7B%22time%22%3A1566298855967%2C%22params%22%3A%7B%22eu%22%3A0%7D%2C%22bkParams%22%3A%7B%7D%7D; _ym_isad=2; yp=1568890857.oyu.6521862361535385815#1566385257.yu.6521862361535385815; _ym_visorc_22663942=b; _ym_visorc_52332406=b; ya_sess_id=3:1566299041.5.0.1549277558961:WP1bsg:6.1|484186699.0.2|30:182994.475561.ZH0bgLwje9jimjDU28fvXWAjQDE; ys=udn.cDpOdXI0ZGls#c_chck.4287215492; mda2_beacon=1566299041311; sso_status=sso.passport.yandex.ru:synchronized; adblock-warning-toast-hide=1",
"dnt": "1",
"referer": "https://www.kinopoisk.ru/top/",
"sec-fetch-mode": "navigate",
"sec-fetch-site": "same-origin",
"sec-fetch-user": "?1",
"upgrade-insecure-requests": "1",
"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
}

source = requests.get('https://www.kinopoisk.ru/top/', headers=headers).text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('data.csv', 'a')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['movie', 'rating', 'year_released', 'budget', 'total gross', 'gross in USA', 'country', 'runtime', 'views', 'premiere'])


for pos in range(41, 251):
    print(pos)
    idx = "top250_place_" + str(pos)
    data = soup.find('tr', {"id" : idx})
    movie = data.find('a', {"class": "all"})
    
    name = movie.text
    link = movie.get('href')
    rating = data.find('a', {"class": "continue"}).text
    movieLink = "https://www.kinopoisk.ru" + link

    secs = random.randrange(20,42,1)
    sleep(secs)
    response = requests.get(movieLink, headers=headers).text
    sp = BeautifulSoup(response, 'lxml')
    
    table = sp.find('table', {"class": "info"})
    table_body = table.find_all('div')
    runtime = table.find('td', {'id': 'runtime'}).text
    year = (table_body[0].text.rstrip() if len(table_body) > 0 else None)
    country = (table_body[1].text.rstrip() if len(table_body) > 1 else None)
    budget = (table_body[2].text.rstrip() if len(table_body) > 2 else None)
    grossInUSA = (table_body[3].text.rstrip() if len(table_body) > 3 else None)
    totalGross = (table_body[4].text.rstrip() if len(table_body) > 4 else None)
    views = (table_body[5].text.rstrip() if len(table_body) > 5 else None)
    premiere = (table_body[7].text.rstrip() if len(table_body) > 7 else None)

    csv_writer.writerow([name, rating, year, budget, totalGross, grossInUSA, country, runtime, views, premiere])

csv_file.close()
