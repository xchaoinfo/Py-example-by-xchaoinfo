"""Socket Server IO 单线程多路复用 Demo"""

import queue
import socket
import select
import time

# 记录需要返回新的 Socket 以及消息的内容
sock_reply_msg_dict = {}


def handle_client(sock):
    byte_message = sock.recv(4096)
    print(byte_message)


def start_server(host="127.0.0.1", port="6000"):
    # start a server by TCP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        # sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
        server.bind((host, port))

        # 设置非阻塞模式, 如果不是多路复用，要设置成True, 不然程序很快退出
        server.setblocking(False)

        inputs = [server, ]

        # outputs存放链接需要返回的数据
        outputs = []
        # 为了循环调入select加入while
        while True:
            readable, writeables, exceptional = select.select(inputs, outputs, [])
            # print(readable, writeables, exceptional)
            # 收处理
            for r in readable:
                # 代表来了一个新连接
                if r is server:
                    # 等待客户端生成实例
                    conn, addr = server.accept()

                    print("client Connectiont from ", addr)
                    if conn not in inputs:
                        inputs.append(conn)
                    sock_reply_msg_dict[conn] = queue.Queue()

                # 接收新连接数据
                else:
                    if r not in outputs:
                        outputs.append(r)
                    # hander client function
                    handle_client()

            # 发数据：要返回给客户端的链接列表
            for w in writeables:
                # 重链接列表中取出队列的实例
                msg_queue = sock_reply_msg_dict.get(w)
                while msg_queue and (not msg_queue.empty()):
                    data_to_client = msg_queue.get()
                    # 返回给客户端数据
                    w.sendall(data_to_client)
                    time.sleep(2)


if __name__ == '__main__':
    start_server()
