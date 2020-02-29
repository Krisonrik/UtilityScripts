import psutil
import time
import socket
import argparse


def RunServer(port_id: int, connection: list):
    sock = socket.create_server(('localhost', port_id))
    rslt = sock.accept()
    connection.extend(rslt)


def ReportStatus(online: {'online': False}):
    machine_status = {}
    cpu_count = psutil.cpu_count()
    single_core_max_perc = 100.0 / cpu_count
    print("single core max percentage is " + str(single_core_max_perc))
    job_started = False
    while online[0]:
        RunningStatus(machine_status)
        # print(machine_status)
        cpu_usage = float(machine_status["cup"])
        if cpu_usage >= single_core_max_perc:
            if job_started != True:
                print("Job started")
                job_started = True
        else:
            if job_started:
                job_started = not job_started
                print("Job completed")
        time.sleep(1)


def RunningStatus(stat: dict):
    stat["cup"] = psutil.cpu_percent()
    stat["memory"] = str(psutil.virtual_memory())


def main():
    parse = argparse.ArgumentParser()
    parse.add_argument('-p', help="Port number for connection")
    result = parse.parse_args()
    port_id = result.p
    while True:
        connection = ()
        RunServer(int(port_id), connection)
        print(connection[0])
        connection[0].close()
        return


if __name__ == "__main__":
    main()
