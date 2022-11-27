import tkinter as tk
from tkinter import *
import matplotlib
import pandas as pd

matplotlib.use('TKAgg')

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class UserInterface(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('Sensor Data')
        self.geometry('1000x800')
        frame = Frame(self)

        frame.pack(side=tk.TOP, expand=1, anchor='w')

        figure = Figure(figsize=(6, 4), dpi=100)

        tempFigure_canvas = FigureCanvasTkAgg(figure, self)

        tempFigure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        temp_summarize = Button(frame, text='Summarize', command= self.temp_summarize())
        aggregate = Button(frame, text='Aggregate')
        temp_summarize.pack(side = RIGHT)
        aggregate.pack(side = RIGHT)
        self.axes = figure.add_subplot()

        frame = Frame(self)

        frame.pack(side=tk.TOP, expand=1, anchor='w')


        acc_magFrame_canvas = FigureCanvasTkAgg(figure, self)

        acc_magFrame_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        acc_summarize = Button(frame, text='Summarize', command=self.acc_mag_summarize())
        acc_summarize.pack(side=RIGHT)
        self.axes = figure.add_subplot()

        on_wrist_Frame = Frame(self)

        on_wrist_Frame.pack(side=tk.TOP, expand=1, anchor='w')

        on_wrist_Frame_canvas = FigureCanvasTkAgg(figure, self)

        on_wrist_Frame_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        on_wrist_summarize = Button(on_wrist_Frame, text='Summarize', command=self.on_wrist_summarize())
        on_wrist_summarize.pack(side=RIGHT)
        self.axes = figure.add_subplot()

        step_count_Frame = Frame(self)

        step_count_Frame.pack(side=tk.TOP, expand=1, anchor='w')

        step_count_Frame_canvas = FigureCanvasTkAgg(figure, self)

        step_count_Frame_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        step_count_summarize = Button(step_count_Frame, text='Summarize', command=self.step_count_summarize())
        step_count_summarize.pack(side=RIGHT)
        self.axes = figure.add_subplot()

        rest_Frame = Frame(self)

        rest_Frame.pack(side=tk.TOP, expand=1, anchor='w')

        rest_Frame_canvas = FigureCanvasTkAgg(figure, self)

        rest_Frame_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        rest_summarize = Button(rest_Frame, text='Summarize', command=self.rest_summarize())
        rest_summarize.pack(side=RIGHT)
        self.axes = figure.add_subplot()

        EDA_Frame = Frame(self)

        EDA_Frame.pack(side=tk.TOP, expand=1, anchor='w')


        EDA_Frame_canvas = FigureCanvasTkAgg(figure, self)

        EDA_Frame_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        EDA_summarize = Button(EDA_Frame, text='Summarize', command=self.EDA_summarize())
        EDA_summarize.pack(side=RIGHT)
        self.axes = figure.add_subplot()

        Movement_Frame = Frame(self)

        Movement_Frame.pack(side=tk.TOP, expand=1, anchor='w')

        Movement_Frame_canvas = FigureCanvasTkAgg(figure, self)

        Movement_Frame_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        Movement_summarize = Button(Movement_Frame, text='Summarize', command=self.Movement_summarize())
        Movement_summarize.pack(side=RIGHT)
        self.axes = figure.add_subplot()

        E
        # add data here

        # function to add data to graphs
        # self.df= pd.DataFrame(data, columns=[' ', ' '])

        # temp
        # acc_mag
        # on_wrist
        # step_count
        # rest
        # EDA
        # Movement intensity

    def temp_summarize(self):
        pass
    def acc_mag_summarize(self):
        pass
    def on_wrist_summarize(self):
        pass
    def step_count_summarize(self):
        pass
    def rest_summarize(self):
        pass
    def EDA_summarize(self):
        pass
    def Movement_summarize(self):
        pass

    def callback(self):
        self.axes.clear()
        self.df.plot(y='y-axis', x='time', ax=self.axes)
        self.axes.set_title('Sensor Data')
        self.axes.set_ylabel('Y-Axis')
        self.axes.figure.canvas.draw()
if __name__ == '__main__':
    ui = UserInterface()
    ui.mainloop()
