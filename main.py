import skrf as rf
import matplotlib.pyplot as plt
import tkinter
tkinter._test()

rf.stylely()

# Поиск файлов в папке
path = "D://obychenie//TDR//files//"  # меняй путь на свой
meas = rf.read_all_networks(path)
key = list(meas.keys())


# название файлов
for i in meas.keys():
    meas_new = meas[i] # копия для изменения
    meas_new = meas_new.s11.windowed(window=('taylor',10))

    # создание графика
    fig, ax = plt.subplots(2, 2, figsize=(10, 10), layout='constrained',facecolor='w')
    ax1 = ax[0, 0]
    ax2 = ax[0, 1]
    ax3 = ax[1, 0]
    ax4 = ax[1, 1]

    fig.suptitle(f'{i}',fontsize=30)  # Имя как у файла будет

    # Первый график S параметры не измененные
    meas[i].s11.plot_s_db(title='Измерения', ax = ax1)

    # Второй график S параметры во времени без окна (справа внизу)
    meas[i].s11.plot_s_time_db(title='Измерения в TDR', ax = ax2)

    # Третий график из времени с окном в S параметры (сверху слева)
    meas_new.plot_s_db(title='После наложения окна', ax = ax3)

    # Четвертый график во времени с окном (сверху внизу)
    meas_new.plot_s_time_db(title='Наложения окна',ax = ax4)

plt.show()

#window =
