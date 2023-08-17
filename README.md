# enumerate_user_from_password

Two flask servers, one that shows if the user is in the user name list the other doesnt.

Used as an example of why basic things can have a big effect.

## Install

```bash
sudo apt update
sudo apt install python3-pip
sudo apt install python3-venv
```

todo
[ ] write bit about installing from git

### nginx

```bash 

sudo apt install nginx
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx

sudo nano /etc/nginx/sites-available/default
```
in nano add the bits for your IP URL
```
server {
    listen 80;
    server_name yourdomain.com;  # replace with your domain name

    location / {
        proxy_pass http://127.0.0.1:5000;  # assuming your Flask app is running on port 5000
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }


```
cnrol x

```bash
sudo systemctl reload nginx
```
