from plyer import notification
import socket
import argparse


def main():
    parse = argparse.ArgumentParser()
    parse.add_argument('-ip')
    parse.add_argument('-port')

    rslt = parse.parse_args()
    ip = rslt.ip
    port_id = rslt.port

    connection = socket.create_connection((ip, int(port_id)))

    print(connection)

    notification.notify(
        title='Here is the title',
        message='Here is the message',
        app_icon=None,  # e.g. 'C:\\icon_32x32.ico'
        timeout=1000,  # seconds
    )
    connection.close()


if __name__ == "__main__":
    main()
