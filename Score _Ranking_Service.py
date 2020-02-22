import socket
import re

def service_client(new_socket):
    """为这个客户端返回数据"""
    # 定义一个列表,通过列表字典组合来 存储数据
    result ={}
    # 接受浏览器发送过来的请求
    request = new_socket.recv(1024).decode("utf-8")
    response_list = request.splitlines()
    print("1>>>>>>>>>>>>>>>>>")
    print(response_list)
    print("2>>>>>>>>>>>>>>>>>")
    ret = re.match(r"([^/]+/[^ ])(?:upload|query)",response_list[0])

    file_name = ret.group(2)
    # 接口1上传
    if file_name == 'upload':
        pass
    # 接口2查询
    elif file_name == 'query':
        pass
    else:
        response = "HTTP/1.1 404 NOT FOUND\r\n"
        response += "\r\n"
        response += "---Interface does not exist---"


    new_socket.send(response.encode("utf-8"))
   # 关闭套接字
    new_socket.close()

def main():
    """主程序"""
    # 1.tcp套接字
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 2.绑定
    tcp_server_socket.bind(("",8080))
    # 3.变为监听套接字
    tcp_server_socket.listen(128)
    while True:
        # 4.等待新客户端连接
        new_socket,client_addr = tcp_server_socket.accept()
        # 5.为这个客户端服务
        service_client(new_socket)
    # 关闭套接字
    tcp_server_socket.close()


if __name__ == '__main__':
    main()