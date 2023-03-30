from PIL import Image, ImageFilter


def editor_photo():
    stop_while = input('Начало работы --- ')

    while stop_while != 'Стоп':

        image_my = Image.open(f'{input("название пожалуйсто в формате Jpg ---")}')

        filters_my_inp = int(input('блюр - 1\n'
                                   'добавить детализации - 2\n'
                                   'рисунок карандашом - 3\n'
                                   'Выделение контуров - 4\n'
                                   'Тиснение (имитация отпечатка) - 5\n'
                                   'Увеличение резкости - 6\n'
                                   'Сглаживание - 7\n'))

        if filters_my_inp == 1:
            my = image_my.filter(ImageFilter.BLUR)
            my.save('edit_photo.jpg')
        elif filters_my_inp == 2:
            my = image_my.filter(ImageFilter.DETAIL)
            my.save('edit_photo.jpg')
        elif filters_my_inp == 3:
            my = image_my.filter(ImageFilter.CONTOUR)
            my.save('edit_photo.jpg')
        elif filters_my_inp == 4:
            my = image_my.filter(ImageFilter.EDGE_ENHANCE)
            my.save('edit_photo.jpg')
        elif filters_my_inp == 5:
            my = image_my.filter(ImageFilter.EMBOSS)
            my.save('edit_photo.jpg')
        elif filters_my_inp == 6:
            my = image_my.filter(ImageFilter.SHARPEN)
            my.save('edit_photo.jpg')
        elif filters_my_inp == 7:
            my = image_my.filter(ImageFilter.SMOOTH)
            my.save('edit_photo.jpg')

        new_photo = Image.open('edit_photo.jpg')
        new_photo.show()
        stop_while = input('Стоп для завершения или продолжить редактирование --- ')

        hight, weight = new_photo.size

        while stop_while != 'Стоп1':
            print('кольчество пикселей не должно быть равным и не привышать размер фото !')
            print(f'высота - {hight}\n'
                  f'ширина - {weight}')

            # lef = int(input('Сколько пикселей отступить слева '))  <----
            # top = int(input('Сколько пикселей отступить сверху ')) - это и выше почемуто не работают
            rig = input('Сколько пикселей отступить справа ')
            bot = input('Сколько пикселей отступить снизуй ')

            new_photo = new_photo.crop((0, 0, int(rig), int(bot))) # <---- вот тут вместо 0 оно не работает
            hight, weight = new_photo.size
            stop_while = input('"Стоп1" для завершения или "Сохранить" для сохранения --- ')

            if stop_while == 'Сохранить':
                new_photo.save('edit_photo_crop.jpg')
                new_photo.show()


edit_func = editor_photo()
