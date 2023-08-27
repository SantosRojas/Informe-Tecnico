import flet as ft
import datetime
import pdf
import pandas as pd

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
check_list_state[24] = True
check_list_state[26] = True
check_list_state[28] = True
check_list_state[30] = True
check_list_state[32] = True
check_list_state[45] = True
check_list_state[51] = True

class Informe(ft.UserControl):
    def build(self):
        
        self.n_informe = 1
        #CAMPOS DE TEXTO
        self.inst=self.input_text(label="Institución",text_default="BBRAUN MEDICAL PERU")
        self.serv=self.input_text(label="Servicio",text_default="STOCK")
        self.model=self.select_opcion("Modelo","Seleccione el modelo",["I. SPACE","P. SPACE","P. SPACE PLUS","COMPAC PLUS"])
        self.serie = self.input_text(label = "Serie",on_change=self.verify_sq)
        self.qr = self.input_text(label="QR")
        self.fecha = self.input_text(label="Fecha",text_default=str(datetime.date.today()))
        self.otros_eval=self.input_text(label="Otros_eval",text_default="Mnto.Preventivo",width=400)
        self.otros_act = self.input_text(label="Otros_act",width=200)
        self.porcentaje = self.input_text(label="Test Exact.(%)",text_default="0",width=150)
        self.otros_rep = self.input_text(label="Otros Repuestos",width=200)
        self.comen_rec = self.input_text(
            label="Comentarios y Recomendaciones",
            width=600,text_default="Prueba de infusion y sensores OK")
        self.firma = self.input_text(label="firma",width=600)
        self.tabs = ft.Tabs(
            selected_index=0,
            on_change=self.tabs_changed,
            overlay_color=ft.colors.GREEN_700,
            indicator_color=ft.colors.GREEN_700,
            label_color=ft.colors.GREEN_ACCENT,
            tabs=[
                ft.Tab("Cliente"),
                ft.Tab("Evaluacion del Equipo"),
                ft.Tab("Actividades Realizadas"),
                ft.Tab("Repuestos Cambiados"),
                ft.Tab("Estado Final del Equipo")])
        
        self.pick_files_dialog = ft.FilePicker(on_result=self.pick_files_result)

        self.dlg_modal = ft.AlertDialog(
                modal=True,
                title=ft.Text("Error"),
                content=ft.Text("Usted no ha seleccionado ningun archivo"),
                actions=[
                    ft.TextButton("Cancelar", on_click=self.close_dialog,style=ft.ButtonStyle(bgcolor=ft.colors.GREEN_900)),
                    ft.TextButton("Intentar otra vez", on_click=self.intent_new ,style=ft.ButtonStyle(bgcolor=ft.colors.GREEN_400,color=ft.colors.BLACK)),
                ],
                actions_alignment=ft.MainAxisAlignment.END,
                on_dismiss=lambda e: print("Modal dialog dismissed!"),
            )
        
        self.file_selected = ft.Text(value="Empty Files")
        
        self.btn_make_informe = ft.FloatingActionButton(
                                    text="Generar Informe",
                                    width=150,height=40,
                                    bgcolor=ft.colors.GREEN_900,
                                    on_click=self.launch_make_informe,
                                    icon=ft.icons.FILE_DOWNLOAD,disabled=True)
        self.upload_file = ft.Row(
            alignment="center",
            controls=[
                ft.FloatingActionButton(
                    text="Subir excel",
                    width=150,height=40,
                    bgcolor=ft.colors.GREEN_900,
                    on_click=lambda _: self.pick_files_dialog.pick_files(),
                    icon=ft.icons.FILE_UPLOAD),
                self.file_selected
            ]
                )
        

        self.pb = ft.ProgressBar(width=400)
        
        self.progreso = ft.Column(
            alignment="center",
            controls=[
                ft.Text(value="0%"),
                self.pb
            ],
            visible=False
        )
                        
        #COMPONENTES

        self.app_bar = ft.Row(
            alignment="center",
            controls=[
                self.tabs,
                self.btn_make_informe
            ]
        )

        self.cliente =ft.Column(
            horizontal_alignment="center",
            controls=[
                ft.Row(alignment="center",controls=[self.inst,self.serv,self.model]),
                ft.Row(alignment="center",controls=[self.serie,self.qr,self.fecha]),
                self.check_btns(0,2)
            ] 
        )

        self.equipo = ft.Column([
            self.check_btns(2,6),
            self.check_btns(6,10),
            self.check_btns(10,14),
            ft.Row(alignment="center",controls=[self.check_btns(14,16),self.otros_eval])
            
        ])

        self.act_real = ft.Row(
            alignment="center",
            controls=[
                ft.Column(
            horizontal_alignment="center"
,            controls=[
            self.check_btns(16,18),
            self.check_btns(18,20),
            self.check_btns(20,22),
            self.check_btns(22,24),
            self.otros_act
            
        ]),
        ft.Column(
            horizontal_alignment="center",
            controls=[
                ft.Row(
            alignment="center",
            controls=[
                self.porcentaje,
                self.check_btns(24,26)
            ]),
            ft.Row(
            alignment="center",
            controls=[
                ft.Text("Test detect. aire",width=150),
                self.check_btns(26,28)
            ]),
            ft.Row(
            alignment="center",
            controls=[
                ft.Text("Test Pres. Alta",width=150),
                self.check_btns(28,30)
            ]),
            ft.Row(
            alignment="center",
            controls=[
                ft.Text("Test Ant. Flujo",width=150),
                self.check_btns(30,32)
            ]),
            ft.Row(
            alignment="center",
            controls=[
                ft.Text("Prueba Baterias",width=150),
                self.check_btns(32,34)
            ])
            ]
        )
            ])

        self.repuestos = ft.Column(
            alignment="center",
            controls=[
                self.check_btns(36,40),
                self.check_btns(36,40),
                self.check_btns(40,44),
                self.check_btns(44,48),
                ft.Row(alignment="center",controls=[self.check_btns(48,51),self.otros_rep]) 
        ])


        self.estado_final = ft.Column(
            horizontal_alignment="center",
            controls=[
                self.check_btns(51,54),
                self.comen_rec,
                self.upload_file.alignment,
                self.progreso
        ])

        self.inst.visible = True
        self.equipo.visible =False
        self.act_real.visible = False
        self.repuestos.visible = False
        self.estado_final.visible = False

        return (
            ft.Column(horizontal_alignment="center",
                      controls=[
                          self.pick_files_dialog,
                          self.app_bar,self.cliente,
                          self.equipo,self.act_real,
                          self.repuestos,
                          self.estado_final,
                          self.dlg_modal])
            
        )
    
    def verify_sq(self,e):
        if self.serie.value != "":
            self.btn_make_informe.disabled = False
            self.upload_file.disabled=True
        else: 
            self.btn_make_informe.disabled = True
            self.upload_file.disabled=False
        
        super().update()

    def intent_new(self,e):
        self.close_dialog(e)
        self.pick_files_dialog.pick_files()
    
    def close_dialog(self,e):
        self.dlg_modal.open = False
        super().update()


    def launch_make_informe(self,e):
        
        self.make_informe(serie=self.serie.value,qr=self.qr.value)

    def make_informe(self,serie,qr):
        textos = [
            self.inst.value,
            self.serv.value,
            self.model.value,
            serie,
            qr,
            self.fecha.value,
            self.otros_eval.value,
            self.otros_act.value,
            self.porcentaje.value,
            self.otros_rep.value,
            self.comen_rec.value,
            ""
        ]

        print("Elaborando informe, porfavor espere ...")
        
        pdf.make_pdf(textos=textos,checks=check_list_state,n_informe=self.n_informe)
        self.n_informe +=1
        print(self.n_informe)

    def pick_files_result(self,e: ft.FilePickerResultEvent):
        xls_file=e.files
        ruta = xls_file[0].path
        if not xls_file is None:
            self.file_selected.value = ruta
            self.serie.disabled = True
            self.qr.disabled = True
            self.btn_make_informe.disabled = False
            super().update()

            #data = pd.read_excel(ruta)
            data ={
                "SN":["1235468","15165","1235468","15165","1235468","15165"],
                "QR":["1551515","16515","1235468","15165","1235468","15165"]
            }
            for sn,qr,i in zip(data["SN"],data["QR"],range(1,len(data["SN"])+1)):
                self.make_informe(serie=sn,qr=qr)
                self.pb.value = i*(1/len(data["SN"]))
                super().update()

        else:
            self.dlg_modal.open = True
            super().update()
    
    def input_text(self,label,text_default="",width=None,on_change = None):
        return(
            ft.TextField(label=label,value=text_default,focused_border_color=ft.colors.GREEN_ACCENT,width=width,height=40,on_change=on_change)
        )
    
    def tabs_changed(self,e):
        status = str(self.tabs.tabs[self.tabs.selected_index].text)
        
        if status == "Cliente":
            self.cliente.visible = True
            self.equipo.visible =False
            self.act_real.visible = False
            self.repuestos.visible = False
            self.estado_final.visible = False

        if status == "Evaluacion del Equipo":
            self.cliente.visible = False
            self.equipo.visible =True
            self.act_real.visible = False
            self.repuestos.visible = False
            self.estado_final.visible = False
        
        if status == "Actividades Realizadas":
            self.cliente.visible = False
            self.equipo.visible =False
            self.act_real.visible = True
            self.repuestos.visible = False
            self.estado_final.visible = False
        
        if status == "Repuestos Cambiados":
            self.cliente.visible = False
            self.equipo.visible =False
            self.act_real.visible = False
            self.repuestos.visible = True
            self.estado_final.visible = False

        if status == "Estado Final del Equipo":
            self.cliente.visible = False
            self.equipo.visible =False
            self.act_real.visible = False
            self.repuestos.visible = False
            self.estado_final.visible = True

        super().update()

    def select_opcion(self,label,placeholder,li):
        return ft.Dropdown(
            label=label,
            focused_border_color=ft.colors.GREEN_ACCENT,
            height=45,
            dense=True,
            hint_text=placeholder,
            options=[ft.dropdown.Option(i) for i in li],
            value=li[0]
        )
    
    def checkbox_changed(self,e):
        if e.data =="true": value = 1 
        else: value = 0
        index = check_list.index(e.control.label)
        check_list_state[index] =value
    def check_btns(self,check_init = 0, check_final=4,width_check=200):
        return ft.Row(
            alignment="center",
            controls=[ft.Checkbox(
            label=check_list[n], 
            value=check_list_state[n],
            on_change=self.checkbox_changed,
            width=width_check,
            fill_color=ft.colors.GREEN_ACCENT
            ) for n in range(check_init,check_final)])
    
def main(page:ft.Page):
    page.title="INFORME TECNICO"
    page.horizontal_alignment = "center"
    page.scroll = "adaptve"
    page.window_height = 300
    page.window_width= 1000
    page.update()

    app = Informe()

    page.add(app)



ft.app(target=main)