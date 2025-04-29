# Mravatar - Mastodonwide Recognized Avatars

![GitHub last commit](https://img.shields.io/github/last-commit/holgerhuo/mravatar)![GitHub release (latest by date)](https://img.shields.io/github/v/release/holgerhuo/mravatar)![GitHub](https://img.shields.io/github/license/holgerhuo/mravatar)![GitHub all releases](https://img.shields.io/github/downloads/holgerhuo/mravatar/total)![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/holgerhuo/mravatar)

A Mastodonwide Recognized Avatar API

This API provides you with avatar link or proxied avatar file through fediverse account name (@username@localpart).

## API Usages

### /avatar/\<username\> (GET)

```
https://mravatar.dragoncloud.win/avatar/@holgerhuo@dragon-fly.club
https://mravatar.dragoncloud.win/avatar/holgerhuo@dragon-fly.club
```

`GET` request [https://mravatar.dragoncloud.win/avatar/@holgerhuo@dragon-fly.club](https://mravatar.dragoncloud.win/avatar/@holgerhuo@dragon-fly.club) or [https://mravatar.dragoncloud.win/avatar/holgerhuo@dragon-fly.club](https://mravatar.dragoncloud.win/avatar/holgerhuo@dragon-fly.club)

#### Query Strings

- `proxied`
    - `true`
        Enable proxying from Mravatar
    - `false` (default)
        Retrieve `302` redirect 
- `no-cache`
    - `true`
        Force request latest avartar
    - `false`
        Use Mravatar cache (if exists). Cache is refreshed every 3h.
- `default`
    - `<url-encoded-img-url>`
        Set fallback image url.
        (Defaults to https://cdn.jsdelivr.net/gh/mastodon/mastodon@latest/public/avatars/original/missing.png)

Example: `https://mravatar.dragoncloud.win/avatar/holgerhuo@dragon-fly.club?no-cache=true&proxied=true&default=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2F4%2F48%2FMastodon_Logotype_%2528Simple%2529.svg`

## Deployment 

### Dependencies

Make sure you have `python3`, `pip3`, `python3-devel` and `virtualenv` installed.

### Procedures

Create a new user. Clone this repo. Setup virtualenv. Copy dist files. Start your server. Enjoy!

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

## License

GNU Affero General Public License v3.0

©️ Holger Huo, Mastodon

[@holgerhuo@dragon-fly.club](https://mast.dragon-fly.club/@holgerhuo)
