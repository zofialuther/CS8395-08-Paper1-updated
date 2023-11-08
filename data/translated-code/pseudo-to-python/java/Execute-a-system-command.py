import subprocess

class MainEntry:
    def main(self):
        self.executeCmd("ls -oa")

    def executeCmd(self, string):
        pipedOut = None
        try:
            aProcess = subprocess.Popen(string, stdout=subprocess.PIPE, shell=True)
            aProcess.wait()
            pipedOut = aProcess.stdout
            buffer = bytearray(2048)
            read = pipedOut.read(buffer)
            while read >= 0:
                sys.stdout.write(buffer[0:read])
                read = pipedOut.read(buffer)
        except IOError as e:
            print(e)
        except KeyboardInterrupt as ie:
            print(ie)
        finally:
            if pipedOut is not None:
                try:
                    pipedOut.close()
                except IOError as e:
                    pass