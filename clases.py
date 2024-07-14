class Producto:
    # Información básica del producto
    def __init__(self, product_name, product_code, product_category, product_type, product_brand, product_supplier, product_description):
        self.product_name = product_name
        self.product_code = product_code
        self.product_category = product_category
        self.product_type = product_type
        self.product_brand = product_brand
        self.product_supplier = product_supplier
        self.product_description = product_description

        # Inicializar categorías con valores predeterminados o nulos
        self.inventario = None
        self.precios = None
        self.detalles_adicionales = None

    # Inventario del producto
    def establecer_inventario(self, product_quantity, product_min_quantity, product_max_quantity, product_sold_quantity, product_bought_quantity, product_status):
        self.inventario = {
            "cantidad": product_quantity,
            "cantidad_minima": product_min_quantity,
            "cantidad_maxima": product_max_quantity,
            "cantidad_vendida": product_sold_quantity,
            "cantidad_comprada": product_bought_quantity,
            "estado": product_status
        }
    
    def obtener_inventario(self):
        return self.inventario

    # Precios del producto
    def establecer_precios(self, product_price, product_purchase_price, product_sale_price):
        self.precios = {
            "precio": product_price,
            "precio_compra": product_purchase_price,
            "precio_venta": product_sale_price
        }
    
    def obtener_precios(self):
        return self.precios

    # Detalles adicionales del producto
    def establecer_detalles_adicionales(self, product_expiration, product_location, product_purchase_date, product_size, product_color, product_weight):
        self.detalles_adicionales = {
            "fecha_vencimiento": product_expiration,
            "ubicacion": product_location,
            "fecha_compra": product_purchase_date,
            "tamaño": product_size,
            "color": product_color,
            "peso": product_weight
        }
    
    def obtener_detalles_adicionales(self):
        return self.detalles_adicionales
    
    def a_diccionario(self):
        return {
            "informacion_basica": {
                "nombre": self.product_name,
                "codigo": self.product_code,
                "categoria": self.product_category,
                "tipo": self.product_type,
                "marca": self.product_brand,
                "proveedor": self.product_supplier,
                "descripcion": self.product_description
            },
            "inventario": self.inventario if self.inventario else {},
            "precios": self.precios if self.precios else {},
            "detalles_adicionales": self.detalles_adicionales if self.detalles_adicionales else {}
        }