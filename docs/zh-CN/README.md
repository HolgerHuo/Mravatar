# Mravatar - Mastodonwide Recognized Avatars

Mastodon头像API

通过Mastodon用户名返回头像URL或文件

## API 使用

### /avatar/\<username\> (GET)

```
https://mravatar.dragoncloud.win/avatar/@holgerhuo@dragon-fly.club
https://mravatar.dragoncloud.win/avatar/holgerhuo@dragon-fly.club
```

`GET`请求到[https://mravatar.dragoncloud.win/avatar/@holgerhuo@dragon-fly.club](https://mravatar.dragoncloud.win/avatar/@holgerhuo@dragon-fly.club) or [https://mravatar.dragoncloud.win/avatar/holgerhuo@dragon-fly.club](https://mravatar.dragoncloud.win/avatar/holgerhuo@dragon-fly.club)

#### Query Strings

- `proxied`
    - `true`
        通过 Mravatar 代理文件请求
    - `false` (默认)
        返回`302`跳转
- `no-cache`
    - `true`
        强制拉取最新头像
    - `false`
        使用 Mravatar 缓存 (如果已经存在)。缓存每3小时更新一次。
- `default`
    - `<url编码过的图片地址>`
        配置默认头像
        (默认为 https://cdn.jsdelivr.net/gh/mastodon/mastodon@latest/public/avatars/original/missing.png)

实例： `https://mravatar.dragoncloud.win/avatar/holgerhuo@dragon-fly.club?no-cache=true&proxied=true&default=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2F4%2F48%2FMastodon_Logotype_%2528Simple%2529.svg`

![holgerhuo](https://mravatar.dragoncloud.win/avatar/holgerhuo@dragon-fly.club?no-cache=true&proxied=true)

## 部署

![GitHub last commit](https://img.shields.io/github/last-commit/holgerhuo/mravatar)![GitHub release (latest by date)](https://img.shields.io/github/v/release/holgerhuo/mravatar)![GitHub](https://img.shields.io/github/license/holgerhuo/mravatar)![GitHub all releases](https://img.shields.io/github/downloads/holgerhuo/mravatar/total)![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/holgerhuo/mravatar)

### 依赖

**Mravatar需要`Python3.7+`，CentOS 7用户需要自行编译**

请确保你已安装`python3`、`pip3`、`python3-devel`以及`virtualenv`。

也需要`uWSGI`作为后端服务器。也可选择任意后端运行。

### 步骤

创建新用户，克隆仓库，配置环境，复制启动文件，开始运行！

```bash
pip3 install virtualenv
useradd mravatar
sudo su - mravatar
git clone https://github.com/HolgerHuo/mravatar.git mravatar
cd mravatar
virtualenv mravatar
source mravatar/bin/activate
pip3 install -r requirement.txt
exit
cp /home/mravatar/mravatar/dist/mravatar.service /etc/systemd/system/mravatar.service
cp /home/mravatar/mravatar/dist/mravatar.conf /etc/nginx/conf.d/mravatar.conf
systemctl enable --now mravatar
systemctl reload nginx
```

## 许可证

GNU Affero General Public License v3.0

©️ Holger Huo, Mastodon

[@holgerhuo@dragon-fly.club](https://mast.dragon-fly.club/@holgerhuo)