import telnetlib

import passwordContainer
import speedtest_cli


def main():
    HOST = "192.168.1.1"
    username = "root"
    username = str.encode(username)
    password = passwordContainer.password
    password = str.encode(password)
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"DD-WRT login:")
    tn.write(username + b"\n")
    tn.read_until(b"Password:")
    tn.write(password + b"\n")
    tn.read_until(b"root@DD-WRT:~# ", 1)
    tn.write(b"stopservice wshaper\n")
    tn.read_until(b"root@DD-WRT:~# ", 1)
    result = speedtest_cli.speedtest()
    download = str(int((result[0] * 1000) * .89))
    decodedDownload = download
    download = str.encode(download)
    # Upload speed test appears to be bugged and rarely varies. So this will remain
    # static for my use case and is therefore unneeded.
    # upload = str(int((result[1] * 1000) * .89))
    # decodedUpload = upload
    # upload = str.encode(upload)
    tn.read_until(b"root@DD-WRT:~# ", 1)
    tn.write(b"nvram set wshaper_downlink=" + download + b"\n")
    tn.read_until(b"root@DD-WRT:~# ", 1)
    # tn.write(b"nvram set wshaper_uplink=" + upload + b"\n")
    tn.read_until(b"root@DD-WRT:~# ", 1)
    tn.write(b"startservice wshaper\n")

    # Prints download and upload
    # print("\nQOS settings applied. \n download = " + decodedDownload + "\n upload = " + decodedUpload + "\n")
    # Prints only download
    print("\nQOS settings applied. \n download = " + decodedDownload + "\n")


if __name__ == '__main__':
    main()
