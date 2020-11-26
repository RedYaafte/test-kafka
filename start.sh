# Create virtual env if not exist.
if [ ! -d "/code/venv" ]; then
  echo "Creating virtual env..."
  python3 -m venv venv
fi

echo "env activation"

echo "===>  UPDATE  <==="
apt update -y
echo "===>  install java  <==="
apt install default-jre -y
java -version

source venv/bin/activate
echo "Installing requirements..."
pip install -r requirements.txt
echo "Runing migrations..."
./manage.py migrate
echo "Starting on port $APP_PORT..."
./manage.py runserver 0:$APP_PORT

