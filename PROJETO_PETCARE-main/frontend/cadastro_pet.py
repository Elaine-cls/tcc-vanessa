import flet as ft
from datetime import datetime


def main(page: ft.Page):
    # Configurações da página
    page.title = "Cadastro - PET"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START
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

    # Título "CADASTRO - PET"
    title = ft.Text(
        "CADASTRO - PET",
        size=24,
        weight=ft.FontWeight.BOLD,
        color="#BB86FC",
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
            ft.Container(content=title, padding=ft.padding.only(left=10))
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )

    # Campo para inserir ID do Pet (só leitura)
    pet_id_display = ft.TextField(
        value="ID do Pet: 123456",  # Exemplo de ID
        read_only=True,
        text_align=ft.TextAlign.CENTER,
        color="#BB86FC",
        bgcolor="#1A1A2E",
        border_color="#BB86FC",
        border_radius=12,
        width=250
    )

    # Campo para inserir ID do Dono (só leitura)
    dono_id_display = ft.TextField(
        value="ID do Dono: 654321",  # Exemplo de ID do dono
        read_only=True,
        text_align=ft.TextAlign.CENTER,
        color="#BB86FC",
        bgcolor="#1A1A2E",
        border_color="#BB86FC",
        border_radius=12,
        width=250
    )

    # Botão para adicionar foto do pet
    insert_photo_button = ft.ElevatedButton(
        content=ft.Row(
            controls=[
                ft.Icon(name="photo_camera", color=ft.colors.WHITE),
                ft.Text("Adicionar Foto do Pet", color=ft.colors.WHITE)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=8
        ),
        on_click=lambda e: print("Foto do Pet adicionada"),
        width=250,
        height=45,
        style=ft.ButtonStyle(
            bgcolor="#6C63FF",
            shadow_color="#6C63FF",
            elevation=10,
            overlay_color=ft.colors.with_opacity(0.2, ft.colors.WHITE),
            shape=ft.RoundedRectangleBorder(radius=12),
        ),
    )

    # Campo para inserir o nome do pet
    nome_pet_field = ft.TextField(
        label="Nome do Pet",
        text_align=ft.TextAlign.LEFT,
        color="#BB86FC",
        bgcolor="#1A1A2E",
        border_color="#BB86FC",
        border_radius=12,
        width=350
    )

    # Campo para inserir a raça do pet
    raca_pet_field = ft.TextField(
        label="Raça do Pet",
        text_align=ft.TextAlign.LEFT,
        color="#BB86FC",
        bgcolor="#1A1A2E",
        border_color="#BB86FC",
        border_radius=12,
        width=350
    )

    # Campo para a data de nascimento do pet
    nascimento_field = ft.TextField(
        label="Data de Nascimento",
        read_only=True,
        color="#BB86FC",
        bgcolor="#1A1A2E",
        border_color="#BB86FC",
        border_radius=12,
        width=350
    )

    # Campos de visualização da idade do pet
    idade_pet_display = ft.TextField(
        label="Idade do Pet (em anos)",
        read_only=True,
        color="#BB86FC",
        bgcolor="#1A1A2E",
        border_color="#BB86FC",
        border_radius=12,
        width=170
    )

    idade_humana_display = ft.TextField(
        label="Idade em Anos Humanos",
        read_only=True,
        color="#BB86FC",
        bgcolor="#1A1A2E",
        border_color="#BB86FC",
        border_radius=12,
        width=170
    )

    # Função para calcular idade e atualizar campos
    def atualizar_idade(data_nascimento):
        if data_nascimento:
            hoje = datetime.now()
            idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))
            idade_pet_display.value = str(idade)
            idade_humana_display.value = str(idade * 7)
            page.update()

    # Botão para abrir o DatePicker
    date_picker_button = ft.IconButton(
        icon=ft.icons.CALENDAR_MONTH,
        icon_size=24,
        icon_color="#BB86FC",
        on_click=lambda e: page.open(
            ft.DatePicker(
                first_date=datetime(2000, 1, 1),
                last_date=datetime(2030, 12, 31),
                on_change=lambda e: (
                    setattr(nascimento_field, "value", e.control.value.strftime("%d/%m/%Y")),
                    atualizar_idade(e.control.value)
                ),
            )
        ),
    )

    # Campo para altura do pet
    altura_field = ft.TextField(
        label="Altura (em metros)",
        text_align=ft.TextAlign.LEFT,
        color="#BB86FC",
        bgcolor="#1A1A2E",
        border_color="#BB86FC",
        border_radius=12,
        width=350
    )

    # Campo para peso do pet
    peso_field = ft.TextField(
        label="Peso (em kg)",
        text_align=ft.TextAlign.LEFT,
        color="#BB86FC",
        bgcolor="#1A1A2E",
        border_color="#BB86FC",
        border_radius=12,
        width=350
    )

    # Dropdown para escolher o tipo do pet
    tipo_pet_dropdown = ft.Dropdown(
        label="Tipo do Pet",
        options=[
            ft.dropdown.Option("Cachorro"),
            ft.dropdown.Option("Gato"),
            ft.dropdown.Option("Pássaro"),
            ft.dropdown.Option("Coelho"),
            ft.dropdown.Option("Outros"),
        ],
        width=350,
        color="#BB86FC",
        bgcolor="#1A1A2E",
        border_color="#BB86FC",
    )

    # Campo de observações sobre o pet
    observacoes_field = ft.TextField(
        label="Observações",
        multiline=True,
        color="#BB86FC",
        bgcolor="#1A1A2E",
        border_color="#BB86FC",
        border_radius=12,
        width=350,
        height=150
    )

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
                # IDs do Pet e do Dono e botão de foto
                ft.Container(content=pet_id_display, alignment=ft.alignment.center, padding=ft.padding.only(bottom=5)),
                ft.Container(content=dono_id_display, alignment=ft.alignment.center, padding=ft.padding.only(bottom=15)),
                insert_photo_button,
                # Campos de texto
                nome_pet_field,
                raca_pet_field,
                # Data de nascimento e cálculo da idade
                ft.Row(
                    controls=[nascimento_field, date_picker_button],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    controls=[idade_pet_display, idade_humana_display],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=10,
                ),
                # Campos para altura, peso e tipo do pet
                altura_field,
                peso_field,
                tipo_pet_dropdown,
                # Campo de observações
                observacoes_field,
                ft.Row(
                    controls=[cancel_button, save_button],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=20
                ),
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10
        )
    )


# Executando o app
ft.app(target=main, assets_dir='..\_IMG_PET_CARE')
