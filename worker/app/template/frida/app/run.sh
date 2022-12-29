adb connect android:5555
wget -O /tmp/a.apk $APK_URL
adb -s android:5555 install -t -g /tmp/a.apk

python3 main.py
python3 fridadown.py
sleep 1h