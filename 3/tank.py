from hitbox import Hitbox
from tkinter import PhotoImage, NW

class Tank:
    __count = 0
    #__SIZE = 100

    def __init__(self, canvas, x, y,model = 'Т-14 Армата', ammo = 100, speed = 10, file_up = '../img/tank_up.png',
                 file_down = '../img/tank_down.png', file_left = '../img/tank_left.png', file_right = '../img/tank_right.png'):
        self.__skin_up = PhotoImage(file=file_up)
        self.__skin_down = PhotoImage(file=file_down)
        self.__skin_left = PhotoImage(file=file_left)
        self.__skin_right = PhotoImage(file=file_right)
        self.__hitbox = Hitbox(x, y, self.get_size(), self.get_size())   # 1. добавить атрибут hitbox
        self.__canvas = canvas
        Tank.__count += 1
        self.__model = model
        self.__hp = 100
        self.__xp = 0
        self.__ammo = ammo
        self.__fuel = 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        self.__speed = speed
        self.__x = x
        self.__y = y
        self.__vx = 0
        self.__vy = 0
        self.__dx = 0
        self.__dy = 0
        if self.__x < 0:
            self.__x = 0
        if self.__y < 0:
            self.__y = 0
        self.__create()
        self.right()

    def fire(self):
        if self.__ammo > 0:
            self.__ammo -= 1
            print('стреляю')

    def forward(self):
        self.__vx = 0
        self.__vy = -1
        self.__canvas.itemconfig(self.__id, image=self.__skin_up)


    def backward(self):
        self.__vx = 0
        self.__vy = 1
        self.__canvas.itemconfig(self.__id, image=self.__skin_down)


    def left(self):
        self.__vx = -1
        self.__vy =0
        self.__canvas.itemconfig(self.__id, image=self.__skin_left)


    def right(self):
        self.__vx = 1
        self.__vy = 0
        self.__canvas.itemconfig(self.__id, image=self.__skin_right)


    def update(self):
        if self.__fuel > self.__speed:
            self.__fuel -= self.__speed
            self.__dx = self.__vx * self.__speed
            self.__dy = self.__vy * self.__speed
            self.__x += self.__dx
            self.__y += self.__dy
            self.__update_hitbox()
            self.__repaint()

    def __create(self):
        self.__id = self.__canvas.create_image(self.__x, self.__y, image = self.__skin_up, anchor = NW)


    def __repaint(self):
        self.__canvas.moveto(self.__id, x = self.__x, y = self.__y)



    #  2 метод движения хитбокса
    def __update_hitbox(self):
        self.__hitbox.moveto(self.__x, self.__y)








#    3   метод проверки столкновения - обертка
    def inersects(self, other_tank):
        return self.__hitbox.intersects(other_tank.__hitbox)

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_ammo(self):
        return self.__ammo

    def get_model(self):
        return self.__model

    def get_hp(self):
        return self.__hp

    def get_xp(self):
        return self.__xp

    def get_fuel(self):
        return self.__fuel

    def get_speed(self):
        return self.__speed

    @staticmethod
    def get_quantity():
        return Tank.__count

    #@staticmethod
    def get_size(self):
        return self.__skin_up.width()

    def undo_move(self):
        self.__x -= self.__dx
        self.__y -= self.__dy
        self.__fuel += self.__speed
        self.__update_hitbox()
        self.__repaint()
        pass


    def __str__(self):
        return (f'координаты: x = {self.__x}, y = {self.__y}, модель: {self.__model}, '
                f'здоровье: {self.__hp}, опыт: {self.__xp}, боеприпасы: {self.__ammo}')