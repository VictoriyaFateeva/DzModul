def func_2():
    if __name__ != '__main__':
        print('Я второй')

func_2()

if __name__=='__main__':
    print('Я второй и я предпочел бы быть модулем')