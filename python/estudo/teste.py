import os
import streamlit as st
import streamlit.components.v1 as components
from gtts import gTTS
import io
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import make_pipeline
# Biblioteca para o microfone
from streamlit_mic_recorder import mic_recorder

# --- CONFIGURAÇÕES ---
st.set_page_config(page_title="PWD ACESSIBILIDADE | Petrobras", page_icon="💚", layout="wide")

@st.cache_resource 
def treinar_ia():
    textos = ["rampa", "cadeira", "cego", "surdo", "libras", "braço", "perna", "visão", "escada", "auditório"]
    cats = ["Física", "Física", "Visual", "Auditiva", "Auditiva", "Motora", "Motora", "Visual", "Física", "Física"]
    modelo = make_pipeline(TfidfVectorizer(), MLPClassifier(max_iter=1000, random_state=42))
    modelo.fit(textos, cats)
    return modelo

ia_acessibilidade = treinar_ia()

if 'escolha' not in st.session_state:
    st.session_state.escolha = None

def gerar_audio(texto):
    tts = gTTS(text=texto, lang='pt')
    fp = io.BytesIO()
    tts.write_to_fp(fp)
    return fp

# --- INTERFACE ---
st.title("💚 PWD ACESSIBILIDADE - Petrobras")
st.subheader("Selecione sua categoria:")

cols = st.columns(5)
categorias = ["Visual", "Auditiva", "Física", "Motora", "Outra"]
icones = ["👁️", "👂", "♿", "🧠", "❓"]

for i, cat in enumerate(categorias):
    with cols[i]:
        if st.button(f"{icones[i]} {cat.upper()}", use_container_width=True):
            st.session_state.escolha = cat

st.divider()

if st.session_state.escolha:
    st.info(f"Categoria ativa: **{st.session_state.escolha}**")
    
    # --- ÁUDIO GUIA (APENAS PARA VISUAL) ---
    if st.session_state.escolha == "Visual":
        st.audio(gerar_audio("Categoria visual selecionada. Use o botão de microfone abaixo para gravar sua denúncia."), autoplay=True)

    # --- ÁREA DE DENÚNCIA (TEXTO + MICROFONE) ---
    col_txt, col_mic = st.columns([2, 1])
    
    with col_txt:
        texto_denuncia = st.text_area("Descreva sua necessidade (ou grave ao lado):", height=150)
    
    with col_mic:
        st.write("🎤 **Gravar por Voz**")
        # O botão de microfone fica disponível para todos, mas é essencial para Física/Motora/Visual
        audio_data = mic_recorder(
            start_prompt="Clique para Falar 🎙️",
            stop_prompt="Parar Gravação ⏹️",
            key='recorder'
        )
        if audio_data:
            st.success("✅ Áudio capturado com sucesso!")

    if st.button("ENVIAR FORMULÁRIO 🚀", use_container_width=True):
        # Lógica de validação: precisa de texto OU áudio
        if texto_denuncia or audio_data:
            if st.session_state.escolha == "Outra" and texto_denuncia:
                final = ia_acessibilidade.predict([texto_denuncia])[0]
            else:
                final = st.session_state.escolha
            
            st.success(f"Denúncia enviada! Categoria registrada: {final}")
            
            if st.session_state.escolha == "Visual":
                st.audio(gerar_audio("Sua denúncia foi enviada com sucesso."), autoplay=True)
                
            if st.button("Nova Solicitação"):
                st.session_state.escolha = None
                st.rerun()
        else:
            st.error("Por favor, digite sua denúncia ou grave um áudio antes de enviar.")

# VLIBRAS
with st.sidebar:
    st.write("🤟 Suporte em Libras")
    components.html('<div vw class="enabled"><div vw-access-button class="active"></div><div vw-plugin-wrapper><div class="vw-plugin-top-wrapper"></div></div></div><script src="https://vlibras.gov.br/app/vlibras-plugin.js"></script><script>new window.VLibras.Widget("https://vlibras.gov.br/app");</script>')

# ==========================================
# BLOCO DE ACESSIBILIDADE VISUAL CORRIGIDO
# ==========================================
st.sidebar.subheader("⚙️ Ajustes de Visibilidade")

modo_leitura = st.sidebar.checkbox("📖 Letras Maiores")
alto_contraste = st.sidebar.checkbox("👁️ Modo Escuro / Alto Contraste")

estilos_customizados = ""

if modo_leitura:
    estilos_customizados += """
    <style>
        html, body, [class*="st-"], p, div, input, button, textarea, label, span {
            font-size: 26px !important;
        }
    </style>
    """

if alto_contraste:
    estilos_customizados += """
    <style>
        /* Fundo principal e textos globais */
        .stApp, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
            background-color: #000000 !important;
            color: #FFFF00 !important;
        }
        
        /* Forçar cor de todos os textos, títulos e labels */
        h1, h2, h3, h4, p, label, span, stMarkdown, .stWidgetLabel {
            color: #FFFF00 !important;
        }

        /* Ajuste dos Botões das Categorias */
        .stButton>button {
            background-color: #111111 !important;
            color: #FFFF00 !important;
            border: 2px solid #FFFF00 !important;
            border-radius: 10px;
        }

        /* Ajuste das caixas de texto (Inputs) */
        textarea, input {
            background-color: #222222 !important;
            color: #FFFF00 !important;
            border: 2px solid #FFFF00 !important;
        }

        /* Sidebar (Barra Lateral) no modo escuro */
        [data-testid="stSidebar"] {
            background-color: #111111 !important;
            border-right: 1px solid #FFFF00;
        }
        [data-testid="stSidebar"] * {
            color: #FFFF00 !important;
        }
    </style>
    """

if estilos_customizados:
    st.markdown(estilos_customizados, unsafe_allow_html=True)
    
# Verificação da Logo
if os.path.exists("logo.webp"):
    st.sidebar.image("logo.webp", use_container_width=True)
else:
    st.sidebar.error("❌ Arquivo 'logo.png' não encontrado na pasta.")