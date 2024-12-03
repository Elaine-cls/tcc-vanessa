import datetime
import flet as ft


def main(page: ft.Page):
    # Configurações da página
    page.title = "Cadastro - Pet"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.bgcolor = "#0D0028"  # Fundo escuro para destacar o tema neon

    # Imagem circular do cabeçalho
    logo = ft.Container(
        content=ft.Image(
            src=r"..\_IMG_PET_CARE\675ac9488896439ba6af16592ae468dc.png",
            fit=ft.ImageFit.COVER,
            width=60,
            height=60,
        ),
        width=60,
        height=60,
        border_radius=30,  # Tornando a imagem circular
        clip_behavior=ft.ClipBehavior.HARD_EDGE,
    )

    # Título "CADASTRO - PET" com efeito neon
    title = ft.Text(
        "CADASTRO - PET",
        size=24,
        weight=ft.FontWeight.BOLD,
        color="#E0BBE4",  # Roxo neon claro
        text_align=ft.TextAlign.LEFT,
        style=ft.TextStyle(shadow=ft.BoxShadow(
            color="#E0BBE4",
            blur_radius=10,
            offset=ft.Offset(0, 0)
        ),
        )
    )

    # Cabeçalho com imagem e título alinhados
    header = ft.Row(
        controls=[
            logo,
            ft.Container(content=title, padding=ft.padding.only(left=10))  # Espaçamento entre imagem e título
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=0
    )

    # Botão para inserir foto do pet com ícone de câmera
    insert_photo_button = ft.ElevatedButton(
        content=ft.Row(
            controls=[
                ft.Icon(name="photo_camera", color=ft.colors.WHITE),  # Ícone de câmera
                ft.Text("Inserir Foto do Pet", color=ft.colors.WHITE)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=5
        ),
        on_click=lambda e: print("Foto do Pet inserida"),
        width=200,
        height=40,
        style=ft.ButtonStyle(
            bgcolor="#8A2BE2",  # Roxo neon
            shadow_color="#8A2BE2",
            elevation=8,
            overlay_color=ft.colors.with_opacity(0.1, ft.colors.WHITE),
            shape=ft.RoundedRectangleBorder(radius=10),
        ),
    )

    # Campos desabilitados para exibir ID PET e ID DONO
    id_pet_field = ft.TextField(
        value="ID PET: 123456",  # Exemplo de ID
        read_only=True,
        text_align=ft.TextAlign.CENTER,
        color="#BB86FC",  # Lilás neon para contraste
        bgcolor="#0D0028",
        border_color="#BB86FC",
        border_radius=10,
        width=200
    )

    id_dono_field = ft.TextField(
        value="ID DONO: 654321",  # Exemplo de ID
        read_only=True,
        text_align=ft.TextAlign.CENTER,
        color="#BB86FC",  # Lilás neon para contraste
        bgcolor="#0D0028",
        border_color="#BB86FC",
        border_radius=10,
        width=200
    )

    # Campo para escrever o nome do pet
    nome_pet_field = ft.TextField(
        label="Nome do Pet",
        text_align=ft.TextAlign.LEFT,
        color="#BB86FC",
        bgcolor="#0D0028",
        border_color="#BB86FC",
        border_radius=10,
        width=300
    )

    # Campo para escrever a raça do pet
    raca_pet_field = ft.TextField(
        label="Raça",
        text_align=ft.TextAlign.LEFT,
        color="#BB86FC",
        bgcolor="#0D0028",
        border_color="#BB86FC",
        border_radius=10,
        width=300
    )

    # Campo para escolher a data de nascimento do pet
    data_nascimento_field = ft.TextField(
        label="Data de Nascimento",
        read_only=True,
        color="#BB86FC",
        bgcolor="#0D0028",
        border_color="#BB86FC",
        border_radius=10,
        width=300
    )

    # Função para atualizar a data no campo de data de nascimento
    def handle_change(e):
        if e.control.value:
            data_nascimento_field.value = e.control.value.strftime("%d/%m/%Y")
            page.update()

    def handle_dismissal(e):
        print("DatePicker dismissed")

    # Botão para abrir o DatePicker
    data_nascimento_button = ft.IconButton(
        icon=ft.icons.CALENDAR_MONTH,
        icon_size=24,
        icon_color="#BB86FC",
        on_click=lambda e: page.open(
            ft.DatePicker(
                first_date=datetime.datetime(year=1, month=1, day=1),
                last_date=datetime.datetime(year=9999, month=12, day=31),
                on_change=handle_change,
                on_dismiss=handle_dismissal,
            )
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
                # Inserir Foto e IDs do PET e do DONO
                ft.Container(
                    content=insert_photo_button,
                    alignment=ft.alignment.center,
                    padding=ft.padding.only(top=20, bottom=10)
                ),
                ft.Container(
                    content=id_pet_field,
                    alignment=ft.alignment.center,
                    padding=ft.padding.only(bottom=10)
                ),
                ft.Container(
                    content=id_dono_field,
                    alignment=ft.alignment.center,
                    padding=ft.padding.only(bottom=10)
                ),
                # Campos de cadastro do pet
                ft.Container(content=nome_pet_field, padding=ft.padding.only(bottom=10)),
                ft.Container(content=raca_pet_field, padding=ft.padding.only(bottom=10)),
                ft.Row(
                    controls=[data_nascimento_field, data_nascimento_button],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )


# Executando o app
ft.app(target=main, assets_dir=r'..\_IMG_PET_CARE')
