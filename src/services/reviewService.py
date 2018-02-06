#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    #Author: smilesmith
    #Date: 2018-02-05
    #Desc: 回顾分析服务
"""

from src.daos import answerDao


def get_review_datas():
    """获取所有结果"""
    ai_results = answerDao.get_all_result()

    correct_results = answerDao.get_all_correct_result()

    return {'ai_results': ai_results, 'correct_results': correct_results}
