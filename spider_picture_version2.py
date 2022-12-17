import requests
import json
"""
version2
"""
# https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1670164898311_R&pv=&ic=&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&dyTabStr=MCwzLDYsNCw1LDEsOCw3LDIsOQ%3D%3D&ie=utf-8&sid=&word=%E5%8A%A8%E6%BC%AB

headers = {
    "Host": "image.baidu.com",
    "Cookie": "BDqhfp=%E5%8A%A8%E6%BC%AB%26%26-10-1undefined%26%268364%26%269; BIDUPSID=633DBE996B8FF3C8C468EEC5725F44F1; PSTM=1667711202; BAIDUID=633DBE996B8FF3C8033B690572DCDCE2:FG=1; BAIDUID_BFESS=633DBE996B8FF3C8033B690572DCDCE2:FG=1; ZFY=:AZLVAVUXbk0EZCCK98sVRIwyMPfIvN3lto4EyxILmRc:C; H_PS_PSSID=37855_36554_37840_37766_37760_26350_22158_37882; delPer=0; PSINO=6; BA_HECTOR=04240g058500a4al2l018oua1hopajr1g; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; BDRCVFR[X_XKQks0S63]=mk3SLVN4HKm; firstShowTip=1; indexPageSugList=%5B%22%E5%8A%A8%E6%BC%AB%22%5D; cleanHistoryStatus=0; userFrom=null; ab_sr=1.0.1_ZmNiNzk0NWRiMjhjOGRiZDY1NjMwODkxYjdlMDAwMGJmMDhjYjMwNGM5MGQwOGFjMjJmN2Y1NTNmNzkxZjEzOWM3Yjg0NWQ3ZGVjNzMwOWMzMTQ2MzI1ZTcwY2JkYWIxOWNiZDMzNTk1ZjVkMWEzNWRiNjI2MGMyNTVkMjlkODVhOWY3Njk0MzFlOGI5N2UzNDQyNzNkZGUzMWQ1YzM2OQ==",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}

num = 1
page = 11


class spider_sp:
    __flag = True
    __instance = None

    def spider_pictue(self, num, page):
        pass

    def spider_music(self):
        pass

    def spider_vedio(self):
        pass


class spider(object):
    __flag = True
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance:
            cls.__instance = super().__new__(cls)
            return cls.__instance

    def __init__(self, file_number, page_number):
        if self.__flag:
            self.num = file_number
            self.page = page_number
            __flag = False

    def spider_picture(self, num, page):
        for i in range(1, page):
            url = f"https://image.baidu.com/search/acjson?tn=resultjson_com&logid=8419943923068396246&ipn=rj&ct=201326592&is=&fp=result&fr=&word=%E5%8A%A8%E6%BC%AB&queryWord=%E5%8A%A8%E6%BC%AB&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&expermode=&nojc=&isAsync=&pn={i * 30}&rn=30&gsm=14a&1670165078825="
            response = requests.get(url, headers=headers)
            # print(response.text)
            json_data = response.json()
            data_list = json_data["data"]
            for data in data_list[:-1]:
                print(data)
                picture_url = data["hoverURL"]
                image_data = requests.get(picture_url).content
                with open(f"image/pic_{num}.jpg", "wb") as fp:
                    fp.write(image_data)
                num += 1


if __name__ == "__main__":
    worker_1 = spider(1, 5)
    worker_1.spider_picture()
    # try:
    #     worker_1.spider_picture()
    # except Exception:
    #     print(f"爬取图片出现错误！请检查header或者URL连接！")
# if __name__ == "__main__":
#     spider_picture(1, 5)
