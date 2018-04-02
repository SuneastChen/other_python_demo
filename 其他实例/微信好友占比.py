import itchat  
import echarts  
from echarts import Echart,Legend,Pie  
  
itchat.auto_login(hotReload=True)  
itchat.dump_login_status()  
  
friends = itchat.get_friends(update=True)[:]  
total = len(friends) - 1  
man = women = other = 0  
  
for friend in friends[0:] :  
    sex = friend["Sex"]  
    if sex == 1 :  
        man += 1  
    elif sex == 2 :  
        women += 1  
    else :  
        other += 1  
  
print("男性好友：%.2f%%" % (float(man) / total * 100))  
print("女性好友：%.2f%%" % (float(women) / total * 100))  
print("其他：%.2f%%" % (float(other) / total * 100))  
# itchat.send(u'程序消息发送测试','filehelper')  
  
chart = Echart('%s的微信好友性别比例' % (friends[0]['NickName']),'from Wechat')  
chart.use(Pie('WeChat',  
              [{'value': man, 'name': '男性 %.2f%%' % (float(man) / total * 100)},  
               {'value': women, 'name': '女性 %.2f%%' % (float(women) / total * 100)},  
               {'value': other, 'name': '其他 %.2f%%' % (float(other) / total * 100)}],  
              radius=["50%", "70%"]))  
chart.use(Legend(['man','women','other']))  
del chart.json["xAxis"]  
del chart.json["yAxis"]  
chart.plot()