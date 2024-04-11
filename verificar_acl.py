def verificar_tipo_acl(numero_acl):
    # Verificar si el número de ACL está en el rango de ACL Estándar (1-99)
    if 1 <= numero_acl <= 99:
        return "ACL Estándar"
    # Verificar si el número de ACL está en el rango de ACL Extendida (100-199)
    elif 100 <= numero_acl <= 199:
        return "ACL Extendida"
    else:
        return "El número no corresponde a una lista de acceso"


def main():
    try:
        # Solicitar al usuario que ingrese el número de ACL IPv4
        numero_acl = int(input("Ingrese el número de ACL IPv4: "))
        # Verificar el tipo de ACL y mostrar el resultado
        tipo_acl = verificar_tipo_acl(numero_acl)
        print(f"El número de ACL {numero_acl} corresponde a una {tipo_acl}.")
    except ValueError:
        print("Error: Por favor, ingrese un número válido.")


if __name__ == "__main__":
    main()
