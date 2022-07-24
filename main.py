import requests
import time
while True:
    for i in range(0, 100):
        o = open('link.txt', 'r')
        link = o.readlines()
        cookies = {
            '__dcfduid':
            '74f76430dc2a11ec92e60d0138b32d61',
            '__sdcfduid':
            '74f76431dc2a11ec92e60d0138b32d6155004fa52ae80625949da42347e959e531a75c75aeab82d0aab999c5e38ab797',
            '_gcl_au':
            '1.1.1743570385.1657719386',
            '_ga':
            'GA1.2.463708923.1657719386',
            '_fbp':
            'fb.1.1657719396785.1988849384',
            '__stripe_mid':
            '2a1b827d-2a23-4e1f-ba68-5a3173c8854e7847fa',
            '_gid':
            'GA1.2.555601278.1658654427',
            'OptanonConsent':
            'isIABGlobal=false&datestamp=Sun+Jul+24+2022+16%3A20%3A28+GMT%2B0700+(Gi%E1%BB%9D+%C4%90%C3%B4ng+D%C6%B0%C6%A1ng)&version=6.33.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2Fdownload&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1',
        }

        headers = {
            'authority':
            'discord.com',
            'accept':
            '*/*',
            'accept-language':
            'vi,en;q=0.9,vi-VN;q=0.8,fr-FR;q=0.7,fr;q=0.6,en-US;q=0.5',
            'authorization':
            'OTk2NzcyMzk3Mzg0NDc0NjM0.Gvb-1m.akm1wuSsxSw4AgaZNCE40D8kG5lh--ktTBSDs4',
            # Already added when you pass json=
            # 'content-type': 'application/json',
            # Requests sorts cookies= alphabetically
            # 'cookie': '__dcfduid=74f76430dc2a11ec92e60d0138b32d61; __sdcfduid=74f76431dc2a11ec92e60d0138b32d6155004fa52ae80625949da42347e959e531a75c75aeab82d0aab999c5e38ab797; _gcl_au=1.1.1743570385.1657719386; _ga=GA1.2.463708923.1657719386; _fbp=fb.1.1657719396785.1988849384; __stripe_mid=2a1b827d-2a23-4e1f-ba68-5a3173c8854e7847fa; _gid=GA1.2.555601278.1658654427; OptanonConsent=isIABGlobal=false&datestamp=Sun+Jul+24+2022+16%3A20%3A28+GMT%2B0700+(Gi%E1%BB%9D+%C4%90%C3%B4ng+D%C6%B0%C6%A1ng)&version=6.33.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2Fdownload&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1',
            'origin':
            'https://discord.com',
            'referer':
            'https://discord.com/channels/1000436292414341141/1000436293530034239',
            'sec-ch-ua':
            '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'sec-ch-ua-mobile':
            '?0',
            'sec-ch-ua-platform':
            '"Windows"',
            'sec-fetch-dest':
            'empty',
            'sec-fetch-mode':
            'cors',
            'sec-fetch-site':
            'same-origin',
            'user-agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
            'x-debug-options':
            'bugReporterEnabled',
            'x-discord-locale':
            'vi',
            'x-super-properties':
            'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6InZpIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMy4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTAzLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjEzODI1NCwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=',
        }

        json_data = {
            'content': link[i],
            'nonce': '1000794389129199616',
            'tts': False,
        }

        response = requests.post(
            'https://discord.com/api/v9/channels/1000436293530034239/messages',
            cookies=cookies,
            headers=headers,
            json=json_data)
        print(str(i), 'DONE')
        time.sleep(120)
