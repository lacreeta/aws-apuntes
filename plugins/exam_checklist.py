"""Plugin para agregar checklist de examen automáticamente"""
from mkdocs.plugins import BasePlugin
import re

class ExamChecklistPlugin(BasePlugin):
    
    def on_page_markdown(self, markdown, page, config, files):
        # Agregar checklist automáticamente a páginas de servicios
        if any(folder in page.file.src_path for folder in ['compute/', 'storage/', 'security/']):
            checklist = """
---

!!! success "Checklist para el Examen"
    - [ ] Entiendo qué es este servicio
    - [ ] Conozco sus casos de uso principales
    - [ ] Sé cuándo NO usarlo
    - [ ] Comprendo el modelo de precios básico
"""
            markdown += checklist
        
        return markdown