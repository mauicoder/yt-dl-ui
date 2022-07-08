import tkinter as tk
from tkinter import ttk
import subprocess
from DownloadFacade import DownloadFacade


class App(tk.Tk):
    def __init__(self, root, download_facade):
        root.title('Youtube-dl GUI')

        # Create a style
        style = ttk.Style(root)

        print(style.theme_names())
        # Set the theme with the theme_use method
        style.theme_use('aqua')

        # place a label on the root window
        ttk.Label(root, text=download_facade.get_downloader()).pack()
        url_string = tk.StringVar(root, value='https://www.youtube.com/watch?v=K096sx5whTE')
        url_entry = ttk.Entry(root, textvariable=url_string)
        url_entry.pack(expand=True, fill='both', )

        dw_button = ttk.Button(root, text="Download", command=lambda: download_facade.download(url_string))
        dw_button.pack()

        dw_button = ttk.Button(root, text="Paste", command=lambda: get_clipboard(url_string, root))
        dw_button.pack()
        root.selected_theme = tk.StringVar()
        theme_frame = ttk.LabelFrame(root, text='Themes')
        for theme_name in style.theme_names():
            # Create a bulk of radio buttons using loop
            radio_buttons = ttk.Radiobutton(
                root,
                text=theme_name,
                value=theme_name,
                variable=root.selected_theme,
                command=lambda: theme_changer(style, root))
            radio_buttons.pack(expand=True, fill='both')


def theme_changer(style, window):
    # Change  theme
    style.theme_use(window.selected_theme.get())


def get_clipboard(url_string, root):
    url_string.set(root.clipboard_get())


def get_download_facade():
    result = subprocess.run(['which', 'youtube-dl'], stdout=subprocess.PIPE)
    downloader = result.stdout.strip().decode('utf-8')
    print(downloader)
    return DownloadFacade(downloader)


def main():
    download_facade = get_download_facade()
    root = tk.Tk()
    App(root, download_facade)
    root.mainloop()


if __name__ == '__main__':
    main()
