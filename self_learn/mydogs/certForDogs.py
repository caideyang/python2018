# encoding:utf-8
import xlrd
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import time, os


class CertForDog:
    """
    接受excel文件，处理生成证书；
    _excel :狗狗信息excel文件全Z路径
    _pic_path:生成的证书路径
    font:字体
    ggrandpa :曾祖父信息
    ggrandma :曾祖母信息

    """

    def __init__(self, excel, pic_path):
        self._excel = excel
        self._pic_path = pic_path
        self.font = {
            "namefont": ImageFont.truetype("C:\Windows\Fonts\simhei.ttf", 26),  # 姓名
            "breedfont": ImageFont.truetype("C:\Windows\Fonts\simhei.ttf", 26),  # 品种
            "colorfont": ImageFont.truetype("C:\Windows\Fonts\simhei.ttf", 26),  # 颜色
            "sexfont": ImageFont.truetype("C:\Windows\Fonts\simhei.ttf", 26),  # 性别
            "birthfont": ImageFont.truetype("C:\Windows\Fonts\simhei.ttf", 26),  # 出生日期
            "ownerfont": ImageFont.truetype("C:\Windows\Fonts\simhei.ttf", 26),  # 犬主
            "breaderfont": ImageFont.truetype("C:\Windows\Fonts\simhei.ttf", 26),  # 繁殖者
            "codenumfont": ImageFont.truetype("C:\Windows\Fonts\simhei.ttf", 26),  # 芯片号码
            "parentsfont": ImageFont.truetype("C:\Windows\Fonts\simhei.ttf", 24),  # 父母
            "grandparentsfont": ImageFont.truetype("C:\Windows\Fonts\simhei.ttf", 22),  # 祖父母
            "ggrandparentsfont": ImageFont.truetype("C:\Windows\Fonts\simhei.ttf", 21),  # 曾祖父母
        }
        self.font2 = {
            "namefont": ImageFont.truetype("C:\Windows\Fonts\simhei.ttf", 21),  # 姓名
            "breedfont": ImageFont.truetype("C:\Windows\Fonts\simhei.ttf", 21),  # 品种
            "colorfont": ImageFont.truetype("C:\Windows\Fonts\simhei.ttf", 21),  # 颜色
            "sexfont": ImageFont.truetype("C:\Windows\Fonts\simhei.ttf", 21),  # 性别
            "birthfont": ImageFont.truetype("C:\Windows\Fonts\simhei.ttf", 21),  # 出生日期
            "ownerfont": ImageFont.truetype("C:\Windows\Fonts\simhei.ttf", 21),  # 犬主
            "breaderfont": ImageFont.truetype("C:\Windows\Fonts\simhei.ttf", 21),  # 繁殖者
            "codenumfont": ImageFont.truetype("C:\Windows\Fonts\simhei.ttf", 21),  # 芯片号码
            "parentsfont": ImageFont.truetype("C:\Windows\Fonts\simhei.ttf", 18),  # 父母
            "grandparentsfont": ImageFont.truetype("C:\Windows\Fonts\simhei.ttf", 17),  # 祖父母
            "ggrandparentsfont": ImageFont.truetype("C:\Windows\Fonts\simhei.ttf", 15),  # 曾祖父母
        }
        self.ggandpa = []
        self.ggpandma = []

    def getExcel(self):
        return self._excel

    # 获取狗狗信息列表,index为excel中的sheet索引。
    def getDogInfo(self, index):
        dogs_info = []
        excel = xlrd.open_workbook(self._excel)
        sheet0 = excel.sheet_by_index(index)
        nrows = sheet0.nrows
        for dog in range(1, nrows):
            dog_info = sheet0.row_values(dog)
            dogs_info.append(dog_info)
        return dogs_info

    #
    def setGrandpa(self, *args):
        self.ggandpa = args

    def setGrandma(self, *args):
        self.ggpandma = args

    def crateDir(self):
        if os.path.exists(self._pic_path):
            print("需要创建的路径 【%s】 已经存在，生成的照片将存放到该路径！" % self._pic_path)
        else:
            os.mkdir(self._pic_path)
            print("路径 【%s】 创建成功，生成的照片将存放到该路径！" % self._pic_path)

    # 创建血统证书Detail
    def createCertDetail(self, template_path, dogs_info):
        for dog_info in dogs_info:
            image_file = template_path + '\\' + dog_info[-1] + "_info.png"  # 获取模板文件
            img = Image.open(image_file)
            # 新建一个画板
            draw = ImageDraw.Draw(img)
            if dog_info[-1] == "new":

                draw.text((160, 80), dog_info[2], (0, 0, 0), font=self.font2["namefont"])  # 狗狗名称
                draw.text((160, 145), dog_info[3].title(), (0, 0, 0), font=self.font2["breedfont"])  # 品种
                draw.text((160, 255), dog_info[4].title(), (0, 0, 0), font=self.font2["colorfont"])  # 毛色
                draw.text((160, 195), dog_info[5].title(), (0, 0, 0), font=self.font2["sexfont"])  # 公母
                draw.text((160, 322), dog_info[6].title(), (0, 0, 0), font=self.font2["birthfont"])  # 出生日期
                draw.text((160, 440), dog_info[7].title(), (0, 0, 0), font=self.font2["ownerfont"])  # 犬主人
                draw.text((160, 380), dog_info[8].title(), (0, 0, 0), font=self.font2["breaderfont"])  # 繁殖者
                draw.text((160, 575), dog_info[9].title(), (0, 0, 0), font=self.font2["codenumfont"])  # 芯片号码
                draw.text((160, 515), dog_info[10].title(), (0, 0, 0), font=self.font2["codenumfont"])  # 犬住址
                draw.text((70, 684), dog_info[11].title(), (0, 0, 0), font=self.font2["parentsfont"])  # 父亲信息
                draw.text((70, 932), dog_info[12].title(), (0, 0, 0), font=self.font2["parentsfont"])  # 母亲信息
                draw.text((234, 628), dog_info[13].title(), (0, 0, 0), font=self.font2["grandparentsfont"])  # 祖父信息
                draw.text((234, 745), dog_info[14].title(), (0, 0, 0), font=self.font2["grandparentsfont"])  # 祖母信息
                draw.text((234, 868), dog_info[15].title(), (0, 0, 0), font=self.font2["grandparentsfont"])  # 外祖父信息
                draw.text((234, 990), dog_info[16].title(), (0, 0, 0), font=self.font2["grandparentsfont"])  # 外祖母信息
                draw.text((448, 592), dog_info[17].title(), (0, 0, 0), font=self.font2["ggrandparentsfont"])  # 曾祖父
                draw.text((448, 655), dog_info[18].title(), (0, 0, 0), font=self.font2["ggrandparentsfont"])  # 曾祖母
                draw.text((448, 720), dog_info[19].title(), (0, 0, 0), font=self.font2["ggrandparentsfont"])  # 增外祖父
                draw.text((448, 781), dog_info[20].title(), (0, 0, 0), font=self.font2["ggrandparentsfont"])  # 增外祖母
                draw.text((448, 845), dog_info[21].title(), (0, 0, 0), font=self.font2["ggrandparentsfont"])  # 外曾祖父
                draw.text((448, 906), dog_info[22].title(), (0, 0, 0), font=self.font2["ggrandparentsfont"])  # 外曾祖母
                draw.text((448, 967), dog_info[23].title(), (0, 0, 0), font=self.font2["ggrandparentsfont"])  # 外曾外祖父
                draw.text((448, 1030), dog_info[24].title(), (0, 0, 0), font=self.font2["ggrandparentsfont"])  # 外曾外祖母
                tmp_number = dog_info[6].replace('/', '') + dog_info[9][-2:]
                # cert_id = tmp_number[0]+tmp_number[2:]+"\nCKU-000390409"
                cert_id = tmp_number[0] + tmp_number[2:]

                draw.text((115, 23), cert_id, (0, 0, 0), font=self.font2["grandparentsfont"])  # 证书编号

            else:
                draw.text((160, 55), dog_info[2], (0, 0, 0), font=self.font2["namefont"])  # 狗狗名称
                draw.text((160, 110), dog_info[3].title(), (0, 0, 0), font=self.font2["breedfont"])  # 品种
                draw.text((160, 225), dog_info[4].title(), (0, 0, 0), font=self.font2["colorfont"])  # 毛色
                draw.text((160, 165), dog_info[5].title(), (0, 0, 0), font=self.font2["sexfont"])  # 公母
                draw.text((160, 285), dog_info[6].title(), (0, 0, 0), font=self.font2["birthfont"])  # 出生日期
                draw.text((160, 410), dog_info[7].title(), (0, 0, 0), font=self.font2["ownerfont"])  # 犬主人
                draw.text((160, 350), dog_info[8].title(), (0, 0, 0), font=self.font2["breaderfont"])  # 繁殖者
                draw.text((160, 480), dog_info[9].title(), (0, 0, 0), font=self.font2["codenumfont"])  # 芯片号码
                draw.text((73, 600), dog_info[11].title(), (0, 0, 0), font=self.font2["parentsfont"])  # 父亲信息
                draw.text((68, 845), dog_info[12].title(), (0, 0, 0), font=self.font2["parentsfont"])  # 母亲信息
                draw.text((240, 540), dog_info[13].title(), (0, 0, 0), font=self.font2["grandparentsfont"])  # 祖父信息
                draw.text((240, 660), dog_info[14].title(), (0, 0, 0), font=self.font2["grandparentsfont"])  # 祖母信息
                draw.text((240, 790), dog_info[15].title(), (0, 0, 0), font=self.font2["grandparentsfont"])  # 外祖父信息
                draw.text((240, 908), dog_info[16].title(), (0, 0, 0), font=self.font2["grandparentsfont"])  # 外祖母信息
                draw.text((450, 510), dog_info[17].title(), (0, 0, 0), font=self.font2["ggrandparentsfont"])  # 曾祖父
                draw.text((450, 577), dog_info[18].title(), (0, 0, 0), font=self.font2["ggrandparentsfont"])  # 曾祖母
                draw.text((450, 637), dog_info[19].title(), (0, 0, 0), font=self.font2["ggrandparentsfont"])  # 增外祖父
                draw.text((450, 700), dog_info[20].title(), (0, 0, 0), font=self.font2["ggrandparentsfont"])  # 增外祖母
                draw.text((450, 760), dog_info[21].title(), (0, 0, 0), font=self.font2["ggrandparentsfont"])  # 外曾祖父
                draw.text((450, 828), dog_info[22].title(), (0, 0, 0), font=self.font2["ggrandparentsfont"])  # 外曾祖母
                draw.text((450, 885), dog_info[23].title(), (0, 0, 0), font=self.font2["ggrandparentsfont"])  # 外曾外祖父
                draw.text((450, 947), dog_info[24].title(), (0, 0, 0), font=self.font2["ggrandparentsfont"])  # 外曾外祖母

            draw = ImageDraw.Draw(img)
            dog_name = dog_info[3] + "-" + dog_info[2] + "-" + dog_info[0] + "-" + dog_info[1] + ".png"
            img.save(self._pic_path + "\\" + dog_name)
            print("%s 创建完毕" % dog_name)

        # 创建血统证书

    def createCert(self, template_path, dogs_info):
        for dog_info in dogs_info:
            image_file = template_path + '\\' + dog_info[-1] + ".jpg"  # 获取模板文件
            img = Image.open(image_file)
            # 新建一个画板
            draw = ImageDraw.Draw(img)
            if dog_info[-1] == "new":

                draw.text((300, 310), dog_info[2], (0, 0, 0), font=self.font["namefont"])  # 狗狗名称
                draw.text((300, 395), dog_info[3].title(), (0, 0, 0), font=self.font["breedfont"])  # 品种
                draw.text((300, 557), dog_info[4].title(), (0, 0, 0), font=self.font["colorfont"])  # 毛色
                draw.text((300, 478), dog_info[5].title(), (0, 0, 0), font=self.font["sexfont"])  # 公母
                draw.text((300, 646), dog_info[6].title(), (0, 0, 0), font=self.font["birthfont"])  # 出生日期
                draw.text((300, 718), dog_info[7].title(), (0, 0, 0), font=self.font["breaderfont"])  # 犬主人
                draw.text((300, 794), dog_info[8].title(), (0, 0, 0), font=self.font["breaderfont"])  # 繁殖者
                draw.text((300, 960), dog_info[9].title(), (0, 0, 0), font=self.font["codenumfont"])  # 芯片号码
                draw.text((300, 880), dog_info[10].title(), (0, 0, 0), font=self.font["codenumfont"])  # 犬住址
                draw.text((868, 493), dog_info[11].title(), (0, 0, 0), font=self.font["parentsfont"])  # 父亲信息
                draw.text((868, 855), dog_info[12].title(), (0, 0, 0), font=self.font["parentsfont"])  # 母亲信息
                draw.text((1158, 413), dog_info[13].title(), (0, 0, 0), font=self.font["grandparentsfont"])  # 祖父信息
                draw.text((1156, 588), dog_info[14].title(), (0, 0, 0), font=self.font["grandparentsfont"])  # 祖母信息
                draw.text((1158, 775), dog_info[15].title(), (0, 0, 0), font=self.font["grandparentsfont"])  # 外祖父信息
                draw.text((1156, 946), dog_info[16].title(), (0, 0, 0), font=self.font["grandparentsfont"])  # 外祖母信息
                draw.text((1472, 365), dog_info[17].title(), (0, 0, 0), font=self.font["ggrandparentsfont"])  # 曾祖父
                draw.text((1472, 460), dog_info[18].title(), (0, 0, 0), font=self.font["ggrandparentsfont"])  # 曾祖母
                draw.text((1472, 544), dog_info[19].title(), (0, 0, 0), font=self.font["ggrandparentsfont"])  # 增外祖父
                draw.text((1472, 638), dog_info[20].title(), (0, 0, 0), font=self.font["ggrandparentsfont"])  # 增外祖母
                draw.text((1472, 727), dog_info[21].title(), (0, 0, 0), font=self.font["ggrandparentsfont"])  # 外曾祖父
                draw.text((1472, 823), dog_info[22].title(), (0, 0, 0), font=self.font["ggrandparentsfont"])  # 外曾祖母
                draw.text((1472, 908), dog_info[23].title(), (0, 0, 0), font=self.font["ggrandparentsfont"])  # 外曾外祖父
                draw.text((1472, 1005), dog_info[24].title(), (0, 0, 0), font=self.font["ggrandparentsfont"])  # 外曾外祖母
                tmp_number = dog_info[6].replace('/', '') + dog_info[9][-2:]
                # cert_id = tmp_number[0] + tmp_number[2:]+"\nCKU-000390409"
                cert_id = tmp_number[0] + tmp_number[2:]
                draw.text((262, 123), cert_id, (0, 0, 0), font=self.font["grandparentsfont"])  # 证书编号
            else:
                draw.text((340, 385), dog_info[2], (0, 0, 0), font=self.font["namefont"])  # 狗狗名称
                draw.text((340, 470), dog_info[3].title(), (0, 0, 0), font=self.font["breedfont"])  # 品种
                draw.text((340, 630), dog_info[4].title(), (0, 0, 0), font=self.font["colorfont"])  # 毛色
                draw.text((340, 545), dog_info[5].title(), (0, 0, 0), font=self.font["sexfont"])  # 公母
                draw.text((340, 713), dog_info[6].title(), (0, 0, 0), font=self.font["birthfont"])  # 出生日期
                draw.text((340, 795), dog_info[7].title(), (0, 0, 0), font=self.font["ownerfont"])  # 犬主人
                draw.text((340, 884), dog_info[8].title(), (0, 0, 0), font=self.font["breaderfont"])  # 繁殖者
                draw.text((340, 980), dog_info[9].title(), (0, 0, 0), font=self.font["codenumfont"])  # 芯片号码
                draw.text((888, 525), dog_info[11].title(), (0, 0, 0), font=self.font["parentsfont"])  # 父亲信息
                draw.text((888, 887), dog_info[12].title(), (0, 0, 0), font=self.font["parentsfont"])  # 母亲信息
                draw.text((1180, 440), dog_info[13].title(), (0, 0, 0), font=self.font["grandparentsfont"])  # 祖父信息
                draw.text((1180, 615), dog_info[14].title(), (0, 0, 0), font=self.font["grandparentsfont"])  # 祖母信息
                draw.text((1180, 800), dog_info[15].title(), (0, 0, 0), font=self.font["grandparentsfont"])  # 外祖父信息
                draw.text((1180, 975), dog_info[16].title(), (0, 0, 0), font=self.font["grandparentsfont"])  # 外祖母信息
                draw.text((1488, 392), dog_info[17].title(), (0, 0, 0), font=self.font["ggrandparentsfont"])  # 曾祖父
                draw.text((1488, 488), dog_info[18].title(), (0, 0, 0), font=self.font["ggrandparentsfont"])  # 曾祖母
                draw.text((1488, 574), dog_info[19].title(), (0, 0, 0), font=self.font["ggrandparentsfont"])  # 增外祖父
                draw.text((1488, 670), dog_info[20].title(), (0, 0, 0), font=self.font["ggrandparentsfont"])  # 增外祖母
                draw.text((1488, 759), dog_info[21].title(), (0, 0, 0), font=self.font["ggrandparentsfont"])  # 外曾祖父
                draw.text((1488, 851), dog_info[22].title(), (0, 0, 0), font=self.font["ggrandparentsfont"])  # 外曾祖母
                draw.text((1488, 938), dog_info[23].title(), (0, 0, 0), font=self.font["ggrandparentsfont"])  # 外曾外祖父
                draw.text((1488, 1036), dog_info[24].title(), (0, 0, 0), font=self.font["ggrandparentsfont"])  # 外曾外祖母

            draw = ImageDraw.Draw(img)
            dog_name = dog_info[3] + "-" + dog_info[2] + "-" + dog_info[0] + "-" + dog_info[1] + ".jpg"
            img.save(self._pic_path + "\\" + dog_name)
            print("%s 创建完毕" % dog_name)


if __name__ == "__main__":
    # 创建一个对象，导入狗狗信息D:\cert_dog.xlsx  ，导出位置D:\20180305
    cert = CertForDog('D:\\mydogs\\data\\20180527.xlsx', 'D:\\mydogs\\data\\20180527')
    # 创建导出位置
    cert.crateDir()
    # 获取狗狗信息，参数0 是获取第一个sheet的值
    dogs_info = cert.getDogInfo(0)
    #     print(dogs_info)
    # 根据模板，创建证书，模板位置：'D:\template'
    cert.createCert('D:\\mydogs\\template', dogs_info)
    cert.createCertDetail('D:\\mydogs\\template', dogs_info)













