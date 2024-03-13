# from plyer import notification
# import time
# if __name__ == '_main_':
#    while True:
#     notification.notify(
#         title = "Sir please,Take rest",
#         message = "Rest helps prevent injuries and improve overall performance. It also aids in muscle repair, reduces inflammation, and supports a healthy immune system. Additionally, rest helps manage stress levels and lowers blood pressure, contributing to a healthier heart.",
#         app_icon ="D:/VSpython/JavaS/rest-10.png",
#         timeout= 5)
#     time.sleep(20)
# import time  
from winotify import Notification, audio 
tono = Notification(app_id="NAMAZ_ALERT",
                    title="***আসর***",
                    msg="স্যার বিকাল হয়ে গেসে, আপনার নামাজের সময় হয়েছে ",
                    icon ="D:/VSpython/JavaS/namaz.png",
                    duration="short")
tono.add_actions( label="I'm in", launch="https://www.youtube.com/watch?v=AFKC1T9zwMc")
tono.set_audio(audio.LoopingCall10, loop= True)
tono.show()

    