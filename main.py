import streamlit as st

Home = st.Page("classes/home.py", title="🏠 Home", default=True)
dAlunos = st.Page("navigation_apps/update_db.py", title="🗃️ Alunos e Olimpíadas")
dEntrevistas = st.Page("navigation_apps/update_entrevistas.py", title="🎤 Entrevistas")
tutorial = st.Page("navigation_apps/tutorial.py", title="📚 Como usar")
add_new_data = st.Page("navigation_apps/add_new_data_db.py", title="📂 Adicionar novas olimpíadas")

pg = st.navigation(
    {
        "Início": [Home],
        "Instruções de uso": [tutorial],
        "Atualizar databases": [dAlunos, dEntrevistas, add_new_data],
    }
)
pg.run()