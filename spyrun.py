import os

def create_wifi_network(ssid, password):
    # WiFi ağı oluşturulacak ara yüzü kapat
    os.system("netsh wlan stop hostednetwork")

    # WiFi ağını oluştur
    os.system(f"netsh wlan set hostednetwork mode=allow ssid={ssid} key={password}")
    
    # WiFi ağını başlat
    os.system("netsh wlan start hostednetwork")

if __name__ == "__main__":
    # WiFi ağı bilgilerini belirtin
    ssid = "MyWiFiNetwork"
    password = "MyPassword"

    # WiFi ağı oluştur
    create_wifi_network(ssid, password)
