import mqtt_pub

def coin_callback(p):
    if p.value()==0:
        mqtt_pub.pub("1")  
        coin_count = coin_count + 1
        print('pin_coin change', p.value(), "total money", coin_count)