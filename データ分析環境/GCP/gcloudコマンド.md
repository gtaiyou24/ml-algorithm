# gcloudコマンド

## GCPインスタンスにssh接続
```bash
gcloud compute ssh --zone {インスタンスのゾーン} "{インスタンス名}"
```

## GCPインスタンス上で起動したjupyterをローカルPCで操作する
```bash
gcloud compute ssh --zone {インスタンスのゾーン} "{インスタンス名}" -- -N -f -L 28888:localhost:8888
```