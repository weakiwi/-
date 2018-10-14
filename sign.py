#cpding=utf-8
from ghost import Ghost
import requests

def signYaohuo():
    ghost = Ghost()
    session = ghost.start()
    resp = session.open("http://yaohuo.me/waplogin.aspx")
    session.set_field_value("[name=logname]", 用户名)
    session.set_field_value("[name=logpass]", 密码)
    session.click("[type=submit]",btn=0)
    session.wait_for_selector("[href='/signin/signin.aspx']")
    session.open("http://yaohuo.me/signin/signin.aspx")
    session.set_field_value("[name=content]", "today is a new day")
    session.click("[name=g]")
    session.wait_for_selector(".tip")
    return session.evaluate("document.documentElement.getElementsByTagName('head')")
def signNeu6():
    ghost = Ghost()
    session = ghost.start()
    resp = session.open("http://bt.neu6.edu.cn/member.php")
    session.set_field_value("[name=username]", 用户名)
    session.set_field_value("[name=password]", 密码)
    session.click("[type=checkbox]")
    session.click("[type=submit]")
    session.open("http://bt.neu6.edu.cn/member.php")
    return session

#print signYaohuo()
signNeu6()
