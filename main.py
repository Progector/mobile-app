# Здесь должен быть твой код
# программа с двумя экранами
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen


class MainScr(Screen):
    def __init__(self, name = 'main'):
        super().__init__(name = name)
        # global names
        # global age
        box1 = BoxLayout(orientation = 'vertical', spacing = 1)
        box2 = BoxLayout(orientation = 'horizontal',
        padding = 20, spacing = 1)
        box3 = BoxLayout(orientation = 'horizontal',
        padding = 20, spacing = 1)
        box4 = BoxLayout(orientation = 'vertical', spacing = 1)
        txt = Label(markup = True, text = 'Данное приложение позволит вам с помощью теста Руфье провести первичную диагностику вашего' +'\n' + 'здоровья.' +'\n' +'\n' + 'Проба Руфье представляет собой нагрузочный комплекс, предназначенный для оценки работоспособности' +'\n' + 'сердца при физической нагрузке. ' +'\n' +'\n' + 'У испытуемого определяют частоту пульса за 15 секунд.' +'\n' + '\n' +'Затем в течение 45 секунд испытуемый выполняет 30 приседаний. ' +'\n' +'\n' + 'После окончания нагрузки пульс подсчитывается вновь:число пульсаций за первые 15 секунд, 30 секунд отдыха, ' +'\n' + ' число пульсаций за последние 15 секунд.', size_hint = (1, 1.5))
        btn = Button(text = 'Дальше', size_hint = (1, .3))
        name_in = TextInput(size_hint = (1, .4), multiline = False)
        txt1 = Label(text = 'Введите возраст', size_hint = (1, .4))
        age_in = TextInput(size_hint = (1, .4), multiline = False)
        txt2 = Label(text = 'Введите ваше имя', size_hint = (1, .4))
        btn.on_press = self.next
        self.add_widget(box1)
        box1.add_widget(txt)
        box1.add_widget(box4)
        box1.add_widget(btn)
        box4.add_widget(box2)
        box4.add_widget(box3)
        box2.add_widget(txt1)
        box2.add_widget(name_in)
        box3.add_widget(txt2)
        box3.add_widget(age_in)
 
    
    def next(self):
        # age = age_in.text
        # names = name_in.text
        self.manager.transition.direction = 'left'
        self.manager.current = 'first'


class FirstScr(Screen):
    def __init__(self, name = 'first'):
        super().__init__(name = name)
        global p1
        box1 = BoxLayout(orientation = 'vertical')
        box2 = BoxLayout(orientation = 'vertical', 
                         padding = 10, spacing = 10)
        box3 = BoxLayout()
        txt = Label(markup = True, text = 'Замерьте пульс за 15 секунд' + '\n' + 'Результат запишите в соответствующее поле.')
        btn = Button(text = 'Дальше', size_hint = (1, .3))
        txtin = TextInput(size_hint = (1, .4), multiline = False)
        p1_in = Label(text = 'Введите результат', size_hint = (1, .3))
        btn.on_press = self.next
        self.add_widget(box1)
        box1.add_widget(txt)
        box1.add_widget(box2)
        box2.add_widget(box3)
        box3.add_widget(p1_in)
        box3.add_widget(txtin)
        box2.add_widget(btn)


    def next(self):
        # p1 = p1_in.text        
        self.manager.transition.direction = 'left'
        self.manager.current = 'second'    

class SecondScr(Screen):
    def __init__(self, name = 'second'):
        super().__init__(name = name)
        box1 = BoxLayout(orientation = 'vertical')
        box2 = BoxLayout(orientation = 'vertical', 
                         padding = 10, spacing = 10)
        txt = Label(markup = True, text = 'Выполните 30 приседаний за 45 секунд.' )
        btn = Button(text = 'Дальше', size_hint = (1, .3))
        btn.on_press = self.next
        self.add_widget(box1)
        box1.add_widget(txt)
        box1.add_widget(box2)
        box2.add_widget(btn)

    def next(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'thrid' 

class ThridScr(Screen):
    def __init__(self, name = 'thrid'):
        super().__init__(name = name)
        global p2
        global p3
        box1 = BoxLayout(orientation = 'vertical')
        box2 = BoxLayout(orientation = 'vertical', 
                         padding = 20, spacing = 1)
        box3 = BoxLayout(orientation = 'vertical', padding = 10, spacing = 10)
        txt  = Label(markup = True, text = 'В течении минуты замерьте пульс 2 раза:' + '\n' + 'За первые 15 секунд минуты, затем за последние 15 секунд' + '\n' + 'Результаты запишите в соответсвующие поля.')
        btn = Button(text = 'Дальше')
        txtin2 = TextInput(size_hint = (1, .4), multiline = False)
        p2_in = Label(text = 'Введите результат', size_hint = (1, .4))
        txtin3 = TextInput(size_hint = (1, .4), multiline = False)
        p3_in = Label(text = 'Введите результат после отдыха', size_hint = (1, .4))
        btn.on_press = self.next
        self.add_widget(box1)
        box1.add_widget(txt)
        box1.add_widget(box3)
        box1.add_widget(box2)
        box2.add_widget(btn)
        box3.add_widget(p2_in)
        box3.add_widget(txtin2)
        box3.add_widget(p3_in)
        box3.add_widget(txtin3)
      
       
    def next(self):
        # p2 = p2_in.text
        # p3 = p3_in.text
        self.manager.transition.direction = 'left'
        self.manager.current = 'fourth'  
          

class FourthScr(Screen):
    def __init__(self, name = 'fourth'):
        super().__init__(name = name)
        box1 = BoxLayout(orientation = 'vertical')
        # для имени
        # txt1 = Label(text = self.names)
        # для возраста
        # txt2 = Label(text = self.age)
        btn = Button(text = 'Назад')
        btn.on_press = self.next
        self.add_widget(box1)
        # box1.add_widget(txt1)
        # box1.add_widget(txt2)
        box1.add_widget(btn)


    def next(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'main'   
    

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScr())
        sm.add_widget(FirstScr())
        sm.add_widget(SecondScr())
        sm.add_widget(ThridScr())
        sm.add_widget(FourthScr())
        return sm

app = MyApp()
app.run()