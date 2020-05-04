apt install -y python3 python3-pip

pip3 install flask xmltodict ujson requests gunicorn Flask-WeasyPrint WeasyPrint

apt update && apt full-upgrade -y
apt install -y python3-pip
apt install -y python3-flask libcairo2 libglib2.0-0
apt install -y build-essential python3-dev python3-pip python3-setuptools python3-wheel python3-cffi libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info
pip3 install flask xmltodict ujson requests gunicorn