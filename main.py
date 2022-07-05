import tkinter as tk
import subprocess
from DownloadFacade import DownloadFacade


class App(tk.Tk):
    def __init__(self, root, download_facade):
        root.title('Youtube-dl GUI')

        # place a label on the root window
        tk.Label(root, text=download_facade.get_downloader()).pack()
        url_string = tk.StringVar(root, value='https://www.youtube.com/watch?v=K096sx5whTE')
        url_entry = tk.Entry(root, textvariable=url_string)
        url_entry.pack()

        dw_button = tk.Button(root, text="Download", command=lambda: download_facade.download(url_string))
        dw_button.pack()

        dw_button = tk.Button(root, text="Paste", command=lambda: get_clipboard(url_string, root))
        dw_button.pack()


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
