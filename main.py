import flet as ft
import warnings

warnings.filterwarnings("ignore")

def main(page: ft.Page):
    # إعدادات الصفحة
    page.title = "المشخص الطبي"
    page.rtl = True
    page.theme_mode = ft.ThemeMode.LIGHT
    
    # ... (بقية كود الأسئلة والمنطق الخاص بك) ...
    
    # تأكد أن الكود ينتهي بـ page.add أو الواجهة الرئيسية
    # (انسخ الكود الذي أرفقته لي بالكامل وضعه هنا)

# السطر الأهم لتشغيل التطبيق
ft.app(target=main)
