import json
from random import random

import requests
import bs4
import os
import datetime
import time
from urllib import  request
import urllib.request
import re

import urllib3
urllib3.disable_warnings()
REG = re.compile('<[^>]*>')

def extract_answer(s):
    #对s做字符串处理
    str = REG.sub("",s).replace("\n","").replace(" ", "")
    return str

def createURLList():
    urllist = []

    # urllist.append("https://www.zhihu.com/question/367106937")
    urllist.append(
        "https://www.zhihu.com/api/v4/questions/367106937/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Cis_labeled%2Cpaid_info%2Cpaid_info_content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_recognized%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics%3Bdata%5B%2A%5D.settings.table_of_content.enabled&limit=5&offset=0&platform=desktop&sort_by=default")
    # 1 月 26 日全国确诊新型肺炎 2744 例，死亡 80 例，目前的防治情况怎么样了？

    # urllist.append("https://www.zhihu.com/question/368178650")
    urllist.append(
        "https://www.zhihu.com/api/v4/questions/368178650/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Cis_labeled%2Cpaid_info%2Cpaid_info_content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_recognized%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics%3Bdata%5B%2A%5D.settings.table_of_content.enabled&limit=5&offset=10&platform=desktop&sort_by=default")
    # 1 月 27 日武汉疫情发布会称筹款统一归口，只通过省市红十字会接受捐赠，会对物资援助带来什么影响？

    # urllist.append("https://www.zhihu.com/question/368230779")
    urllist.append(
        "https://www.zhihu.com/api/v4/questions/368230779/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Cis_labeled%2Cpaid_info%2Cpaid_info_content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_recognized%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics%3Bdata%5B%2A%5D.settings.table_of_content.enabled&limit=5&offset=0&platform=desktop&sort_by=default")
    # 1 月 29 日全国新型肺炎确诊 7711 例，死亡 170 例，目前的防治情况怎么样了？

    # urllist.append("https://www.zhihu.com/question/368932802")
    urllist.append(
        "https://www.zhihu.com/api/v4/questions/368932802/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Cis_labeled%2Cpaid_info%2Cpaid_info_content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_recognized%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics%3Bdata%5B%2A%5D.settings.table_of_content.enabled&limit=5&offset=13&platform=desktop&sort_by=default")
    # 1 月 31 日全国新型肺炎累计确诊 11791 例，死亡 259 例，目前的防治情况怎么样了？

    # urllist.append("https://www.zhihu.com/question/369545723")
    urllist.append(
        "https://www.zhihu.com/api/v4/questions/369545723/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Cis_labeled%2Cpaid_info%2Cpaid_info_content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_recognized%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics%3Bdata%5B%2A%5D.settings.table_of_content.enabled&limit=5&offset=0&platform=desktop&sort_by=default")
    # 2 月 3 日全国确诊新型肺炎 20438 例，死亡 425 例，目前防治情况如何？

    # urllist.append("https://www.zhihu.com/question/370187473/answer/1003039368")
    urllist.append(
        "https://www.zhihu.com/api/v4/questions/370187473/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Cis_labeled%2Cpaid_info%2Cpaid_info_content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_recognized%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics%3Bdata%5B%2A%5D.settings.table_of_content.enabled&limit=5&offset=0&platform=desktop&sort_by=default")
    # 2月6日全国新增新冠肺炎确诊3143例，累计确诊 31161 例、死亡 636 例，目前防治情况如何？

    # urllist.append("https://www.zhihu.com/question/370825699")
    urllist.append(
        "https://www.zhihu.com/api/v4/questions/370825699/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Cis_labeled%2Cpaid_info%2Cpaid_info_content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_recognized%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics%3Bdata%5B%2A%5D.settings.table_of_content.enabled&limit=5&offset=0&platform=desktop&sort_by=default")
    # 2月9日全国新增确诊病例 3062 例，累计40171 例，目前防治情况如何？

    # urllist.append("https://www.zhihu.com/question/371526885/answer/1013438781")
    urllist.append(
        "https://www.zhihu.com/api/v4/questions/371526885/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Cis_labeled%2Cpaid_info%2Cpaid_info_content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_recognized%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics%3Bdata%5B%2A%5D.settings.table_of_content.enabled&limit=3&offset=0&platform=desktop&sort_by=default")
    # 如何看待2月12日湖北新增确诊人数14840人，首次单日确诊人数过万，什么情况？

    # urllist.append(("https://www.zhihu.com/question/372223761/answer/1018985472"))
    urllist.append(
        "https://www.zhihu.com/api/v4/questions/372223761/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Cis_labeled%2Cpaid_info%2Cpaid_info_content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_recognized%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics%3Bdata%5B%2A%5D.settings.table_of_content.enabled&limit=3&offset=0&platform=desktop&sort_by=default")
    # 2月15日湖北新增 1843 例新冠肺炎，疑似病例首次未见通报中，目前防治情况如何？

    # urllist.append("https://www.zhihu.com/question/373187653/answer/1026488899")
    urllist.append(
        "https://www.zhihu.com/api/v4/questions/373187653/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Cis_labeled%2Cpaid_info%2Cpaid_info_content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_recognized%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics%3Bdata%5B%2A%5D.settings.table_of_content.enabled&limit=3&offset=0&platform=desktop&sort_by=default")
    # 2月19日全国新增确诊病例 394 例，多地无新增确诊病例，目前防治情况如何？

    # urllist.append("zhihu.com/question/373699511/answer/1030300194")
    urllist.append(
        "https://www.zhihu.com/api/v4/questions/373699511/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Cis_labeled%2Cpaid_info%2Cpaid_info_content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_recognized%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics%3Bdata%5B%2A%5D.settings.table_of_content.enabled&limit=5&offset=0&platform=desktop&sort_by=default")
    # 2月21日全国新增确诊病例 397 例，累计 76288 例，目前防治情况如何？

    # urllist.append("https://www.zhihu.com/question/374211051/answer/1035590085")
    urllist.append(
        "https://www.zhihu.com/api/v4/questions/374211051/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Cis_labeled%2Cpaid_info%2Cpaid_info_content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_recognized%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics%3Bdata%5B%2A%5D.settings.table_of_content.enabled&limit=5&offset=0&platform=desktop&sort_by=default")
    # 2 月 23 日全国新增确诊病例 409 例，全国 24 个省（区、市）实现零新增，目前防治情况如何？

    # urllist.append("https://www.zhihu.com/question/374719304/answer/1038917214")
    urllist.append(
        "https://www.zhihu.com/api/v4/questions/374719304/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Cis_labeled%2Cpaid_info%2Cpaid_info_content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_recognized%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics%3Bdata%5B%2A%5D.settings.table_of_content.enabled&limit=3&offset=0&platform=desktop&sort_by=default")
    # 2 月 25 日全国新增确诊 406 例（湖北 401 例），新增死病 52 例，目前防治情况如何？

    # urllist.append("https://www.zhihu.com/question/375771510/answer/1047321377")
    urllist.append(
        "https://www.zhihu.com/api/v4/questions/375771510/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Cis_labeled%2Cpaid_info%2Cpaid_info_content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_recognized%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics%3Bdata%5B%2A%5D.settings.table_of_content.enabled&limit=3&offset=0&platform=desktop&sort_by=default")
    # 2 月 29 日全国新增确诊病例 573 例，湖北以外地区新增 3 例，目前防治情况如何？

    # urllist.append("https://www.zhihu.com/question/367785070/answer/999771653")
    urllist.append(
        "https://www.zhihu.com/api/v4/questions/367785070/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Cis_labeled%2Cpaid_info%2Cpaid_info_content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_recognized%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics%3Bdata%5B%2A%5D.settings.table_of_content.enabled&limit=5&offset=0&platform=desktop&sort_by=default")
    # 武汉乃至湖北各区市实际情况如何？

    # urllist.append("zhihu.com/question/367305173/answer/981917569")
    urllist.append(
        "https://www.zhihu.com/api/v4/questions/367305173/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Cis_labeled%2Cpaid_info%2Cpaid_info_content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_recognized%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics%3Bdata%5B%2A%5D.settings.table_of_content.enabled&limit=3&offset=0&platform=desktop&sort_by=default")
    # 钟南山院士称新型冠状病毒传染性比 SARS 最强时弱，两者对比如何？从非典我们学到了什么？

    # urllist.append("zhihu.com/question/371524248/answer/1092604572")
    urllist.append(
        "https://www.zhihu.com/api/v4/questions/371524248/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Cis_labeled%2Cpaid_info%2Cpaid_info_content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_recognized%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics%3Bdata%5B%2A%5D.settings.table_of_content.enabled&limit=5&offset=0&platform=desktop&sort_by=default")
    # 新冠肺炎给中国带来的积极意义是什么？

    return urllist

def saveFile(content, path, filename):
    if content != "This is the file that doesn't fits our need!":
        # 如果content的内容不是我们想要的，就将文章内容content保存到本地文件中
        if not os.path.exists(path):
            os.makedirs(path)
        with open(path + filename, 'w', encoding='utf-8') as f:
            f.write(content)

def crawl_Childcomments(start_childurl, title):
    destdir = "ZhihuComments"
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }
    next_url = [start_childurl]
    count = 0
    for url in next_url:
        html = requests.get(url, headers=headers)
        try:
            html.encoding = 'utf-8'
            bs = bs4.BeautifulSoup(html.text, "lxml")
            content = str(bs.p).split("<p>")[1].split("</p>")[0]

            c = json.loads(content)
            if not(c["paging"]["is_end"]): #如果是最后一页，也就是没有子评论
                for item in c["data"]:
                    # 每一个item是一个child_comment
                    count += 1
                    text = ""
                    author = item['author']['member']['name']
                    voteup = item['vote_count']
                    if extract_answer(item["content"]) != "":
                        text += "用户：" + author + "\n"
                        text += "点赞数：" + str(voteup) + "\n"
                        text += extract_answer(item["content"])
                        path = destdir + "/" + title + "/"
                        filename = author + "的评论" + ".txt"
                        saveFile(text, path, filename)
                        print("完成child_comment数目：" + str(count))
                next_url.append(c["paging"]["next"])
        except requests.exceptions.ConnectionError:
            print("Connection Error")
            time.sleep(2)
    print("子评论爬取完成,数目：" + str(count))

def crawl_Rootcomments(start_commenturl, title):
    destdir = "ZhihuComments"
    #传入参数是root_comment的初始页和这个回答的标题
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }

    next_url = [start_commenturl]
    count = 0

    for url in next_url:
        html = requests.get(url, headers=headers)
        html.encoding = 'utf-8'
        bs = bs4.BeautifulSoup(html.text, "lxml")
        content = str(bs.p).split("<p>")[1].split("</p>")[0]

        c = json.loads(content)
        for item in c["data"]:
            # 每一个item是一个root_comment
            if not(item["featured"]):
                #featured是true的时候代表是精选评论，用这个筛选不爬取精选评论，避免重复爬取
                count += 1
                #爬取root_comments自己
                text = ""
                author = item['author']['member']['name']
                voteup = item['vote_count']
                # comment = item['child_comment_count']
                if extract_answer(item["content"]) != "":
                    text += "用户：" + author + "\n"
                    text += "点赞数：" + str(voteup) + "\n"
                    # text += "评论数" + str(comment) + "\n"
                    text += extract_answer(item["content"])
                    path = destdir + "/" + title + "/"
                    filename = author + "的评论" + ".txt"
                    saveFile(text, path, filename)
                    print("完成评论数目：" + str(count))
                #爬取child_comments
                currurl = item["url"]
                child_starturl = currurl + "/child_comments"
                crawl_Childcomments(child_starturl, title)  # 爬取child_comments
        next_url.append(c["paging"]["next"])
        if (c["paging"]["is_end"]):
            break

def getAnswerList():

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }

    # urllist = createURLList()
    urllist = []

    # urllist.append("https://www.zhihu.com/question/370187473/answer/1003039368")
    urllist.append(
        "https://www.zhihu.com/api/v4/questions/370187473/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Cis_labeled%2Cpaid_info%2Cpaid_info_content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_recognized%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics%3Bdata%5B%2A%5D.settings.table_of_content.enabled&limit=5&offset=0&platform=desktop&sort_by=default")
    # 2月6日全国新增新冠肺炎确诊3143例，累计确诊 31161 例、死亡 636 例，目前防治情况如何？

    # urllist.append("https://www.zhihu.com/question/370825699")
    urllist.append(
        "https://www.zhihu.com/api/v4/questions/370825699/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Cis_labeled%2Cpaid_info%2Cpaid_info_content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_recognized%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics%3Bdata%5B%2A%5D.settings.table_of_content.enabled&limit=5&offset=0&platform=desktop&sort_by=default")
    # 2月9日全国新增确诊病例 3062 例，累计40171 例，目前防治情况如何？

    # destdir = "ZhiHuComments"

    for start_url in urllist:
        #answerurllist是每个回答的urllist
        next_url = [start_url]
        count = 0
        title = ""
        for url in next_url:
            html = requests.get(url, headers=headers)
            html.encoding = 'utf-8'
            bs = bs4.BeautifulSoup(html.text, "lxml")
            content = str(bs.p).split("<p>")[1].split("</p>")[0]

            c = json.loads(content)
            for item in c["data"]:
                #每一个item是一个回答
                count += 1
                if count % 20 == 0:
                    #每20个回答sleep一次
                    time.sleep(3)
                if count == 1:   #说明是第一个回答，那么就获取标题
                    title = item['question']['title']
                    print("开始爬取:" + title + "的评论：")
                currurl = item["url"]
                root_commenturl = currurl + "/root_comments"
                crawl_Rootcomments(root_commenturl,title)
                print("完成回答数目：" + str(count))
            next_url.append(c["paging"]["next"])
            if (c["paging"]["is_end"]):
                print("爬取完成" + title)
                break


if __name__ == '__main__':
    getAnswerList()