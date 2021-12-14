import glob
import json
import bs4
import sys

sys.setrecursionlimit(10000)


def get_html():
    global title, body
    found = glob.glob("C:/Users/OW_KAKUTA/PycharmProjects/scraping_data-max/test/*.html",
                      recursive=True)
    n = 0
    s = 1

    data_format = {"file_path": "", "title": "", "body": "", "img": {}}
    for i in range(len(found)):
        count = 0
        print(found[n:n + s:1][0])
        path = found[n:n + s:1]
        soup = bs4.BeautifulSoup(open(path[0], encoding="utf-8", errors='ignore'), "html.parser")

        if soup.find("div", class_="kijinews_text01"):
            body = soup.find("div", class_="kijinews_text01")
            title = soup.find("title")

        elif soup.find("div", class_="entry-body"):
            title = soup.find("title")
            body = soup.find("div", class_="entry-body")

        elif soup.find("topnews_area03"):
            title = soup.find("title")
            body = soup.find("topnews_area03")

        elif soup.find("left_area"):
            title = soup.find("title")
            body = soup.find("left_area")

        elif soup.find("body"):
            title = soup.find("title")
            body = soup.find("body")

        print(i)
        directory_path = path[0].rfind("\\")

        file_path = path[0].find("scraping_data-max/")
        with open("../datamax-json/{}.json".format(path[0][directory_path:]), 'w', encoding="utf-8",
                  errors="ignore") as f:
            data_format["file_path"] = path[0][file_path:]
            if title is not None:
                change_title = title.text.rfind("：")
                data_format["title"] = title.text[:change_title].replace("　", "")
            else:
                data_format["title"] = "is None"

            if "<!--　twitterボタン　-->" in str(body):
                count = 0
                links = body.findAll("img")
                body = str(body).split("<!--　twitterボタン　-->")
                del body[1]
                data_format["body"] = str(body[0])

                for link in links:
                    if "twitter.png" in str(link.get("src")):
                        pass
                    else:
                        count += 1
                        print(link)
                        data_format["img"].setdefault("img_source{}".format(str(count)), link.get("src"))

            elif "<!-- トップニュースend -->" in str(body):
                count = 0
                links = body.findAll("img")
                body = str(body).split("<!-- トップニュースend -->")
                del body[1]
                data_format["body"] = body[0]
                for link in links:
                    if "twitter.png" in str(link.get("src")):
                        pass
                    else:
                        count += 1
                        data_format["img"].setdefault("img_source{}".format(str(count)), link.get("src"))

            elif "<!--　記事内容ここまで　-->" in str(body):
                count = 0
                links = body.findAll("img")
                body = str(body).split("<!--　記事内容ここまで　-->")
                del body[1]
                data_format["body"] = body[0]
                for link in links:
                    if "twitter.png" in str(link.get("src")):
                        pass
                    else:
                        count += 1
                        data_format["img"].setdefault("img_source{}".format(str(count)), link.get("src"))
            else:
                for link in links:
                    if "twitter.png" in str(link.get("src")):
                        pass
                    else:
                        count += 1
                        data_format["img"].setdefault("img_source{}".format(str(count)), link.get("src"))
            print(data_format["img"])
            json_data = json.dump(data_format, f)

        n += s


if __name__ == '__main__':
    get_html()
