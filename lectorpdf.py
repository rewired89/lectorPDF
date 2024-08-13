import openai
import PyPDF2

# Configura tu clave API de OpenAI
openai.api_key = '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'

# Función para extraer texto de un documento PDF
def extraer_texto_pdf(ruta_pdf):
    with open(ruta_pdf, 'rb') as archivo:
        lector_pdf = PyPDF2.PdfReader(archivo)
        texto_completo = "" 
        for pagina in range(len(lector_pdf.pages)):
            texto_completo += lector_pdf.pages[pagina].extract_text()
    return texto_completo

# Función para obtener respuesta de OpenAI utilizando la nueva API
def obtener_respuesta_openai(texto, palabras_clave):
    prompt = f"Extrae la información relevante sobre las siguientes palabras clave: {palabras_clave}\n\nTexto:\n{texto}"
    try:
        respuesta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Eres un asistente útil."},
                {"role": "user", "content": prompt}
            ]
        )
        return respuesta['choices'][0]['message']['content'].strip()
    except Exception as e:
        print("Ocurrió un error:", e)
        return None

# Ejemplo de uso
ruta_pdf = 'mi_documento.pdf'  # Aquí debes poner la ruta correcta al archivo PDF
texto = extraer_texto_pdf(ruta_pdf)
palabras_clave = "income, spending, invest"

respuesta = obtener_respuesta_openai(texto, palabras_clave)
if respuesta:
    print(respuesta)
else:
    print("No se pudo obtener una respuesta de OpenAI.")
