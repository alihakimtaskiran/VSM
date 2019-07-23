#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 13:55:57 2019

@author: ali
"""
import numpy as np
wordlist=[]

def import_contents(_doc_):
    _doc_=_doc_.lower()
    _doc_=_doc_.replace('"',' ')
    _doc_=_doc_.replace('!',' ')
    _doc_=_doc_.replace('\'',' ')
    _doc_=_doc_.replace('^',' ')
    _doc_=_doc_.replace('+',' ')
    _doc_=_doc_.replace('&',' ')
    _doc_=_doc_.replace('/',' ')
    _doc_=_doc_.replace('(',' ')
    _doc_=_doc_.replace(')',' ')
    _doc_=_doc_.replace('=',' ')
    _doc_=_doc_.replace('_',' ')
    _doc_=_doc_.replace(';',' ')
    _doc_=_doc_.replace(',',' ')
    _doc_=_doc_.replace('*',' ')
    _doc_=_doc_.replace('.',' ')
    _doc_=_doc_.replace(':',' ')
    _doc_=_doc_.replace('`',' ')
    _doc_=_doc_.replace('}',' ')
    _doc_=_doc_.replace(']',' ')
    _doc_=_doc_.replace('[',' ')
    _doc_=_doc_.replace('{',' ')
    _doc_=_doc_.replace('¾',' ')
    _doc_=_doc_.replace('½',' ')
    _doc_=_doc_.replace('#',' ')
    _doc_=_doc_.replace('>',' ')
    _doc_=_doc_.replace('<',' ')
    _doc_=_doc_.replace('          ',' ')
    _doc_=_doc_.replace('         ',' ')
    _doc_=_doc_.replace('        ',' ')
    _doc_=_doc_.replace('      ',' ')
    _doc_=_doc_.replace('     ',' ')
    _doc_=_doc_.replace('    ',' ')
    _doc_=_doc_.replace('   ',' ')
    _doc_=_doc_.replace('  ',' ')
    _doc_=_doc_.replace('\n',' ')
    
    _doc_=_doc_.split(" ")
    
    index_list=[]
    for i in range(len(_doc_)):
        if _doc_[i]=="":
            index_list.append(i)
        else:
            pass
    index_list.reverse()
    for i in index_list:
        _doc_.pop(i)
    del index_list
    
    for i in _doc_:
        if not i in wordlist:
            wordlist.append(i)
        else:
            pass 
        
class func:
    def is_in(_x_):
        if not str(_x_).lower() in wordlist:
            return False
        else:
            return True
    
    def doc2vec(_doc_):
        vec=[0]*len(wordlist)
        for i in range(len(wordlist)):
            n=_doc_.lower().count(wordlist[i])
            vec[i]=n
        return np.array(vec)   

    def cossim(_a_,_b_):
        return np.matmul(_a_,_b_)/(np.linalg.norm(_a_,2)*np.linalg.norm(_b_,2))
        
        
            
