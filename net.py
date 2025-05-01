import requests

def send_file_content():
    # 获取用户输入并处理协议头
    url_input = input("请输入目标URL或IP地址: ").strip()
    if not url_input.startswith(('http://', 'https://')):
        url = f'http://{url_input}'  # 默认添加http协议
    else:
        url = url_input

    try:
        # 读取文件内容
        with open('send.net', 'r', encoding='utf-8') as file:
            file_content = file.read()
    except FileNotFoundError:
        print("错误：send.net文件不存在")
        return
    except Exception as e:
        print(f"读取文件失败：{str(e)}")
        return
    for aaa in range(1000):#lllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll
        try:
        # 发送POST请求（根据需求可改为PUT）
            response = requests.post(
                url,
                data=file_content,
                timeout=10,
                headers={'User-Agent': 'Mozilla/5.0'},
                verify=True  # 保持SSL验证
            )
            print(f"响应状态码: {response.status_code}")


        except requests.exceptions.SSLError:
            print("SSL证书验证失败，尝试使用 verify=False 或检查证书")
        except requests.exceptions.ConnectionError:
            print("连接失败，请检查网络或目标地址")
        except requests.exceptions.Timeout:
            print("请求超时，请检查网络连接或增加超时时间")
        except requests.exceptions.RequestException as e:
            print(f"请求异常：{str(e)}")

if __name__ == "__main__":
    send_file_content()