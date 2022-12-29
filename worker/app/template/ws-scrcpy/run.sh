A=`adb connect android:5555`
while printf '%s\n' "$A" | grep -Fqe "Connection refused";  do  
    echo $A sleep 5
    sleep 5
    A=`adb connect android:5555`
done
adb root
npm start