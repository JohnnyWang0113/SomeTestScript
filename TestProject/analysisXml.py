import xml.sax


# 解析xml文件

class FundHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.no = ""
        self.value = ""
        self.issuer = ""
        self.share = ""

    # 元素开始调用
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "fund":
            title = attributes["name"]
            print("基金名称：", title)

    # 读取字符时调用
    def characters(self, content):
        if self.CurrentData == "no":
            self.no = content
        elif self.CurrentData == "value":
            self.value = content
        elif self.CurrentData == "Issuer":
            self.issuer = content
        elif self.CurrentData == "share":
            self.share = content

    # 元素结束调用
    def endElement(self, tag):
        if self.CurrentData == "no":
            print("基金代码:", self.no)
        elif self.CurrentData == "value":
            print("净值:", self.value)
        elif self.CurrentData == "Issuer":
            print("发行方:", self.issuer)
        elif self.CurrentData == "share":
            print("总份额:", self.share)
        self.CurrentData = ""


if __name__ == "__main__":
    # 创建一个 XMLReader
    parser = xml.sax.make_parser()
    # 关闭命名空间
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # 重写 ContextHandler
    Handler = FundHandler()
    parser.setContentHandler(Handler)

    parser.parse("funds.xml")
