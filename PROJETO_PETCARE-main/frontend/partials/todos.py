import flet as ft


# Estilo padrão para botões
def obter_btn_style():
    """Define e retorna o estilo padrão para botões."""
    return ft.ButtonStyle(
        color={ft.ControlState.DEFAULT: ft.colors.WHITE, ft.ControlState.HOVERED: ft.colors.PURPLE},
        bgcolor={ft.ControlState.DEFAULT: ft.colors.PURPLE, ft.ControlState.HOVERED: ft.colors.WHITE},
        side={ft.ControlState.DEFAULT: ft.BorderSide(1, ft.colors.WHITE30),
              ft.ControlState.HOVERED: ft.BorderSide(1, ft.colors.PURPLE_300)},
        shape=ft.ContinuousRectangleBorder(radius=15)
    )


# Botão "Voltar"
def criar_voltar_btn():
    """Cria e retorna o botão 'Voltar'."""
    return ft.ElevatedButton(
        content=ft.Row(
            [
                ft.Icon(name=ft.icons.ARROW_BACK),
                ft.Text('Voltar')
            ], spacing=100, alignment=ft.MainAxisAlignment.CENTER
        ),
        style=obter_btn_style(),
        width=200,
    )


# Botão "Prosseguir" com texto e ícone alinhados
def criar_prox_btn():
    """Cria e retorna o botão 'Prosseguir' com texto e ícone."""
    return ft.ElevatedButton(
        content=ft.Row(
            controls=[
                ft.Text("Prosseguir"),
                ft.Icon(name=ft.icons.ARROW_FORWARD)
            ], spacing=75
        ),
        style=obter_btn_style(),
        width=200,
    )


# Linha de botões "Voltar" e "Prosseguir"
def criar_alt_btns():
    """Cria e retorna a linha com os botões 'Voltar' e 'Prosseguir'."""
    voltar_btn = criar_voltar_btn()
    prox_btn = criar_prox_btn()

    return ft.Row(
        controls=[voltar_btn, prox_btn],
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )


# Botão de envio de foto
def criar_botao_foto():
    """Cria e retorna o botão para enviar foto."""
    cor_foto = {ft.ControlState.DEFAULT: ft.colors.WHITE, ft.ControlState.HOVERED: ft.colors.PURPLE}
    foto_estilo = ft.ButtonStyle(
        color=obter_btn_style().color,
        bgcolor=obter_btn_style().bgcolor,
        side=obter_btn_style().side,
        icon_size=100,
        shape=obter_btn_style().shape,
        animation_duration=300
    )

    icone_foto = ft.Icon(ft.icons.ADD_A_PHOTO, size=90, color=cor_foto)
    texto_foto = ft.Text("Foto", color=cor_foto)

    return ft.ElevatedButton(
        content=ft.Column(
            controls=[icone_foto, texto_foto],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=-5
        ),
        style=foto_estilo,
        on_click=lambda e: print("Botão 'Foto' clicado!")
    )


def obter_prev_button(p=88):
    prev_button = ft.ElevatedButton(icon=ft.icons.ARROW_BACK, style=obter_btn_style(), text='Voltar')

    prev = ft.Container(prev_button, padding=ft.padding.only(right=p))
    return prev
