import flet as ft


def main(page: ft.Page):
    # Configurações da página
    page.title = "Login - PET CARE"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = "#1A1A2E"  # Fundo escuro elegante

    # Logo em larga escala
    logo = ft.Container(
        content=ft.Image(
            src=r"..\_IMG_PET_CARE\675ac9488896439ba6af16592ae468dc.png",
            fit=ft.ImageFit.CONTAIN,
            width=300,
            height=300
        ),
        width=300,
        height=300,
        border_radius=75,  # Circular
        clip_behavior=ft.ClipBehavior.HARD_EDGE
    )

    # Título "PET CARE" com efeito neon
    title = ft.Text(
        "PET CARE",
        size=40,
        weight=ft.FontWeight.BOLD,
        color="#BB86FC",  # Roxo neon
        text_align=ft.TextAlign.CENTER,
        style=ft.TextStyle(
            shadow=ft.BoxShadow(
                color="#BB86FC",
                blur_radius=15,
                spread_radius=5,
                offset=ft.Offset(0, 0)
            )
        ),
    )

    # Campo de texto para inserir E-mail
    email_field = ft.TextField(
        label="E-mail",
        text_align=ft.TextAlign.LEFT,
        color="#BB86FC",
        bgcolor="#1A1A2E",
        border_color="#BB86FC",
        border_radius=12,
        width=350
    )

    # Campo de texto para inserir Senha
    password_field = ft.TextField(
        label="Senha",
        password=True,  # Campo de senha
        text_align=ft.TextAlign.LEFT,
        color="#BB86FC",
        bgcolor="#1A1A2E",
        border_color="#BB86FC",
        border_radius=12,
        width=350
    )

    # Função para exibir a mensagem de recuperação de senha
    def recuperar_senha(e):
        print("Recuperação de senha acionada")

    # Link para recuperar senha
    recuperar_senha_link = ft.ElevatedButton(
        text="Esqueci minha senha",
        on_click=recuperar_senha,
        style=ft.ButtonStyle(
            color="#6C63FF",
            bgcolor='#00000000',
            text_style=ft.TextStyle(
                decoration=ft.TextDecoration.UNDERLINE
            )
        ),
    )

    # Função para realizar o login
    def realizar_login(e):
        print("Tentativa de login com E-mail:", email_field.value)

    # Botão de login
    login_button = ft.ElevatedButton(
        content=ft.Row(
            controls=[
                ft.Text("Entrar", color="#FFFFFF"),
                ft.Icon(name="login", color="#FFFFFF")
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=8
        ),
        on_click=realizar_login,
        width=180,
        height=45,
        style=ft.ButtonStyle(
            bgcolor="#6C63FF",
            shadow_color="#6C63FF",
            elevation=10,
            overlay_color=ft.colors.with_opacity(0.2, ft.colors.WHITE),
            shape=ft.RoundedRectangleBorder(radius=12)
        ),
    )

    # Layout principal
    page.add(
        ft.Column(
            controls=[
                logo,
                ft.Container(content=title, padding=ft.padding.only(top=20, bottom=40)),
                email_field,
                ft.Container(content=password_field, padding=ft.padding.only(top=10, bottom=5)),
                recuperar_senha_link,
                ft.Container(content=login_button, padding=ft.padding.only(top=20))
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10
        )
    )


# Executando o app
ft.app(target=main, assets_dir='..\_IMG_PET_CARE')
