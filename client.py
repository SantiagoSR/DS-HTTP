import requests
import cmd


def STATUS(url):
    global STATUS_ADDR
    STATUS_ADDR = "http://ec2-3-85-36-56.compute-1.amazonaws.com:3000"
    r = requests.post('http://ec2-3-85-36-56.compute-1.amazonaws.com:3000', data =
            {'url': url})
    print(f"{r}")

def SHORTY(url):
    global STATUS_ADDR
    STATUS_ADDR = "http://ec2-44-196-1-65.compute-1.amazonaws.com:3000"
    r = requests.post(STATUS_ADDR, data =
            {'url': url})
    print(f"{r.text}")

def REQUESTS():
    global COUNT_ADDR
    COUNT_ADDR = "http://ec2-54-165-183-13.compute-1.amazonaws.com:3000"
    r = requests.get(COUNT_ADDR)
    print(f'{r.text}')

def QR(url):
    global QR_ADDR
    QR_ADDR = "http://ec2-3-92-174-11.compute-1.amazonaws.com:3000"
    r = requests.post(QR_ADDR, data = {'url': url})

    print(f"{r.text}")
 
class ShortyShell(cmd.Cmd):
    intro = "Welcome to shorty, the URL shortner. \n Type help COMMAND_NAME to see further information about the command. \n Type bye to leave."
    prompt = "ShortyShell -> "
    file = None
    def do_STATUS(self, arg):
        'Generates STATUS based on URL: STATUS <URL> '
        STATUS(str(arg))

    def do_REQUESTS(self, arg):
        'Generates STATUS based on URL: REQUESTS <URL> '
        REQUESTS()
    
    def do_SHORTY(self, arg):
        'Generates SHORT URL based on URL: SHORTY <URL> '
        SHORTY(str(arg))
    
    def do_QR(self, arg):
        'Generates QR based on URL: QR <URL> '
        QR(str(arg))

def main():
    shell = ShortyShell()
    try:
        shell.cmdloop()
    except Exception as e:
        print(f"Sorry, we were not expecting that. {e}")

 

if __name__ == "__main__":
    main()
