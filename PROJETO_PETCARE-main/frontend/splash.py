import flet as ft
from partials.todos import obter_btn_style


def main(page: ft.Page):
    # Configurações da página
    page.title = "Splash"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = "#1B003A"  # Fundo roxo escuro para destaque neon

    # Configuração da imagem do logo em um container centralizado
    logo = ft.Container(
        content=ft.Image(
            src=r"..\_IMG_PET_CARE\675ac9488896439ba6af16592ae468dc.png",
            fit=ft.ImageFit.CONTAIN,
            width=400,
            height=400,
        ),
        width=400,
        height=400,
        border_radius=200,  # Circular
        clip_behavior=ft.ClipBehavior.HARD_EDGE,
        alignment=ft.alignment.center,
        padding=ft.padding.only(bottom=20)
    )

    # Título "PET CARE" com efeito neon
    title = ft.Text(
        "PET CARE",
        size=42,
        weight=ft.FontWeight.BOLD,
        color="#DDA0DD",  # Roxo neon claro
        text_align=ft.TextAlign.CENTER,
        style=ft.TextStyle(
            shadow=ft.BoxShadow(
                color="#DDA0DD",
                blur_radius=12,
                spread_radius=5,
                offset=ft.Offset(0, 0)
            )
        )
    )

    # Subtítulo com descrição e efeito de brilho
    subtitle = ft.Text(
        "Seu amigo em boas mãos",
        size=20,
        color="#BB86FC",  # Tom lilás neon para contraste
        text_align=ft.TextAlign.CENTER,
        style=ft.TextStyle(
            shadow=ft.BoxShadow(
                color="#BB86FC",
                blur_radius=8,
                spread_radius=3,
                offset=ft.Offset(0, 0)
            )
        ),
    )

    # Botão "Próximo" com estilo neon
    next_button = ft.ElevatedButton(
        content=ft.Row(
            controls=[
                ft.Text("Prosseguir", color="#FFFFFF"),
                ft.Icon(name="arrow_forward", color="#FFFFFF")
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=8
        ),
        on_click=lambda e: print("Prosseguir clicado"),
        width=160,
        height=45,
        style=ft.ButtonStyle(
            bgcolor="#6C63FF",  # Roxo neon mais claro
            shadow_color="#6C63FF",
            elevation=10,
            overlay_color=ft.colors.with_opacity(0.2, ft.colors.WHITE),
            shape=ft.RoundedRectangleBorder(radius=12),
        ),
    )

    # Layout principal com alinhamento e espaçamento uniforme
    splash_content = ft.Column(
        controls=[
            logo,
            title,
            subtitle,
            ft.Container(
                content=next_button,
                padding=ft.padding.only(top=30),
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=10,
    )

    # Adicionando o layout centralizado à página
    page.add(splash_content)


# Executando o app
ft.app(target=main, assets_dir='..\_IMG_PET_CARE')
