#coding=gbk
import os

def mkdir(path):
    # ����ģ��


    # ȥ����λ�ո�
    path = path.strip()
    # ȥ��β�� \ ����
    path = path.rstrip("\\")

    # �ж�·���Ƿ����
    # ����     True
    # ������   False
    isExists = os.path.exists(path)

    # �жϽ��
    if not isExists:
        # ����������򴴽�Ŀ¼
        # ����Ŀ¼��������
        os.makedirs(path)

        print path + '�����ɹ�'
        return True
    else:
        # ���Ŀ¼�����򲻴���������ʾĿ¼�Ѵ���
        print path + ' Ŀ¼�Ѵ���'
        return False


# ����Ҫ������Ŀ¼
for i in range (200):
    mkpath = ("F:\\qttc\\web\\"+str(i)+"\\")
    # ���ú���
    mkdir(mkpath)