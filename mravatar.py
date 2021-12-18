from flask import Flask, redirect, request, render_template, Response
from requests_cache import CachedSession
import requests_cache
import json
import re

app = Flask(__name__)

# Setup Requests Cache
persistent = CachedSession(
    'persistent', 
    backend='sqlite', 
    allowable_methods=['GET'],
    allowable_codes=[200],
    stale_if_error=True,
    )

session = CachedSession(
    'cache', 
    backend='sqlite',
    expire_after=10800,
    allowable_methods=['GET'],
    allowable_codes=[200],
    stale_if_error=True,
)

# /avatar/<user> entrypoint
@app.route("/avatar/<user>")
def req_avatar(user):
    # Validate Username
    if re.search('@[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+',user):
        webfinger_url = "https://"+re.split('@',user[1:])[1]+"/.well-known/webfinger?resource=acct:"+user[1:]
    elif re.search('[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+',user):
        webfinger_url = "https://"+re.split('@',user)[1]+"/.well-known/webfinger?resource=acct:"+user
    else:
        app.logger.error("%s is invalid.", user)
        return render_template('invalid.html', user=user), 400
    
    # Find account url
    try:
        webfinger = persistent.get(webfinger_url)
    except Exception as e:
        app.logger.error("%s is not accessable.", webfinger_url)
        return render_template('inaccessible.html', url=webfinger_url), 400
    
    if webfinger.ok:
        user_url = json.loads(webfinger.text)['aliases'][1]+".json"
    else: 
        app.logger.error("%s is not accessable.", webfinger_url)
        return render_template('inaccessible.html', url=webfinger_url), 400

    if request.args.get('no-cache') == 'true':
        requests_cache.backends.sqlite.SQLiteCache(db_path='cache').delete_url(user_url, method='GET')
        
    # Get User Info
    try:
        user_json = session.get(user_url)
    except Exception as e:
        app.logger.error("%s is not accessable.", user_url)
        return render_template('inaccessible.html', url=user_url), 400
    
    if user_json.ok:
        if "icon" in json.loads(user_json.text):
            img_url = json.loads(user_json.text)['icon']['url']
        else:
            img_url = "https://cdn.jsdelivr.net/gh/mastodon/mastodon@latest/public/avatars/original/missing.png"
    else:
        app.logger.error("%s is not accessable.", user_url)
        return render_template('inaccessible.html', url=user_url), 400
    
    # Proxy Images
    if request.args.get('proxied') == 'true':
        if request.args.get('no-cache') == 'true':
            requests_cache.backends.sqlite.SQLiteCache(db_path='cache').delete_url(img_url, method='GET')
        try: 
            img_resp = session.get(
                img_url, 
                headers={'Accept': request.headers['Accept']}
            )
        except Exception as e:
            app.logger.error("%s inaccessable.", img_url)
            return redirect(img_url, code=302)
        
        if img_resp.ok:
            img = Response(img_resp.content, img_resp.status_code, {'Content-Type': img_resp.headers['Content-Type'], 'Cache-Control': 'max-age=3600'})
            return img
        else:
            app.logger.error("%s inaccessable.", img_url)
            return redirect(img_url, code=302)

    else:
        return redirect(img_url, code=302)