import requests
import exrex

class Zidian03:
    def __init__(self):
        pass


#取出字典内容，返回的是一个列表
    def get_txt_contents(self, file_name):
        with open(f"{file_name}", 'r') as f:
            #去除\n换行方法
            zidian_list02 = f.read().splitlines()
            #print(zidian_list)
        return zidian_list02



#拼接url
    def get_url(self, url, zidian_list02):
        new_url_list = []   #给一个空列表 new_url_list
        for i in zidian_list02:    #遍历列表
            new_url = "http://" + url +'/' + i
            print(new_url)
            res = requests.get(new_url)
            #对请求结果进行识别
            if res.status_code == 200 or res.status_code == 302 or res.status_code == 403:
                new_url_list.append(new_url)
        return new_url_list


if __name__ == '__main__':
    #实例化对象,调用类
    zidian03 = Zidian03()
    zidian_list03 = zidian03.get_txt_contents('zidian.txt')
    url = input("请输入要扫描的url:")
    print(zidian03.get_url(url, zidian_list03))           #这个打印就是打印get_url()函数里面的new_url_list列表
#结果为['http://www.gxaedu.com/']
