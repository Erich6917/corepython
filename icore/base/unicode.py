# -*- coding: utf-8 -*-
# @Time    : 2017/12/13 
# @Author  : LIYUAN134
# @File    : unicode.py
# @Commment: 
#            
import chardet

msg = '资管新规加上金融去杠杆，引发市场对年底出现阶段性兑付风险的担忧，叠加目前流动性环境中性偏紧，沪深300指数在银行为首的蓝筹带动下连跌三周。从目前权重股的估值水平来看，只要不发生系统性风险，市场调整正接近底部区域。　　国家统计局公布的11月物价数据显示，居民消费价格总水平同比上涨1.7%，较10月同比涨幅下降0.2个百分点；工业生产者出厂价格同比上涨5.8%，涨幅较上月下降1.1个百分点，总体符合市场预期。从近期猪价变动的趋势来看，环保因素及消费旺季有望导致猪价同比降幅大幅收窄，从而带动食品端CPI走强。近期工业品以及原油走势趋稳，PPI有望在基数效应的共同作用下，同比涨幅缓慢下行。　　另外，海关总署12月8日公布的我国11月进出口数据显示，11月我国出口同比增速为12.3%，进口同比增长17.7%，大幅好于预期，出口增长超预期令贸易顺差较上月小幅回升至402.1亿美元。这一数据与11月制造业PMI新出口订单反弹一致，同时海外国家PMI景气指数继续回升意味着外需改善具有较强的持续性。　　11月末官方外汇储备环比上升100.7亿美元，连续10个月回升，主要由于美元贬值带来的估值效应推动外汇储备回升。以中国为代表的新兴经济体逐渐走出衰退加入全球复苏的进程中，当前发达国家与新兴市场货币政策分化，美、英等国陆续加息，而金砖国家货币环境维持宽松。与美、德、英三国10年期国债利率纷纷上行形成对比的是，今年7月南非5年来首次降息25BP，8月印度央行降息25BP，9月俄罗斯央行降息50BP，12月巴西央行降息50BP。经济复苏的传导效应加上货币政策的差异，拉动新兴经济体贸易部门快速复苏。由于利差处于高位，有利于中国等新兴市场国家保持货币政策的相对独立，进而维持币值稳定，利于全球流动性从发达国家流向新兴市场，推升新兴市场资产价格，而中国将是其中最大的收益国。　　人民币双向波动预期的形成，以及10年期国债收益率的走高，不仅显示出国内产能出清和杠杆去化方面取得的成效，更体现出市场对宏观政策和金融监管的认可。上周末召开的中央政治局经济工作会议提出，2018年宏观调控侧重于在经济稳增长的基础上更加看重质量，特别要求生态环境质量总体改善。由此可见，未来宏观调控将围绕经济发展的质量而展开，继续调整经济结构，深化实体经济发展的市场化道路，提高资源配置效率，保持中性审慎的货币政策，侧重降低杠杆率和防范化解重大风险。对此定调，市场给出了积极反映，确立了2018年“制造+创新”政策周期的格局。　　当前，中小创业绩占优，制造业毛利率受挤压的状况逐步改善，产能出清初见成效，ROE有望延续上行趋势。外汇占款持续增加，基础货币增长和金融去杠杆接近尾声，有利于M2增速见底反弹，长期国债利率短期进一步上行空间受限，从边际上推动市场的风险偏好，经过了将近四个月的振荡调整，我们认为市场接近底部区域，建议逢低买入。　　（作者单位：宝城期货）进入【新浪财经股吧】讨论'

fencoding = chardet.detect(msg)
print fencoding