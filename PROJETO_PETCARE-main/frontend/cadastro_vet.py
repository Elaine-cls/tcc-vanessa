import flet as ft


def main(page: ft.Page):
    # Configurações da página
    page.title = "Cadastro - Veterinário"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.bgcolor = "#1A1A2E"  # Fundo escuro elegante

    # Imagem circular do cabeçalho com borda neon
    logo = ft.Container(
        content=ft.Image(
            src=r"..\_IMG_PET_CARE\675ac9488896439ba6af16592ae468dc.png",
            fit=ft.ImageFit.COVER,
            width=80,
            height=80,
        ),
        width=80,
        height=80,
        border_radius=40,
        border=ft.border.all(3, color="#BB86FC"),
        clip_behavior=ft.ClipBehavior.HARD_EDGE,
    )

    # Título "CADASTRO - VETERINÁRIO" com efeito neon e sombra
    title = ft.Text(
        "CADASTRO - VETERINÁRIO",
        size=30,
        weight=ft.FontWeight.BOLD,
        color="#BB86FC",
        text_align=ft.TextAlign.LEFT,
        style=ft.TextStyle(
            shadow=ft.BoxShadow(
                color="#BB86FC",
                blur_radius=15,
                spread_radius=5,
                offset=ft.Offset(0, 0),
            )
        ),
    )

    # Cabeçalho com imagem e título alinhados
    header = ft.Row(
        controls=[
            logo,
            ft.Container(content=title, padding=ft.padding.only(left=15))
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )

    # Botão para enviar foto do veterinário
    insert_photo_button = ft.ElevatedButton(
        content=ft.Row(
            controls=[
                ft.Icon(name="photo_camera", color=ft.colors.WHITE),
                ft.Text("Inserir Foto", color=ft.colors.WHITE)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=8
        ),
        on_click=lambda e: print("Foto do Veterinário inserida"),
        width=250,
        height=50,
        style=ft.ButtonStyle(
            bgcolor="#6C63FF",
            shadow_color="#6C63FF",
            elevation=12,
            overlay_color=ft.colors.with_opacity(0.2, ft.colors.WHITE),
            shape=ft.RoundedRectangleBorder(radius=12),
        ),
    )

    # Campo para exibir o ID do veterinário (PK VET)
    vet_id_display = ft.TextField(
        value="ID do Veterinário: 987654",  # Exemplo de ID
        read_only=True,
        text_align=ft.TextAlign.CENTER,
        color="#BB86FC",
        bgcolor="#1A1A2E",
        border_color="#BB86FC",
        border_radius=12,
        width=250
    )

    # Campos de texto para Nome, CRMV, CNPJ e Especialização
    def create_text_field(label):
        return ft.TextField(
            label=label,
            text_align=ft.TextAlign.LEFT,
            color="#BB86FC",
            bgcolor="#1A1A2E",
            border_color="#BB86FC",
            border_radius=12,
            width=350
        )

    nome_field = create_text_field("Nome do Veterinário")
    crmv_field = create_text_field("CRMV do Veterinário")
    cnpj_field = create_text_field("CNPJ do Veterinário")
    especializacao_field = create_text_field("Especialização do Veterinário")

    # Botões de "Salvar" e "Cancelar" com ícones
    cancel_button = ft.ElevatedButton(
        content=ft.Row(
            controls=[
                ft.Icon(name="cancel", color="#FFFFFF"),
                ft.Text("Cancelar", color="#FFFFFF")
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=8
        ),
        on_click=lambda e: print("Cadastro cancelado"),
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

    save_button = ft.ElevatedButton(
        content=ft.Row(
            controls=[
                ft.Text("Salvar", color="#FFFFFF"),
                ft.Icon(name="save", color="#FFFFFF")
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=8
        ),
        on_click=lambda e: print("Cadastro salvo"),
        width=160,
        height=45,
        style=ft.ButtonStyle(
            bgcolor="#6C63FF",
            shadow_color="#6C63FF",
            elevation=10,
            overlay_color=ft.colors.with_opacity(0.2, ft.colors.WHITE),
            shape=ft.RoundedRectangleBorder(radius=12),
        ),
    )

    # Layout principal
    page.add(
        ft.Column(
            controls=[
                # Cabeçalho
                ft.Container(
                    content=header,
                    alignment=ft.alignment.center,
                    padding=ft.padding.all(20)
                ),
                # Inserir Foto e ID do Veterinário
                ft.Container(
                    content=insert_photo_button,
                    alignment=ft.alignment.center,
                    padding=ft.padding.only(top=20, bottom=10)
                ),
                ft.Container(
                    content=vet_id_display,
                    alignment=ft.alignment.center,
                    padding=ft.padding.only(bottom=15)
                ),
                # Campos de texto
                ft.Container(content=nome_field, padding=ft.padding.only(bottom=15)),
                ft.Container(content=crmv_field, padding=ft.padding.only(bottom=15)),
                ft.Container(content=cnpj_field, padding=ft.padding.only(bottom=15)),
                ft.Container(content=especializacao_field, padding=ft.padding.only(bottom=20)),
                # Botões de ação
                ft.Row(
                    controls=[cancel_button, save_button],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=20
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10
        )
    )


# Executando o app
ft.app(target=main, assets_dir='..\_IMG_PET_CARE')
