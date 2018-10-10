import ipfsapi

api = ipfsapi.connect('127.0.0.1', 5001)


def test_id():
    # 查看节点ID
    print(api.id())


def test_add():
    # 添加文件
    res = api.add('wallet.json')
    print(res)


def test_cat():
    # 查看文件
    print(api.cat("Qmc3KnyZv8KfhifgYzkALPpTQXjmXDSMWrGxQyV5MDoV8s"))


def test_add_multi_file():
    # 添加多个文件
    res = api.add('testfile', pattern='*.py')
    print(res)


def test_add_directory():
    # 添加文件夹 Qmc3KnyZv8KfhifgYzkALPpTQXjmXDSMWrGxQyV5MDoV8s
    res = api.add('fake_dir', recursive=True)
    print(res)


def test_download():
    # 下载文件夹或者文件
    api.get("Qmc3KnyZv8KfhifgYzkALPpTQXjmXDSMWrGxQyV5MDoV8s")


def test_ls():
    # 列出文件夹信息
    res = api.ls("Qmc3KnyZv8KfhifgYzkALPpTQXjmXDSMWrGxQyV5MDoV8s")
    print(res)


if __name__ == '__main__':
    test_ls()
    # 展示文件详细信息
    print(api.file_ls("Qmc3KnyZv8KfhifgYzkALPpTQXjmXDSMWrGxQyV5MDoV8s"))
