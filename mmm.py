strlist = "ここまでを残す<!--　twitterボタン　-->dwagtr"

a = "｢久山町の自然環境と共生できる住宅開発・提供が、会社の社会的使命｣<br/>というビジネスのタイミングを掴む亀頭社長の経営センスはさすがだ。凡人の１００倍の強い気概を持ちつつ、加えて経営者としてのしたたかさも大したものだ。</p><p>　山崎氏の久山町における活動遺産は捨てたものではない！！</p><!--　twitterボタン　--><a href="
def test(strlist):

    if '<!--　twitterボタン　-->' in strlist:
        sss = strlist.split("<!--　twitterボタン　-->")
        del sss[1]
        print(sss[0])
    if '<!--　記事内容ここまで　-->' in strlist:
        sss = strlist.split("<!--　twitterボタン　-->")
        del sss[1]
        print(sss[0])
    return exit()

test(a)