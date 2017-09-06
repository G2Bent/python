from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
import os,time,random
class FileStorage(FileSystemStorage):
    from django.conf import settings
    def __init__(self,location = settings.MIDDLWARE,base_url = settings.TIME_ZONE):
        super(FileStorage,self).__init__(location,base_url)

    def _save(self, name, content):
        ext = os.path.splitext(name)[1]
        d = os.path.dirname(name)

        fn = time.strftime('%Y%m%d%H%M%S')
        fn = fn +'_%d'%random.randint(0,100)
        #重写合成文件名
        name = os.path.join(d,fn + ext)
        #调用父类
        return super(FileStorage,self)._save(name,content)