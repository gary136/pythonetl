import re
import json
import datetime

import pytz
import requests
from celery import Celery
from bs4 import BeautifulSoup
import rethinkdb as r

app = Celery('tasks', broker='pyamqp://celery:celery@localhost//')
HOST = 'https://www.yes123.com.tw/admin/'

@app.task
def add(x, y):
    return x + y

@app.task
def get_list(page):
    offset = (page-1) * 20
    url = HOST + "job_refer_list.asp"
    data = json.loads(r'''{
        "find_key1": "軟體工程師",
        "search_work": "職務",
        "search_multi_loc": "地區",
        "find_key2": "",
        "search_multi_loc2": "請選擇地區",
        "search_work2": "請選擇職務",
        "search_job2": "請選擇行業",
        "find_key3": "",
        "search_multi_loc3": "請選擇地區",
        "search_work3": "請選擇職務",
        "search_subj": "請選擇你的科系",
        "search_work4": "",
        "search_multi_loc4": "請選擇地區",
        "search_multi_loc5": "請選擇地區",
        "search_work6": "",
        "search_work7": "",
        "search_multi_loc6": "",
        "search_work8": "",
        "search_multi_loc7": "",
        "search_work9": "請選擇職務",
        "find_sf_subj_mode1": "",
        "s_find_sf_subj_mode1": "",
        "find_se_work_mode1": "",
        "s_find_se_work_mode1": "",
        "find_ss_work_mode1": "",
        "s_find_ss_work_mode1": "",
        "find_zone_mode1": "",
        "find_zone_mode2": "",
        "find_zone_mode3": "",
        "find_zone_mode4": "",
        "find_zone_mode5": "",
        "find_zone_mode6": "",
        "find_zone_mode7": "",
        "find_zone_mode8": "",
        "find_zone_mode9": "",
        "find_zone_mode10": "",
        "s_find_zone_mode1": "",
        "s_find_zone_mode2": "",
        "s_find_zone_mode3": "",
        "s_find_zone_mode4": "",
        "s_find_zone_mode5": "",
        "s_find_zone_mode6": "",
        "s_find_zone_mode7": "",
        "s_find_zone_mode8": "",
        "s_find_zone_mode9": "",
        "s_find_zone_mode10": "",
        "find_metro_mode1": "",
        "find_metro_mode2": "",
        "find_metro_mode3": "",
        "find_metro_mode4": "",
        "find_metro_mode5": "",
        "find_metro_mode6": "",
        "find_metro_mode7": "",
        "find_metro_mode8": "",
        "find_metro_mode9": "",
        "find_metro_mode10": "",
        "s_find_metro_mode1": "",
        "s_find_metro_mode2": "",
        "s_find_metro_mode3": "",
        "s_find_metro_mode4": "",
        "s_find_metro_mode5": "",
        "s_find_metro_mode6": "",
        "s_find_metro_mode7": "",
        "s_find_metro_mode8": "",
        "s_find_metro_mode9": "",
        "s_find_metro_mode10": "",
        "find_map_mode1": "",
        "find_map_mode2": "",
        "find_map_mode3": "",
        "find_map_mode4": "",
        "find_indy_mode1": "",
        "find_indy_mode2": "",
        "find_indy_mode3": "",
        "find_indy_mode4": "",
        "find_indy_mode5": "",
        "find_indy_mode6": "",
        "find_indy_mode7": "",
        "find_indy_mode8": "",
        "find_indy_mode9": "",
        "find_indy_mode10": "",
        "s_find_indy_mode1": "",
        "s_find_indy_mode2": "",
        "s_find_indy_mode3": "",
        "s_find_indy_mode4": "",
        "s_find_indy_mode5": "",
        "s_find_indy_mode6": "",
        "s_find_indy_mode7": "",
        "s_find_indy_mode8": "",
        "s_find_indy_mode9": "",
        "s_find_indy_mode10": "",
        "find_scl_mode1": "",
        "find_scl_mode2": "",
        "find_scl_mode3": "",
        "find_scl_mode4": "",
        "find_scl_mode5": "",
        "find_scl_mode6": "",
        "find_scl_mode7": "",
        "find_scl_mode8": "",
        "find_scl_mode9": "",
        "find_scl_mode10": "",
        "s_find_scl_mode1": "",
        "s_find_scl_mode2": "",
        "s_find_scl_mode3": "",
        "s_find_scl_mode4": "",
        "s_find_scl_mode5": "",
        "s_find_scl_mode6": "",
        "s_find_scl_mode7": "",
        "s_find_scl_mode8": "",
        "s_find_scl_mode9": "",
        "s_find_scl_mode10": "",
        "find_work_mode1": "",
        "find_work_mode2": "",
        "find_work_mode3": "",
        "find_work_mode4": "",
        "find_work_mode5": "",
        "find_work_mode6": "",
        "find_work_mode7": "",
        "find_work_mode8": "",
        "find_work_mode9": "",
        "find_work_mode10": "",
        "s_find_work_mode1": "",
        "s_find_work_mode2": "",
        "s_find_work_mode3": "",
        "s_find_work_mode4": "",
        "s_find_work_mode5": "",
        "s_find_work_mode6": "",
        "s_find_work_mode7": "",
        "s_find_work_mode8": "",
        "s_find_work_mode9": "",
        "s_find_work_mode10": "",
        "find_job_mode1": "",
        "find_job_mode2": "",
        "find_job_mode3": "",
        "find_job_mode4": "",
        "find_job_mode5": "",
        "find_job_mode6": "",
        "find_job_mode7": "",
        "find_job_mode8": "",
        "find_job_mode9": "",
        "find_job_mode10": "",
        "s_find_job_mode1": "",
        "s_find_job_mode2": "",
        "s_find_job_mode3": "",
        "s_find_job_mode4": "",
        "s_find_job_mode5": "",
        "s_find_job_mode6": "",
        "s_find_job_mode7": "",
        "s_find_job_mode8": "",
        "s_find_job_mode9": "",
        "s_find_job_mode10": "",
        "find_sche_mode1": "",
        "find_sche_mode2": "",
        "find_sche_mode3": "",
        "find_sche_mode4": "",
        "find_sche_mode5": "",
        "s_find_sche_mode1": "",
        "s_find_sche_mode2": "",
        "s_find_sche_mode3": "",
        "s_find_sche_mode4": "",
        "s_find_sche_mode5": "",
        "_mu_sf_1": "",
        "_mu_se_1": "",
        "_mu_chkbox_2": "",
        "_mu_chkbox_3": "",
        "_mu_wk_1": "",
        "_mu_wk_2": "",
        "_mu_wk_3": "",
        "_mu_wk_4": "",
        "_mu_wk_5": "",
        "_mu_job_1": "",
        "_mu_edu_1": "",
        "_mu_edu_2": "",
        "_mu_edu_3": "",
        "_mu_edu_4": "",
        "_mu_edu_5": "",
        "_mu_edu_6": "",
        "_mu_edu_7": "",
        "_mu_year_1": "",
        "_mu_year_2": "",
        "_mu_lang_1": "",
        "_mu_lang_2": "",
        "_mu_lang_3": "",
        "_mu_psn_1": "",
        "_mu_time_1": "",
        "_mu_time_2": "",
        "_mu_time_3": "",
        "_mu_time_4": "",
        "_mu_time_5": "",
        "_mu_vc_1": "",
        "_mu_vc_2": "",
        "_mu_vc_3": "",
        "_mu_vc_4": "",
        "_mu_sc_1": "",
        "_mu_sc_2": "",
        "find_subj_mode1": "",
        "find_subj_mode2": "",
        "find_subj_mode3": "",
        "s_find_subj_mode1": "",
        "s_find_subj_mode2": "",
        "s_find_subj_mode3": "",
        "find_sw_mode1": "",
        "find_sw_mode2": "",
        "find_sw_mode3": "",
        "find_sw_mode4": "",
        "find_sw_mode5": "",
        "s_find_sw_mode1": "",
        "s_find_sw_mode2": "",
        "s_find_sw_mode3": "",
        "s_find_sw_mode4": "",
        "s_find_sw_mode5": "",
        "find_cert_mode1": "",
        "find_cert_mode2": "",
        "find_cert_mode3": "",
        "find_cert_mode4": "",
        "find_cert_mode5": "",
        "s_find_cert_mode1": "",
        "s_find_cert_mode2": "",
        "s_find_cert_mode3": "",
        "s_find_cert_mode4": "",
        "s_find_cert_mode5": "",
        "find_us_sf_subj_mode1": "",
        "s_find_us_sf_subj_mode1": "",
        "find_us_se_work_mode1": "",
        "s_find_us_se_work_mode1": "",
        "find_us_work_mode1": "",
        "find_us_work_mode2": "",
        "find_us_work_mode3": "",
        "find_us_work_mode4": "",
        "find_us_work_mode5": "",
        "find_us_work_mode6": "",
        "find_us_work_mode7": "",
        "find_us_work_mode8": "",
        "find_us_work_mode9": "",
        "find_us_work_mode10": "",
        "s_find_us_work_mode1": "",
        "s_find_us_work_mode2": "",
        "s_find_us_work_mode3": "",
        "s_find_us_work_mode4": "",
        "s_find_us_work_mode5": "",
        "s_find_us_work_mode6": "",
        "s_find_us_work_mode7": "",
        "s_find_us_work_mode8": "",
        "s_find_us_work_mode9": "",
        "s_find_us_work_mode10": "",
        "find_us_zone_mode1": "",
        "find_us_zone_mode2": "",
        "find_us_zone_mode3": "",
        "find_us_zone_mode4": "",
        "find_us_zone_mode5": "",
        "find_us_zone_mode6": "",
        "find_us_zone_mode7": "",
        "find_us_zone_mode8": "",
        "find_us_zone_mode9": "",
        "find_us_zone_mode10": "",
        "s_find_us_zone_mode1": "",
        "s_find_us_zone_mode2": "",
        "s_find_us_zone_mode3": "",
        "s_find_us_zone_mode4": "",
        "s_find_us_zone_mode5": "",
        "s_find_us_zone_mode6": "",
        "s_find_us_zone_mode7": "",
        "s_find_us_zone_mode8": "",
        "s_find_us_zone_mode9": "",
        "s_find_us_zone_mode10": "",
        "find_us_metro_mode1": "",
        "find_us_metro_mode2": "",
        "find_us_metro_mode3": "",
        "find_us_metro_mode4": "",
        "find_us_metro_mode5": "",
        "find_us_metro_mode6": "",
        "find_us_metro_mode7": "",
        "find_us_metro_mode8": "",
        "find_us_metro_mode9": "",
        "find_us_metro_mode10": "",
        "s_find_us_metro_mode1": "",
        "s_find_us_metro_mode2": "",
        "s_find_us_metro_mode3": "",
        "s_find_us_metro_mode4": "",
        "s_find_us_metro_mode5": "",
        "s_find_us_metro_mode6": "",
        "s_find_us_metro_mode7": "",
        "s_find_us_metro_mode8": "",
        "s_find_us_metro_mode9": "",
        "s_find_us_metro_mode10": "",
        "find_us_indy_mode1": "",
        "find_us_indy_mode2": "",
        "find_us_indy_mode3": "",
        "find_us_indy_mode4": "",
        "find_us_indy_mode5": "",
        "find_us_indy_mode6": "",
        "find_us_indy_mode7": "",
        "find_us_indy_mode8": "",
        "find_us_indy_mode9": "",
        "find_us_indy_mode10": "",
        "s_find_us_indy_mode1": "",
        "s_find_us_indy_mode2": "",
        "s_find_us_indy_mode3": "",
        "s_find_us_indy_mode4": "",
        "s_find_us_indy_mode5": "",
        "s_find_us_indy_mode6": "",
        "s_find_us_indy_mode7": "",
        "s_find_us_indy_mode8": "",
        "s_find_us_indy_mode9": "",
        "s_find_us_indy_mode10": "",
        "find_us_map_mode1": "",
        "find_us_map_mode2": "",
        "find_us_map_mode3": "",
        "find_us_map_mode4": "",
        "strrec": "%s",
        "search_key_word": "軟體工程師",
        "search_type": "job",
        "us_menu": "",
        "search_item": "1",
        "search_from": "index"
    }'''%offset)
    headers = json.loads(r'''{
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Length": "6160",
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": "_sh_c_1=search_type%3Ajob%7Csearch_item%3A1%7Csearch_key_word%3A%E8%BB%9F%E9%AB%94%E5%B7%A5%E7%A8%8B%E5%B8%AB%7C_mu_ckb_21%3Acheckbox%7C_mu_ckb_22%3Acheckbox%7C_mu_ckb_23%3Acheckbox%7C_mu_ckb_24%3Acheckbox%7C_mu_ckb_25%3Acheckbox; __auc=96bb3e47161316640a21544cdad; _ga=GA1.3.1835310821.1516952241; ASPSESSIONIDQSABDSSA=NEHFNDJAFKHEFFCENHKAFOHL; citrix_ns_id=NTH5FeqYzJZTH+Cff7Zuk795B6oA000; ASP.NET_SessionId=155014982; StepCookie_id=155014982; ClientIP=36.230.46.183; _gid=GA1.3.1475659930.1517365319; __asc=4351f1c81614a0557a517057437; yes123_make_cookie=b06623371d0308352dafe66b5a40bb84; step=3",
        "Host": "www.yes123.com.tw",
        "Origin": "https://www.yes123.com.tw",
        "Pragma": "no-cache",
        "Referer": "https://www.yes123.com.tw/admin/index.asp",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
    }''')

    resp = requests.post(url, data=data, headers=headers)
    resp.encoding = 'utf-8'

    details = [HOST + url for url in re.findall("""<a href="(.*)" class='jobname'""", resp.text)]

    """Delay new jobs to get detail page"""
    for url in details:
        get_detail.delay(url)

@app.task
def get_detail(url):
    data = {}
    resp = requests.get(url,
                    headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"})
    soup = BeautifulSoup(resp.text, 'lxml')

    head_count_str = soup.select_one('.jobname_title').select_one('span').text.strip()
    head_count_str = '需求人數：2至2人'
    data['head_count'] = re.findall('\d', head_count_str)
    data['company_name'] = soup.select_one('.jobname_title').select_one('a').text

    [x.extract() for x in soup.select_one('.jobname_title').select('span')]
    [x.extract() for x in soup.select_one('.jobname_title').select('p')]
    data['job_title'] = soup.select_one('.jobname_title').text.strip()

    date_str = re.findall("""<span class="tt">職缺更新 ： </span><span class="rr">(.*)</span>""", resp.text)[0]
    data['updated_at'] = int(datetime.datetime.strptime(''.join(date_str.split("&nbsp;")).strip(), '%Y年%m月%d日').astimezone(pytz.timezone('Asia/Taipei')).timestamp())
    data['content'] = soup.select_one('div.left').text
    data['url'] = url

    to_rethinkdb.delay(data)
    return data


@app.task
def to_rethinkdb(data):
    conn = r.connect()
    res = r.db('yes123').table('crawler').insert(data).run(conn)
    conn.close()
    return res


