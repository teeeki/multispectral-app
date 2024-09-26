import tkinter as tk
from tkinter import filedialog
import customtkinter
import os
import numpy as np
# 作成モジュール
from functions.preprocessing_images import PreprocessingImages

FONT_TYPE = "meiryo"

class Application(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        self.title('マルチスペクトル画像処理')
        self.geometry('1270x750')
        self.fonts = (FONT_TYPE, 15)
        customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green
        
        # MenuFrameの設定
        self.menu_fram = MenuFrame().grid(row=0, column=0, padx=20, pady=20)


class MenuFrame(customtkinter.CTkFrame):
    def __init__(self, window=None):
        super().__init__(window)
        
        self.fonts = (FONT_TYPE, 15)
        
        self.create_widgets()
    
    
    # フォルダ選択ボタンの配置
    def create_widgets(self):
        self.button_select_dir = customtkinter.CTkButton(self, text='フォルダ選択',
                                                            command=self.select_dir_callback)
        self.button_select_dir.grid(row=0, padx=10, pady=(5,0), sticky="w")
        
        self.label_dir_name = customtkinter.CTkLabel(self, text='フォルダ名: なし')
        self.label_dir_name.grid(row=1, padx=10, pady=(5,0), sticky="w")
        
        self.button_start_proccesing = customtkinter.CTkButton(self, text='前処理開始', fg_color="#696969",
                                                            command=self.start_processing_callback)
        self.button_start_proccesing.grid(row=2, padx=10, pady=(5,0), sticky="w")
        
    
    
    # フォルダ選択ボタンが押されたときのコールバック。フォルダ選択ダイアログを表示する
    def select_dir_callback(self):
        
        # init_dir='C:/Users/taval/Documents/研究/スクリプト/frames/'
        init_dir = 'C:/project/processing_multispectral_image'
        if not os.path.exists(init_dir):
            init_dir = os.path.expanduser('~')
        # フォルダ選択のダイアログを開く
        self.select_dir_path = tk.filedialog.askdirectory(initialdir=init_dir)
        
        if self.select_dir_path:
            self.folder_name = os.path.basename(self.select_dir_path)
            self.label_dir_name.configure(text=f"フォルダ名: {self.folder_name}")
            
    def start_processing_callback(self):
        # 作成モジュールに渡す
        preprocessor = PreprocessingImages(self.select_dir_path)
        image_8bit_list = preprocessor.bit_convert()
        data_cubes_list = preprocessor.make_datacube()
        data_cubes_list = np.array(data_cubes_list)
        print(data_cubes_list.shape)