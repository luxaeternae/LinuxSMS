echo "Running Set up"

sudo apt-get install python
sudo apt-get install python-gobject
sudo apt-get install libnotify-bin
sudo apt-get install libnotify-dev

python first-time-setup.py
sudo mv setupvars.txt vars.py
mkdir contacts
