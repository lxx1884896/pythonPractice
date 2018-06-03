# -*- coding:utf-8 -*-
#第 0001 题：**做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用**生成激活码**（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）

import random, string

import pymysql#python3下导入的mysql模块
forSelect = string.ascii_letters + "0123456789"
#print "forselect:"  +forSelect  #print 出来为一个字符串：26大写+26小写+0123456789
jihuoma = []
def generate(count, length):
    # count = 200
    # length = 20

    for x in range(count):                #共有count个激活码
        Re = ""
        for y in range(length):
            Re += random.choice(forSelect)#每次从26大写+26小写+0123456789中选出一个字符，共选length次，这些组成了一个激活码
        #print(Re)
        jihuoma.append(Re)
    #print jihuoma
    return jihuoma

def storeInMysql(codelist):
    try:
        conn = pymysql.connect(host='127.0.0.1',user='root',passwd='',db='jihuo')
        cur = conn.cursor()
    except BaseException as e:
        print(e)
    else:
        try:

            cur.execute('USE jihuo')
            cur.execute('''CREATE TABLE IF NOT EXISTS code(
                            id INT NOT NULL AUTO_INCREMENT,
                            code VARCHAR(32) NOT NULL,
                            PRIMARY KEY(id)
                        )''')
            cur.executemany('insert into code(code) value(%s)', jihuoma)
            cur.connection.commit()
        except BaseException as e:
            print(e)
    finally:
        cur.close()
        conn.close()

if __name__ == "__main__":
    storeInMysql(generate(200,20))
    print('OK!')