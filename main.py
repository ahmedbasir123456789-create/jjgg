import flet as ft
import warnings

# --- إضافة سحرية لإخفاء التحذيرات الصفراء ---
warnings.filterwarnings("ignore")

def main(page: ft.Page):
    # --- 1. إعدادات الصفحة ---
    page.title = "المشخص الطبي"
    page.rtl = True
    page.theme_mode = ft.ThemeMode.LIGHT
    page.scroll = "hidden"
    page.window_width = 390
    page.window_height = 844
    
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # --- 2. البيانات ---
    questions = [
        "1. هل تعاني من ارتفاع في درجة الحرارة؟",
        "2. هل تشعر بسعال جاف؟",
        "3. هل تشعر بضيق في التنفس؟",
        "4. هل تعاني من سيلان في الأنف؟",
        "5. هل تشعر بألم في الحلق؟",
        "6. هل فقدت حاسة الشم أو التذوق مؤخراً؟",
        "7. هل تشعر بصداع شديد؟",
        "8. هل تشعر بآلام في العضلات؟",
        "9. هل تشعر بالتعب الشديد والإرهاق؟",
        "10. هل تعاني من عطس مستمر؟"
    ]
    
    answers = []
    current_index = 0

    # --- 3. الحاوية الرئيسية ---
    main_container = ft.Container(
        width=350,
        height=550, 
        padding=20,
        bgcolor="white",
        border_radius=15,
        shadow=ft.BoxShadow(blur_radius=10, color="grey"),
        alignment=ft.Alignment(0, 0),
    )

    # --- 4. واجهة الترحيب ---
    def build_welcome_view():
        return ft.Column(
            [
                ft.Text("🏥", size=80), 
                ft.Text("أهلاً بك", size=28, weight="bold", color="blue"),
                ft.Text("في تطبيق المشخص الطبي", size=20, weight="bold"),
                ft.Divider(color="grey"),
                ft.Text(
                    "سيقوم هذا النظام بطرح بعض الأسئلة\nلتحليل الأعراض وتقديم نصيحة مبدئية.",
                    size=16, 
                    color="grey", 
                    text_align="center"
                ),
                ft.Container(height=30),
                
                # استخدمنا الزر الجديد المتوافق
                ft.Button(
                    "ابدأ الفحص الآن",
                    width=200, height=50,
                    style=ft.ButtonStyle(bgcolor="blue", color="white"),
                    on_click=lambda e: update_view(build_question_view())
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10
        )

    # --- 5. واجهة السؤال ---
    def build_question_view():
        return ft.Column(
            [
                ft.Text("فحص الأعراض السريع", size=14, color="grey", text_align="center"),
                ft.ProgressBar(width=300, value=current_index/len(questions), color="blue"),
                ft.Divider(height=30, color="transparent"),
                
                ft.Container(
                    content=ft.Text(
                        questions[current_index], 
                        size=22, 
                        weight="bold", 
                        text_align="center",
                        color="black"
                    ),
                    alignment=ft.Alignment(0, 0),
                    expand=True 
                ),
                
                ft.Divider(height=20, color="transparent"),
                
                ft.Row(
                    [
                        ft.Button(
                            "نعم", 
                            width=130, height=50,
                            style=ft.ButtonStyle(bgcolor="green", color="white"),
                            on_click=lambda e: answer_clicked(True)
                        ),
                        ft.Button(
                            "لا", 
                            width=130, height=50,
                            style=ft.ButtonStyle(bgcolor="red", color="white"),
                            on_click=lambda e: answer_clicked(False)
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=20
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10
        )

    # --- 6. واجهة النتيجة ---
    def build_result_view():
        result_text = "يرجى المحاولة مرة أخرى."
        result_emoji = "💚"
        
        if len(answers) >= len(questions):
            if answers[0] and answers[1] and answers[5]:
                result_text = "اشتباه بأعراض كوفيد-19.\nيرجى عزل نفسك ومراجعة الطبيب."
                result_emoji = "🔴"
            elif answers[3] and answers[4] and answers[9]:
                result_text = "قد تكون حساسية موسمية\nأو زكام بسيط."
                result_emoji = "🟠"
            elif answers[0] and answers[7] and answers[8]:
                result_text = "الأعراض تشير لاحتمالية الإنفلونزا."
                result_emoji = "🟡"
            elif sum(answers) >= 5:
                result_text = "لديك أعراض متعددة.\nيفضل استشارة طبيب مختص."
                result_emoji = "🔵"
            else:
                result_text = "الأعراض خفيفة أو غير محددة.\nنتمنى لك السلامة."
                result_emoji = "🟢"
        
        return ft.Column(
            [
                ft.Text(result_emoji, size=60, text_align="center"),
                ft.Text("النتيجة النهائية", size=24, weight="bold", color="black"),
                ft.Divider(color="grey"),
                
                ft.Container(
                    content=ft.Text(result_text, size=20, text_align="center", color="black"),
                    padding=10
                ),
                
                ft.Container(height=20),
                
                ft.Button(
                    "عودة للرئيسية",
                    width=200, height=50,
                    on_click=restart_app,
                    style=ft.ButtonStyle(bgcolor="blue", color="white")
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10
        )

    # --- 7. المنطق ---
    def update_view(view_content):
        main_container.content = view_content
        main_container.update()

    def answer_clicked(answer):
        nonlocal current_index
        answers.append(answer)
        current_index += 1
        
        if current_index < len(questions):
            update_view(build_question_view())
        else:
            update_view(build_result_view())

    def restart_app(e):
        nonlocal current_index
        answers.clear()
        current_index = 0
        update_view(build_welcome_view())

    # --- 8. التشغيل ---
    page.add(main_container)
    update_view(build_welcome_view())

if __name__ == "__main__":
    # عدنا لاستخدام app لأنه الأضمن، وأخفينا التحذيرات
    ft.app(target=main)
