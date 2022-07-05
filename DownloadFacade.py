import subprocess


class DownloadFacade:
    def __init__(self, downloader):
        self.__downloader = downloader

    def get_downloader(self):
        return self.__downloader

    def download(self, urlstring):
        cmd = self.__downloader + " -f 140 " + str(urlstring.get())
        print("downloading: " + cmd)
        for path in self.__execute(cmd):
            print(path, end="")
        return

    @staticmethod
    def __execute(cmd):
        popen = subprocess.Popen(cmd, stdout=subprocess.PIPE, universal_newlines=True, shell=True)
        for stdout_line in iter(popen.stdout.readline, ""):
            yield stdout_line
        popen.stdout.close()
        return_code = popen.wait()
        if return_code:
            raise subprocess.CalledProcessError(return_code, cmd)
        return
