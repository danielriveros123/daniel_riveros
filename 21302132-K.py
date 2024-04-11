# Definir las VLANs para Switch1
switch1_native_vlan = 99
switch1_vlans = [10, 20, 30]

# Definir las VLANs para Switch2
switch2_native_vlan = 200
switch2_vlans = [40, 50, 60]

# Comparar la VLAN nativa de Switch1 con la VLAN en Switch1
if switch1_native_vlan == switch1_vlans[0]:
    print("Las VLANs en Switch1 son iguales y cumplen con el requerimiento")
else:
    print("Las VLANs en Switch1 son diferentes y no cumplen con el requerimiento")

# Comparar las VLANs en Switch1 con un conjunto específico
if set(switch1_vlans) == {10, 100, 30}:
    print("Las VLANs en Switch1 son iguales y cumplen con el requerimiento")
else:
    print("Las VLANs en Switch1 son diferentes y no cumplen con el requerimiento")

# Comparar la VLAN nativa de Switch2 con la VLAN en Switch2
if switch2_native_vlan == switch2_vlans[0]:
    print("Las VLANs en Switch2 son iguales y cumplen con el requerimiento")
else:
    print("Las VLANs en Switch2 son diferentes y no cumplen con el requerimiento")

# Comparar las VLANs en Switch2 con un conjunto específico
if set(switch2_vlans) == {40, 50, 60}:
    print("Las VLANs en Switch2 son iguales y cumplen con el requerimiento")
else:
    print("Las VLANs en Switch2 son diferentes y no cumplen con el requerimiento")
