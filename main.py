import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.properties import NumericProperty
from kivy.uix.gridlayout import GridLayout
import calendar
from datetime import datetime
from kivy.uix.textinput import TextInput
import Conexion
import var


class Calendar(Popup):
    day = NumericProperty(0)
    month = NumericProperty(0)
    year = NumericProperty(0)
    root = BoxLayout(orientation="vertical")

    def __init__(self, **kwargs):
        super(Popup, self).__init__(**kwargs)
        self.add_widget(self.root)
        self.create_calendar()

    def create_calendar(self):
        self.day_str = ['L', 'M', 'X', 'J', 'V', 'S', 'D']
        self.month_str = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre',
                          'Octubre', 'Noviembre', 'Diciembre']

        self.dy = calendar.monthcalendar(self.year, self.month)
        self.title = (self.month_str[self.month - 1] + ", " + str(self.year))

        layout = GridLayout(cols=7)

        for d in self.day_str:
            b = Label(text='[b]' + d + '[/b]', markup=True)
            layout.add_widget(b)

        for wk in range(len(self.dy)):
            for d in range(0, 7):
                dateOfWeek = self.dy[wk][d]
                if not dateOfWeek == 0:
                    b= Button(text=str(dateOfWeek))
                    b.bind(on_release=self.date_selected)
                else:
                    b = Label(text='')
                layout.add_widget(b)
        if self.root:
            self.root.clear_widgets()
        self.root.add_widget(layout)
        bottombox = BoxLayout(orientation="horizontal", size_hint=(1, None), height=40)
        bottombox.add_widget(Button(text='<', on_release=self.change_month))
        bottombox.add_widget(Button(text='>', on_release=self.change_month))
        self.root.add_widget(bottombox)
        BtnMosElim = BoxLayout(orientation="horizontal", size_hint=(1, None), height=40)
        BtnMosElim.add_widget(Button(text='Mostrar', on_release=self.Mostrar))
        BtnMosElim.add_widget(Button(text='Eliminar Recordatorios', on_release=self.eliminar))
        self.root.add_widget(BtnMosElim)
        self.recordatorio = TextInput()
        self.root.add_widget(self.recordatorio)
        self.recordatorio.add_widget(TextInput())

    def change_month(self, event):
        if event.text == '>':
            if self.month == 12:
                self.month = 1
                self.year = self.year + 1
            else:
                self.month = self.month + 1
        elif event.text == '<':
            if self.month == 1:
                self.month = 12
                self.year = self.year - 1
            else:
                self.month = self.month - 1

    def date_selected(self,event):
        self.day = int(event.text)
        event.background_color = 1, 0, 0, 1
        Date=[]
        Date.append(self.day)
        Date.append(self.month)
        Date.append(self.year)
        Rec = []
        self.recordatorio= str(self.recordatorio.text)
        Rec.append(Date)
        Rec.append(str(self.recordatorio))
        Conexion.conexion.Altrecor(Rec)
        Conexion.conexion.MostrarRecordatorios(self)

    def eliminar(self, event):
        Conexion.conexion.EliminarRecor(self)

    def Mostrar(self,event):
        recordatorios=[]
        recordatorios=Conexion.conexion.MostrarRecordatorios(self)
        print(recordatorios)
        for i in recordatorios:
            recor= Label(text=recordatorios[1])
            fecha=Label(text=recordatorios[0])
            self.root.add_widget(recor)
            self.root.add_widget(fecha)


    def on_month(self, widget, event):
        self.create_calendar()

    def on_year(self, widget, event):
        self.create_calendar()

class MainApp(App):
    def build(self):
        self.popup = Calendar(month=datetime.now().month, year=datetime.now().year,
                              size_hint=(None, None), size=(500, 400))
        self.popup.bind(on_dismiss=self.on_dismiss)
        return Button(text="Enseñar Calendario", on_release=self.show_calendar)

    def show_calendar(self, event):
        self.popup.open()

    def on_dismiss(self, arg):
        # Do something on close of popup
        print("Dia selecionado ", str(self.popup.day) + '/' + str(self.popup.month) + '/' + str(self.popup.year))

    Conexion.conexion.db_connect(var.filebd)

if __name__ == "__main__":
    MainApp().run()
