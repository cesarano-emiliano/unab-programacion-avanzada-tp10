"""
Ejercicio 2: Patrón Estructural 
"""

class ModernXMLReport:
    """La interfaz moderna espera datos estructurados en XML."""
    def generate_xml_report(self) -> str:
        return "<report><status>success</status><records>45</records></report>"


class LegacyPHPService:
    """El servicio viejo que devuelve un formato distinto (JSON plano)."""
    def fetch_legacy_json(self) -> str:
        return '{"estado": "exito", "registros": 45}'


class PHPToXMLAdapter(ModernXMLReport):
    """El Adaptador convierte la salida del formato viejo al formato esperado."""
    def __init__(self, legacy_service: LegacyPHPService):
        self.legacy_service = legacy_service

    def generate_xml_report(self) -> str:
        # Consumimos el servicio incompatible
        legacy_data = self.legacy_service.fetch_legacy_json()
        print(f"[Adaptador] Transformando: {legacy_data}")
        
        # En producción se parsearía el JSON y se armaría el árbol XML
        return "<report><status>success</status><records>45</records></report>"


# --- Ejemplo Concreto de Uso ---
if __name__ == "__main__":
    print("\n=== TEST PATRÓN ADAPTER ===")
    
    # El sistema heredado incompatible
    servicio_viejo = LegacyPHPService()
    
    # Instanciamos el adaptador envolviendo el servicio viejo
    adaptador = PHPToXMLAdapter(servicio_viejo)
    
    # El cliente consume el reporte de manera usando la interfaz moderna
    resultado_final = adaptador.generate_xml_report()
    print(f"Resultado final obtenido:\n{resultado_final}")