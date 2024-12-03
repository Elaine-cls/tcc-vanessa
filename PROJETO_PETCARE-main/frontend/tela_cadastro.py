import flet as ft
from partials.todos import obter_btn_style, obter_prev_button


def main(page: ft.Page):
    # Configurações da página
    page.title = "Cadastro"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = "#1B003A"  # Fundo roxo escuro para destaque neon

    # Logo em miniatura com estilo neon
    logo = ft.Container(
        content=ft.Image(
            src=r"../_IMG_PET_CARE/675ac9488896439ba6af16592ae468dc.png",
            fit=ft.ImageFit.CONTAIN,
            width=50,
            height=50,
        ),
        width=50,
        height=50,
        border_radius=25,  # Circular
        clip_behavior=ft.ClipBehavior.HARD_EDGE,
        alignment=ft.alignment.center
    )

    # Título "Cadastros" com efeito neon
    title = ft.Text(
        "Cadastros",
        size=36,
        weight=ft.FontWeight.BOLD,
        color="#DDA0DD",  # Roxo neon claro
        text_align=ft.TextAlign.CENTER,
        style=ft.TextStyle(
            shadow=ft.BoxShadow(
                color="#DDA0DD",
                blur_radius=10,
                spread_radius=5,
                offset=ft.Offset(0, 0)
            )
        )
    )

    # Subtítulo com tom lilás neon
    subtitle = ft.Text(
        "Nesta tela você escolhe o seu tipo de perfil",
        size=18,
        color="#BB86FC",
        text_align=ft.TextAlign.CENTER,
        style=ft.TextStyle(
            shadow=ft.BoxShadow(
                color="#BB86FC",
                blur_radius=6,
                spread_radius=3,
                offset=ft.Offset(0, 0)
            )
        )
    )

    # Botão "Cadastrar Usuário" com estilo neon
    sign_up_user = ft.ElevatedButton(
        text="Cadastrar Usuário",
        width=200,
        height=50,
        on_click=lambda e: print("Cadastrado Usuário"),
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=12),
            bgcolor="#8A2BE2",
            color=ft.colors.WHITE,
            overlay_color=ft.colors.with_opacity(0.1, ft.colors.WHITE),
            shadow_color="#8A2BE2",
            elevation=10,
        ),
    )

    # Botão "Cadastrar Veterinário" com estilo neon
    sign_up_vet = ft.ElevatedButton(
        text="Cadastrar Veterinário",
        width=200,
        height=50,
        on_click=lambda e: print("Cadastrado Veterinário"),
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=12),
            bgcolor="#8A2BE2",
            color=ft.colors.WHITE,
            overlay_color=ft.colors.with_opacity(0.1, ft.colors.WHITE),
            shadow_color="#8A2BE2",
            elevation=10,
        ),
    )

    # Fila para CPF e botão de cadastro de usuário
    row_signup_user = ft.Row(
        [
            ft.Text('CPF:', color="#BB86FC", size=16, weight=ft.FontWeight.BOLD),
            sign_up_user
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10,
    )

    # Fila para CRMV e botão de cadastro de veterinário
    row_signup_vet = ft.Row(
        [
            ft.Text('CRMV:', color="#BB86FC", size=16, weight=ft.FontWeight.BOLD),
            sign_up_vet
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10,
    )

    # Botão "Anterior" com efeito neon
    back_button = ft.ElevatedButton(
        content=ft.Row(
            controls=[
                ft.Icon(name="arrow_back", color="#FFFFFF"),
                ft.Text("Voltar", color="#FFFFFF")
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=8
        ),
        on_click=lambda e: print("Voltar clicado"),
        width=160,
        height=45,
        style=ft.ButtonStyle(
            bgcolor="#FF8A65",  # Laranja neon suave
            shadow_color="#FF8A65",
            elevation=10,
            overlay_color=ft.colors.with_opacity(0.2, ft.colors.WHITE),
            shape=ft.RoundedRectangleBorder(radius=12),
        ),
    )

    # Layout principal com alinhamento e espaçamento uniforme
    page.add(
        ft.Column(
            [
                # Cabeçalho com logo e título
                ft.Row(
                    controls=[
                        logo,
                        title
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                # Subtítulo
                ft.Container(content=subtitle, alignment=ft.alignment.center, padding=ft.padding.only(bottom=20)),
                # Linhas para cadastro de usuário e veterinário
                row_signup_user,
                row_signup_vet,
                # Botão "Voltar"
                ft.Container(content=back_button, padding=ft.padding.only(top=30))
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15,  # Espaçamento uniforme entre os elementos
        )
    )


# Executando o app
ft.app(target=main, assets_dir='assets')
