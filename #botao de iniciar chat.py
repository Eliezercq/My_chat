import flet as ft

def main(pagina):
    texto = ft.Text("EliezerZapp") 

    nome_usuario = ft.TextField(Label="Escreva seu nome")


    def entrar_popup(evento):
      
        popup.open = False
       
        pagina.update()

    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title=ft.Text("Bem vindoao EliezerZapp"),
        content=nome_usuario,
        actions=[ft.ElevatedButton("Entrar", on_click=entrar_popup)],
        )

    def entrar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click=entrar_chat)

    pagina.add(texto)
    pagina.add(botao_iniciar)
    
ft.app(target=main) 
