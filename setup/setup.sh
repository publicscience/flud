# Get ready
sudo apt-get update && sudo apt-get upgrade

# Packages
sudo apt-get install nginx python3-pip git uwsgi supervisor uwsgi-plugin-python uwsgi-plugin-python3 ruby

# Virtualenv
pip3 install virtualenv
virtualenv -p python2.7 /env/glimpse --no-site-packages

# Sass
gem install sass

# Setup app
git clone https://github.com/publicscience/glimpse.git /srv/glimpse
cd /srv/glimpse
mv config-sample.py config.py
source /env/glimpse/bin/activate
pip install -r requirements.txt

# Supervisor
sudo cp /srv/glimpse/setup/supervisor/*.conf /etc/supervisor/conf.d/

# Nginx
sudo sed -i '' 's/# server_names_hash_bucket_size/server_names_hash_bucket_size/g' /etc/nginx/nginx.conf
sudo cp /srv/glimpse/setup/nginx/*.conf /etc/nginx/conf.d/

# Restart
sudo service nginx restart
sudo service supervisor restart

# Warning
echo -e "\n\nYou should edit /srv/glimpse/config.py for your settings, then restart supervisor.\n\n"
