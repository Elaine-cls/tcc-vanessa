import flet as ft


def main(page: ft.Page):
    # Configurações da página
    page.title = "Histórico - PET CARE"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = "#1A1A2E"  # Fundo escuro elegante
    page.scroll = 'adaptive'

    # Logo em miniatura
    logo = ft.Container(
        content=ft.Image(
            src=r"675ac9488896439ba6af16592ae468dc.png",
            fit=ft.ImageFit.CONTAIN,
            width=40,
            height=40,
        ),
        width=40,
        height=40,
        border_radius=20,  # Circular
        clip_behavior=ft.ClipBehavior.HARD_EDGE,
    )

    # Título "HISTÓRICO"
    title = ft.Text(
        "HISTÓRICO",
        size=24,
        weight=ft.FontWeight.BOLD,
        color="#BB86FC",  # Roxo neon
        text_align=ft.TextAlign.LEFT,
        style=ft.TextStyle(
            shadow=ft.BoxShadow(
                color="#BB86FC",
                blur_radius=8,
                spread_radius=3,
                offset=ft.Offset(0, 0),
            )
        ),
    )

    # Cabeçalho com logo e título
    header = ft.Row(
        controls=[
            logo,
            ft.Container(content=title, padding=ft.padding.only(left=10))  # Espaço entre logo e título
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )

    # Campo para inserção do ID do pet
    pet_id_field = ft.TextField(
        label="ID do Pet",
        text_align=ft.TextAlign.CENTER,
        color="#BB86FC",
        bgcolor="#1A1A2E",
        border_color="#BB86FC",
        border_radius=12,
        width=250
    )

    # Campo para visualização do nome do pet
    nome_pet_display = ft.TextField(
        label="Nome do Pet",
        value="Exemplo: Rex",  # Exemplo de nome do pet
        read_only=True,
        text_align=ft.TextAlign.CENTER,
        color="#BB86FC",
        bgcolor="#1A1A2E",
        border_color="#BB86FC",
        border_radius=12,
        width=350
    )

    # Lista de datas de atendimento
    datas_atendimento = ft.ListView(
        controls=[
            ft.Text("20/01/2023", text_align=ft.TextAlign.CENTER),
            ft.Text("15/03/2023", text_align=ft.TextAlign.CENTER),
            ft.Text("10/05/2023", text_align=ft.TextAlign.CENTER),
        ],
        spacing=10,
        padding=ft.padding.all(10),
        expand=True,
        height=100,
    )

    # Lista de vacinas
    vacinas_list = ft.ListView(
        controls=[
            ft.Text("Vacina Anti-rábica - 20/01/2023", text_align=ft.TextAlign.CENTER),
            ft.Text("Vacina Polivalente - 15/03/2023", text_align=ft.TextAlign.CENTER),
        ],
        spacing=10,
        padding=ft.padding.all(10),
        expand=True,
        height=100
    )

    # Lista de consultas
    consultas_list = ft.ListView(
        controls=[
            ft.Text("Consulta de rotina - 10/05/2023", text_align=ft.TextAlign.CENTER),
            ft.Text("Consulta com especialista - 20/06/2023", text_align=ft.TextAlign.CENTER),
        ],
        spacing=10,
        padding=ft.padding.all(10),
        expand=True,
        height=100,
    )

    # Lista de cuidados do pet
    cuidados_list = ft.ListView(
        controls=[
            ft.Text("Banho e Tosa - 05/04/2023", text_align=ft.TextAlign.CENTER),
            ft.Text("Higienização dos dentes - 25/07/2023", text_align=ft.TextAlign.CENTER),
        ],
        spacing=10,
        padding=ft.padding.all(10),
        expand=True,
        height=100
    )

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
                # ID do Pet e Nome do Pet
                ft.Container(content=pet_id_field, alignment=ft.alignment.center, padding=ft.padding.only(bottom=15)),
                ft.Container(content=nome_pet_display, alignment=ft.alignment.center, padding=ft.padding.only(bottom=20)),
                # Histórico de datas de atendimento
                ft.Text("Datas de Atendimento:", color="#BB86FC", size=16),
                datas_atendimento,
                # Histórico de vacinas
                ft.Text("Vacinas:", color="#BB86FC", size=16),
                ft.Container(content=vacinas_list, alignment=ft.alignment.center),
                # Histórico de consultas
                ft.Text("Consultas:", color="#BB86FC", size=16),
                ft.Container(content=consultas_list, alignment=ft.alignment.center),
                # Histórico de cuidados
                ft.Text("Cuidados:", color="#BB86FC", size=16),
                ft.Container(content=cuidados_list, alignment=ft.alignment.center),
                back_button
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10
        )
    )


# Executando o app
ft.app(target=main, assets_dir='..\_IMG_PET_CARE')
