import flet as ft
from datetime import datetime


def main(page: ft.Page):
    # Configurações da página
    page.title = "Ficha - PET CARE"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.bgcolor = "#1A1A2E"  # Fundo escuro elegante

    # Logo em miniatura
    logo = ft.Container(
        content=ft.Image(
            src=r"..\_IMG_PET_CARE\675ac9488896439ba6af16592ae468dc.png",
            fit=ft.ImageFit.CONTAIN,
            width=40,
            height=40,
        ),
        width=40,
        height=40,
        border_radius=20,  # Circular
        clip_behavior=ft.ClipBehavior.HARD_EDGE,
    )

    # Título "FICHA"
    title = ft.Text(
        "FICHA",
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

    # Campo de exibição do ID do pet (chave estrangeira)
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

    # Campo para o nome do pet
    nome_pet_field = ft.TextField(
        label="Nome do Pet",
        text_align=ft.TextAlign.LEFT,
        color="#BB86FC",
        bgcolor="#1A1A2E",
        border_color="#BB86FC",
        border_radius=12,
        width=350
    )

    # Campo para a data da consulta
    consulta_date_field = ft.TextField(
        label="Data da Consulta",
        read_only=True,
        color="#BB86FC",
        bgcolor="#1A1A2E",
        border_color="#BB86FC",
        border_radius=12,
        width=350
    )

    # Função para atualizar a data da consulta ao escolher uma nova data
    def atualizar_data(e):
        if e.control.value:
            consulta_date_field.value = e.control.value.strftime("%d/%m/%Y")
            page.update()

    # Botão para abrir o seletor de data (DatePicker)
    date_picker_button = ft.IconButton(
        icon=ft.icons.CALENDAR_MONTH,
        icon_size=24,
        icon_color="#BB86FC",
        on_click=lambda e: page.open(
            ft.DatePicker(
                first_date=datetime(2020, 1, 1),
                last_date=datetime(2030, 12, 31),
                on_change=atualizar_data,
            )
        ),
    )

    # Campo para descrição dos medicamentos
    medicamentos_field = ft.TextField(
        label="Descrição dos Medicamentos",
        multiline=True,
        color="#BB86FC",
        bgcolor="#1A1A2E",
        border_color="#BB86FC",
        border_radius=12,
        width=350,
        height=150
    )

    # Função para ler QR Code
    def ler_qr_code(e):
        print("QR Code lido - Ação personalizada")

    # Botão para ler QR Code
    qr_button = ft.ElevatedButton(
        content=ft.Row(
            controls=[
                ft.Icon(name="qr_code", color="#FFFFFF"),
                ft.Text("Ler QR Code", color="#FFFFFF")
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=8
        ),
        on_click=ler_qr_code,
        width=180,
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
                # ID do Pet
                ft.Container(content=pet_id_display, alignment=ft.alignment.center, padding=ft.padding.only(bottom=15)),
                # Campos de texto
                nome_pet_field,
                ft.Row(
                    controls=[consulta_date_field, date_picker_button],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Container(content=medicamentos_field, padding=ft.padding.only(top=15, bottom=15)),
                # Botão de leitura de QR Code
                qr_button
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10
        )
    )


# Executando o app
ft.app(target=main, assets_dir='..\_IMG_PET_CARE')
