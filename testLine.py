import requests
import sys
token ="BggmSwVip2mh1PUc9sQusUjS8aUlnwZJQpA2Cs8M3yl"

class LINE:
    def __init__(self, token):
        self.url = 'https://notify-api.line.me/api/notify'
        self.LINE_HEADERS = {'Authorization': 'Bearer ' + token}
        self.session = requests.Session()

    def sendtext(self, msg):
        response = self.session.post(self.url,
                                     headers=self.LINE_HEADERS,
                                     params={"message": msg})
        return response.text

    def sendpicture(self,msg,picurl):
        response = self.session.post(self.url,
                                     headers=self.LINE_HEADERS,
                                     params={'message':msg,'imageThumbnail':picurl,'imageFullsize':picurl})
        return response.text

    def sendsticker(self,msg,stickerID,stickerPackageID):
        response = self.session.post(self.url,
                                     headers=self.LINE_HEADERS,
                                     params={'message':msg,'stickerPackageId':stickerPackageID,'stickerId':stickerID})
        return response.text


# a = LINE(token).sendtext("hello")
# b = LINE(token).sendpicture("myimage","https://www.mystudy.icu/wp-content/uploads/2019/12/365073.jpg")
c = LINE(token).sendsticker("test sendata",19,2)
#  a.sendtext("hello")
print(c)       
