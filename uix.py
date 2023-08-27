import flet as ft
import datetime
import pdf
import pandas as pd
xls_path =""
width_check =200

list_institucion = ["BBRAUN MEDICAL PERU","Hospital Alberto Sabogal","Hospital del Niño - Breña"]

check_list =[
    "Mantenimiento preventivo",
    "Mantenimiento Correctivo",
    "Alarma de aire",
    "Cable Roto",
    "No Enciende",
    "Soporte de Jeringa Roto",
    "Alarma de Jeringa",
    "Garras trabadas",
    "No se Visualiza",
    "Teclado Defectuoso",
    "Alarma de Presion Alta",
    "Linea Trabada",
    "Pinza de Soporte Rota",
    "Brazo no cierra",
    "No Carga Bateria",
    "Puerta Rota",
    "Autotest",
    "Prueba de infusion",
    "Reparacion",
    "Prueba de Sensores",
    "Calibracion",
    "Prueba de Alarmas",
    "Configuracion",
    "Prueba de Teclado",
    "Si_test_exact",
    "No_test_exact",
    "Si_test_aire",
    "No_test_aire",
    "Si_test_pressalt",
    "No_test_pressalt",
    "Si_test_antf",
    "No_test_antf",
    "Si_cargabat",
    "No_cargabat",
    "Alojamiento Inferior",
    "Cable AC",
    "Pinsa de Soporte",
    "Soporte de Jeringa",
    "Alojamiento inferior",
    "Clamp de Seguridad",
    "Sensor de Aire",
    "Unidad Operativa",
    "Altavos",
    "Display LCD",
    "Sensor de Presion",
    "Ninguno",
    "Bateria",
    "Fuente Completa",
    "Targeta Electronica",
    "Cabezal Perfusor",
    "Mecanismo completo",
    "Operativo",
    "Inoperativo",
    "Pendiente por Repuesto"
]

check_list_state =[False]*len(check_list)
check_list_state[0] = True
check_list_state[16] = True
check_list_state[17] = True
check_list_state[19] = True
check_list_state[21] = True
check_list_state[22] = True
check_list_state[23] = True
check_list_state[45] = True
check_list_state[51] = True

def generar_pdf(e):
    data = pd.read_excel('C:\\Users\\BRIX\\OneDrive - B. Braun\\bb170823.xlsx')
    n_inf =3236
    for sn,qr in zip(data["SN"],data["QR"]):
        pdf.make_pdf([
            inst.value,
            serv.value,
            model.value,
            str(sn),
            str(qr),
            fecha.value,
            otros_eval.value,
            porcentaje.value,
            otros_act.value,
            otros_rep.value,
            comen_rec.value,
            firma.value
        ],check_list_state,n_informe=n_inf,name_img = f"bbs_{n_inf}.jpg")
        n_inf+=1

def checkbox_changed(e):
    print(e.control.label)
    print(e.data)
    check_list_state[check_list.index(e.control.label)]=bool(e.data)
        

def select_opcion(label,placeholder,li):
    return ft.Dropdown(
        label=label,
        hint_text=placeholder,
        options=[ft.dropdown.Option(i) for i in li]
    )

inst=select_opcion("Institución","Institucion",list_institucion)
serv=ft.TextField(label="Servicio",height=40)
model=select_opcion("Modelo","Seleccione el modelo",["I. Space","P. Space","Compac Plus"])
serie = ft.TextField(label = "Serie",height=40)
Qr = ft.TextField(label="QR",height=40)
fecha = ft.TextField(label="Fecha",value=str(datetime.date.today()),height=40)
otros_eval=ft.TextField(label="Otros_eval",height=40)
otros_act = ft.TextField(label="Otros_act",height=40)
porcentaje = ft.TextField(label="%",height=40,width=40)
otros_rep = ft.TextField(label="Otros Repuestos",height=40)
comen_rec = ft.TextField(label="Comentarios y Recomendaciones",height=40,width=600)
firma = ft.TextField(label="firma",height=40,width=600)

def pick_files_result(e: ft.FilePickerResultEvent):
        xls_path=e.files[0].path
        
def main(page:ft.Page):
    

    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    l1 = ft.Row([
        inst,
        serv,
        model
    ])

    l2 = ft.Row([
        serie,
        Qr,
        fecha
    ])

    l3 = ft.Row([
        ft.Checkbox(label=check_list[0], value=True,on_change=checkbox_changed,width=width_check),
        ft.Checkbox(label=check_list[1], value=False,on_change=checkbox_changed,width=width_check)
    ])

    l4 = ft.Row([
        ft.Checkbox(label=check_list[2], value=False,on_change=checkbox_changed,width=width_check),
        ft.Checkbox(label=check_list[3], value=False,on_change=checkbox_changed,width=width_check),
        ft.Checkbox(label=check_list[4], value=False,on_change=checkbox_changed,width=width_check),
        ft.Checkbox(label=check_list[5], value=False,on_change=checkbox_changed,width=width_check)
    ])

    l5 = ft.Row([
        ft.Checkbox(label=check_list[6], value=False,on_change=checkbox_changed,width=width_check),
        ft.Checkbox(label=check_list[7], value=False,on_change=checkbox_changed,width=width_check),
        ft.Checkbox(label=check_list[8], value=False,on_change=checkbox_changed,width=width_check),
        ft.Checkbox(label=check_list[9], value=False,on_change=checkbox_changed,width=width_check)
    ])

    l6 = ft.Row([
        ft.Checkbox(label=check_list[10], value=False,on_change=checkbox_changed,width=width_check),
        ft.Checkbox(label=check_list[11], value=False,on_change=checkbox_changed,width=width_check),
        ft.Checkbox(label=check_list[12], value=False,on_change=checkbox_changed,width=width_check),
        ft.Checkbox(label=check_list[13], value=False,on_change=checkbox_changed,width=width_check)
        
    ])

    l7 = ft.Row([
        ft.Checkbox(label=check_list[14], value=False,on_change=checkbox_changed,width=width_check),
        ft.Checkbox(label=check_list[15], value=False,on_change=checkbox_changed,width=width_check),
        otros_eval
    ])

    l8 = ft.Row([
        ft.Checkbox(label=check_list[16], value=True,on_change=checkbox_changed,width=width_check),
        ft.Checkbox(label=check_list[17], value=True,on_change=checkbox_changed,width=width_check)
    ])

    l9 = ft.Row([
        ft.Checkbox(label=check_list[18], value=False,on_change=checkbox_changed,width=width_check),
        ft.Checkbox(label=check_list[19], value=True,on_change=checkbox_changed,width=width_check),
    ])

    l10 = ft.Row([
        ft.Checkbox(label=check_list[20], value=False,on_change=checkbox_changed,width=width_check),
        ft.Checkbox(label=check_list[21], value=True,on_change=checkbox_changed,width=width_check),
    ])

    l11 = ft.Row([
        ft.Checkbox(label=check_list[22], value=True,on_change=checkbox_changed,width=width_check),
        ft.Checkbox(label=check_list[23], value=True,on_change=checkbox_changed,width=width_check)
    ])
    l12 = ft.Row([
        porcentaje,
        ft.Checkbox(label=check_list[24], value=True,on_change=checkbox_changed,width=width_check),
        ft.Checkbox(label=check_list[25], value=False,on_change=checkbox_changed,width=width_check),
    ])

    l13 = ft.Row([
        ft.Text(value="",width=40),
        ft.Checkbox(label=check_list[26], value=True,on_change=checkbox_changed,width=width_check),
        ft.Checkbox(label=check_list[27], value=False,on_change=checkbox_changed,width=width_check)
    ])

    l14 = ft.Row([
        ft.Text(value="",width=40),
        ft.Checkbox(label=check_list[28], value=True,on_change=checkbox_changed,width=width_check),
        ft.Checkbox(label=check_list[29], value=False,on_change=checkbox_changed,width=width_check),
        
    ])

    l15 = ft.Row([
        ft.Text(value="",width=40),
        ft.Checkbox(label=check_list[30], value=True,on_change=checkbox_changed,width=width_check),
        ft.Checkbox(label=check_list[31], value=False,on_change=checkbox_changed,width=width_check),
        
    ])

    l16 = ft.Row([
        ft.Text(value="",width=40),
        ft.Checkbox(label=check_list[32], value=True,on_change=checkbox_changed,width=width_check),
        ft.Checkbox(label=check_list[33], value=False,on_change=checkbox_changed,width=width_check)
        
    ])

    l17 = ft.Row([
        ft.Checkbox(label=check_list[34], value=False,on_change=checkbox_changed,width=width_check),
        ft.Checkbox(label=check_list[35], value=False,on_change=checkbox_changed,width=width_check),
        ft.Checkbox(label=check_list[36], value=False,on_change=checkbox_changed,width=width_check),
        ft.Checkbox(label=check_list[37], value=False,on_change=checkbox_changed,width=width_check)
        
    ])

    l18 = ft.Row([
        ft.Checkbox(label=check_list[38], value=False,on_change=checkbox_changed,width=width_check),
        ft.Checkbox(label=check_list[39], value=False,on_change=checkbox_changed,width=width_check),
        ft.Checkbox(label=check_list[40], value=False,on_change=checkbox_changed,width=width_check),
        ft.Checkbox(label=check_list[41], value=False,on_change=checkbox_changed,width=width_check),
    ])

    l19 = ft.Row([
        ft.Checkbox(label=check_list[42], value=False,on_change=checkbox_changed,width=width_check),
        ft.Checkbox(label=check_list[43], value=False,on_change=checkbox_changed,width=width_check),
        ft.Checkbox(label=check_list[44], value=False,on_change=checkbox_changed,width=width_check),
        ft.Checkbox(label=check_list[45], value=True,on_change=checkbox_changed,width=width_check),
    ])

    l20 = ft.Row([
        ft.Checkbox(label=check_list[46], value=False,on_change=checkbox_changed,width=width_check),
        ft.Checkbox(label=check_list[47], value=False,on_change=checkbox_changed,width=width_check),
        ft.Checkbox(label=check_list[48], value=False,on_change=checkbox_changed,width=width_check),
        ft.Checkbox(label=check_list[49], value=False,on_change=checkbox_changed,width=width_check),
    ])

    l21 = ft.Row([
        ft.Checkbox(label=check_list[50], value=False,on_change=checkbox_changed,width=width_check),
        otros_rep
    ])

    l22 = ft.Row([
        ft.Checkbox(label=check_list[51], value=True,on_change=checkbox_changed,width=width_check),
        ft.Checkbox(label=check_list[52], value=False,on_change=checkbox_changed,width=width_check),
        ft.Checkbox(label=check_list[53], value=False,on_change=checkbox_changed,width=width_check),
    ])



    page.add(
        ft.Column([
            l1,l2,ft.ElevatedButton(
                    "Pick files",
                    icon=ft.icons.UPLOAD_FILE,
                    on_click=lambda _: pick_files_dialog.pick_files(
                        allow_multiple=True
                    ),
                ),
                l3, ft.Text(value ="Evaluacion del Eqipo"),
            l4,l5,l6,l7,
            ft.Row([
                ft.Column([ft.Text(value ="Actividades Realizadas"),l8,l9,l10,l11,otros_act]),
                ft.Column([ft.Text(value ="Conformidad de las Pruebas Realizadas"),
                           l12,l13,l14,l15,l16],alignment=ft.alignment.top_center)
            ]),
            ft.Column([ft.Text(value ="Repuestos Cambiados"),l17,l18,l19,l20,l21],alignment=ft.alignment.top_center),
            ft.Column([ft.Text(value="Estado final del Equipo"),l22,
                       comen_rec
                       ]),
                       ft.FloatingActionButton(text="Generar Informe",width=500,on_click=generar_pdf)
        ],
        spacing=10,
        height=940,
        width=1000,
        scroll=ft.ScrollMode.ALWAYS)
    )



ft.app(target=main)