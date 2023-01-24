import flet as ft
import os


def main(page: ft.Page):
    page.title = "Control de Matriculas"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    matriculas = ft.DataTable(
            width=700,
            bgcolor="Black",
            border=ft.border.all(2, "red"),
            border_radius=10,
            vertical_lines=ft.border.BorderSide(3, "blue"),
            horizontal_lines=ft.border.BorderSide(1, "green"),
            sort_column_index=0,
            sort_ascending=True,
            heading_row_color=ft.colors.BLACK12,
            heading_row_height=100, 
            columns=[  
            ft.DataColumn(
                ft.Text("Matriculas Introducidas")
            )
            ],
            rows=[
                    
            ]
            
    )
    intro = ft.TextField(value="Introduce la matricula",text_align="center",color="white")
    
 
    def añadirMatricula(input):
        matriculas.rows.append(ft.DataRow(
            cells=[(ft.DataCell(ft.Text(f"{input_matricula}")))
                   ]
        ))  
        page.update

    input_matricula = ft.TextField(label="Matricula a añadir", text_align="right", width=100)
    btn_aceptar = ft.TextButton(text="Añadir matricula",on_click=añadirMatricula(input_matricula))
    
    
    page.add( 
        ft.Row([intro],alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([input_matricula],alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([btn_aceptar],alignment=ft.MainAxisAlignment.CENTER,),
        ft.Row([matriculas],alignment=ft.MainAxisAlignment.CENTER),
       
    )

ft.app(target=main)