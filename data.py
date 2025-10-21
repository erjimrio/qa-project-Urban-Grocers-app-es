# Datos para crear usuario nuevo
headers = {
    "Content-Type": "application/json"
}

user_body = {
    "firstName": "Charly",
    "phone": "+11234112341",
    "address": "123 Elm Street, Hilltop"
}

# Datos para crear kit
kit_body = {
    "name": "Mi Kit Personal"
}

# ---------- Datos para la validación ----------

# Datos prueba 1

p1_kit_body = {
    "name": "a"
}

# Datos prueba 2
p2_kit_body = {
    "name": (
    "Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
    "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"
    )
}

# Datos prueba 3
p3_kit_body = {
    "name": ""
}

# Datos prueba 4
p4_kit_body = {
    "name": (
    "Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
    "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"
    )
}

# Datos prueba 5
p5_kit_body = {
    "name": "\"№%@\","
}

# Datos prueba 6
p6_kit_body = {
    "name": " A Aaa "
}

# Datos prueba 7
p7_kit_body = {
    "name": "123"
}

# Datos prueba 9
p9_kit_body = {
    "name": 123
}