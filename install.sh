#!/bin/sh
# Please run as normal user

PROJECT_NAME="hackathon"

# get options
while getopts ":d:n:" o; do
	case "${o}" in
		n)
			PROJECT_NAME="${OPTARG}"
			;;
		d)
			DOMAIN=$(OPTARG}
			;;
		*)
			echo "Wrong argument"
			exit 1
			;;
	esac
done

venvname=${PROJECT_NAME}venv

echo "Installing necessary packages..."

sudo apt update
sudo apt install nginx

sudo apt install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools
sudo apt install python3-venv

cd ~/$PROJECT_NAME
source $venvname/bin/activate

gunicorn --bind 0.0.0.0:5000 wsgi:app

deactivate

echo "Creating service ${PROJECT_NAME}.service"

sudo echo "[Unit]
Description=Gunicorn instance to serve $PROJECT_NAME
After=network.target

[Service]
User=$(whoami)
Group=www-data
WorkingDirectory=/home/$(whoami)/$PROJECT_NAME
Environment=\"PATH=/home/$(whoami)/$PROJECT_NAME/$venvname/bin\"
ExecStart=/home/$(whoami)/$venvname/bin/gunicorn --workers 3 --bind unix:${PROJECT_NAME}.sock -m 007 wsgi:app

[Install]
WantedBy=multi-user.target" > /etc/systemd/system/${PROJECT_NAME}.service

sudo systemctl start $PROJECT_NAME
sudo systemctl enable $PROJECT_NAME

if [ -z "$DOMAIN" ]; then
	echo "Server installation finished without domain."
	echo "You can access your website by http://<your-ip>"
	exit 0
fi

sudo echo "server {
	listen 80;
	server_name $DOMAIN www.${DOMAIN};

	location / {
		include proxy_params;
		proxy_pass http://unix:/home/$(whoami)/$PROJECT_NAME/${PROJECT_NAME}.sock;
	}
}" > /etc/nginx/sites-available/$PROJECT_NAME

sudo ln -s /etc/nginx/sites-available/$PROJECT_NAME /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx

sudo ufw delete allow 5000
sudo ufw allow 'Nginx Full'

sudo chmod 755 /home/$(whoami)

echo "Securing the Application"
sudo apt install python3-certbot-nginx

sudo certbot --nginx -d $DOMAIN -d www.$DOMAIN
sudo ufw delete allow 'Nginx HTTP'

echo "You can access your website by https://$DOMAIN"
