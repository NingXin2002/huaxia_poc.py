# huaxia_poc.py
华夏 ERPV3.3 信息泄漏漏洞

**需要安装支持库**  
pip install requests  

python huaxia_poc.py -h

                ('-. .-.               ('-.    ) (`-.                ('-.               _ (`-.
        ( OO )  /              ( OO ).-. ( OO ).             ( OO ).-.          ( (OO  )
        ,--. ,--. ,--. ,--.    / . --. /(_/.  \_)-. ,-.-')   / . --. /         _.`     \ .-'),-----.    .-----.
        |  | |  | |  | |  |    | \-.  \  \  `.'  /  |  |OO)  | \-.  \         (__...--''( OO'  .-.  '  '  .--./
        |   .|  | |  | | .-').-'-'  |  |  \     /\  |  |  \.-'-'  |  |         |  /  | |/   |  | |  |  |  |('-.
        |       | |  |_|( OO )\| |_.'  |   \   \ |  |  |(_/ \| |_.'  |  (`-.   |  |_.' |\_) |  |\|  | /_) |OO  )
        |  .-.  | |  | | `-' / |  .-.  |  .'    \_),|  |_.'  |  .-.  | (OO  )_ |  .___.'  \ |  | |  | ||  |`-'|
        |  | |  |('  '-'(_.-'  |  | |  | /  .'.  \(_|  |     |  | |  |,------.)|  |        `'  '-'  '(_'  '--'\
        `--' `--'  `-----'     `--' `--''--'   '--' `--'     `--' `--'`------' `--'          `-----'    `-----'

usage: huaxia_poc.py [-h] [-u URL] [-f FILE]  

华夏 ERPV3.3 信息泄漏漏洞  

optional arguments:  
  -h, --help            show this help message and exit  
  -u URL, --url URL     添加url信息  
  -f FILE, --file FILE  添加txt文件  

example:  
        python3 XETUX_POC.py -u http://xxxx.xxxx.xxxx.xxxx  
        python3 XETUX_POC -f x_url.txt  
