
import yt_dlp

def download_video(url):
    # إعدادات yt-dlp لتحميل الفيديو
    ydl_opts = {
        'format': 'best',  # اختر أفضل جودة
        'outtmpl': '%(title)s.%(ext)s',  # تحديد اسم الملف الذي سيتم تنزيله
    }

    try:
        # تنزيل الفيديو باستخدام yt-dlp
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("تم تحميل الفيديو بنجاح.")
    except Exception as e:
        print(f"حدث خطأ أثناء التنزيل: {e}")

if __name__ == '__main__':
    # طلب رابط الفيديو من المستخدم
    url = input("أدخل رابط الفيديو من YouTube: ")
    download_video(url)
