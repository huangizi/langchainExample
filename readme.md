





## 常见问题
如果openai访问超时，一定要记得加这两行，具体的端口要在你自己的代理软件里面查看
os.environ["http_proxy"] = "http://127.0.0.1:7890"
os.environ["https_proxy"] = "http://127.0.0.1:7890"