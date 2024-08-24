import flet as ft


def main(page: ft.Page):
    page.fonts = {
        "BebasNeue": "/fonts/Kanit-Bold.ttf"
    }

    page.theme = ft.Theme(font_family="BebasNeue")

    answer_1 = ft.ElevatedButton(text="Caravaggio")
    answer_2 = ft.ElevatedButton(text="Picasso")
    answer_3 = ft.ElevatedButton(text="Da Vinci")
    answer_4 = ft.ElevatedButton(text="Van Gogh")

    def clear_page(e):
        page.clean()
        page.update()

    def app_start():
        img = ft.Image(
            src="/images/logo_low_rez.png",
            width=200,
            height=200,
            fit=ft.ImageFit.CONTAIN,
        )
        page.add(
            img,
            ft.ElevatedButton(text="Enter", on_click=question_model),
        )

    def correct_answer(e):
        answer_3.bgcolor = ft.colors.GREEN
        answer_3.color = ft.colors.WHITE

        audio_correct = ft.Audio(
            src="/sfx/correct.mp3", autoplay=True,
        )
        page.overlay.append(audio_correct)
        page.update()

    def wrong_answer_1(e):
        answer_1.bgcolor = ft.colors.RED
        answer_1.color = ft.colors.WHITE
        answer_3.bgcolor = ft.colors.GREEN
        answer_3.color = ft.colors.WHITE

        audio_wrong = ft.Audio(
            src="/sfx/wrong.mp3", autoplay=True,
        )
        page.overlay.append(audio_wrong)
        page.update()

    def wrong_answer_2(e):
        answer_2.bgcolor = ft.colors.RED
        answer_2.color = ft.colors.WHITE
        answer_3.bgcolor = ft.colors.GREEN
        answer_3.color = ft.colors.WHITE

        audio_wrong = ft.Audio(
            src="/sfx/wrong.mp3", autoplay=True,
        )
        page.overlay.append(audio_wrong)
        page.update()

    def wrong_answer_4(e):
        answer_4.bgcolor = ft.colors.RED
        answer_4.color = ft.colors.WHITE
        answer_3.bgcolor = ft.colors.GREEN
        answer_3.color = ft.colors.WHITE

        audio_wrong = ft.Audio(
            src="/sfx/wrong.mp3", autoplay=True,
        )
        page.overlay.append(audio_wrong)
        page.update()

    def question_model(e):
        clear_page(e)
        question = ft.Text(value="Who painted this?")
        question_picture = ft.Image(src="/images/mona_lisa.jpg",
                                    width=200,
                                    )

        answer_1.on_click = wrong_answer_1
        answer_2.on_click = wrong_answer_2
        answer_3.on_click = correct_answer
        answer_4.on_click = wrong_answer_4

        page.add(
            question,
            question_picture,
            answer_1,
            answer_2,
            answer_3,
            answer_4,
        )

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    app_start()


ft.app(
    target=main,
    assets_dir="assets",
    view=None,
    port=8000,
    host="0.0.0.0"
)
