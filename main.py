import tkinter as tk
import subprocess


def download():
    cmd = downloader.decode('utf-8') + " -f 140 " + str(urlString.get())
    for path in execute(cmd):
        print(path, end="")


def execute(cmd):
    popen = subprocess.Popen(cmd, stdout=subprocess.PIPE, universal_newlines=True, shell=True)
    for stdout_line in iter(popen.stdout.readline, ""):
        yield stdout_line
    popen.stdout.close()
    return_code = popen.wait()
    if return_code:
        raise subprocess.CalledProcessError(return_code, cmd)


def getClipboard():
    urlString.set(root.clipboard_get())


result = subprocess.run(['which', 'youtube-dl'], stdout=subprocess.PIPE)
downloader = result.stdout.strip()

root = tk.Tk()
root.title('Youtube-dl GUI')

# place a label on the root window
tk.Label(root, text=downloader).pack()
urlString = tk.StringVar(root, value='https://www.youtube.com/watch?v=K096sx5whTE')
urlEntry = tk.Entry(root, textvariable=urlString)
urlEntry.pack()

dwButton = tk.Button(root, text="Download", command=download)
dwButton.pack()

dwButton = tk.Button(root, text="Paste", command=getClipboard)
dwButton.pack()


# keep the window displaying
root.mainloop()
