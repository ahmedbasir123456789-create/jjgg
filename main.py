import flet as ft

def main(page: ft.Page):
    # إعدادات الصفحة
    page.title = "Medical Checker"
    page.rtl = True
    page.scroll = "auto"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # متغيرات الحالة
    current_index = 0
    answers = []

    questions = [
        "هل حرارتك مرتفعة؟",
        "هل عندك سعال جاف؟",
        "هل تشعر بضيق تنفس؟",
        "هل عندك سيلان أنف؟",
        "هل حلقك يؤلمك؟"
    ]

    # العناصر الرسومية
    question_text = ft.Text(size=24, weight="bold", text_align="center")
    result_text = ft.Text(size=22, color="blue", text_align="center")
    
    # حاوية السؤال
    question_container = ft.Column(
        visible=False,
        controls=[
            ft.Text("أجب بـ نعم أو لا", size=16, color="grey"),
            ft.Container(height=20),
            question_text,
            ft.Container(height=20),
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.ElevatedButton(text="نعم", bgcolor="green", color="white", on_click=lambda e: next_question(True)),
                    ft.ElevatedButton(text="لا", bgcolor="red", color="white", on_click=lambda e: next_question(False)),
                ]
            )
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    # حاوية النتيجة
    result_container = ft
