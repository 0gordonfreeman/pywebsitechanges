import schedule
import time
from loguru import logger
import os
import click

def checkReq(sessionid):
    #logger.info("check Requests")    
    cmd = 'py websitechanges.py --url "https://www.campusonline.at/support/wbRMTSearch.wbList?pStatusNr=&pOrgNr=37&pSpecialFieldNr=33&pShow=" --sessionid ' + sessionid
    #logger.info(cmd)
    os.system(cmd)

@click.command()
@click.option("--sid", default="", help="SessionId aus dem Cookie")
@click.option("--refresh", default=15, help="Aktualisiserungzeit in Minuten", show_default=True)
def run(sid, refresh):
    schedule.every(refresh).minutes.do(checkReq, sessionid=sid)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    run()    