import os
import streamlit as st
import base64
def head():
    """
    Displays the header and the logo of the application
    """
    st.set_page_config(page_title="Como usar?", page_icon="📖")
    with open('./utils/front.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    try:
        with open('./utils/logo_jr.png', 'rb') as logo_file:
            logo_base64 = base64.b64encode(logo_file.read()).decode('utf-8')
            st.markdown(f'<p align="center"><img src="data:image/png;base64,{logo_base64}" width="500"></p>', unsafe_allow_html=True)
    except FileNotFoundError:
        st.error("Logo file not found")


    st.markdown("""
        <h3 style='text-align: center;'>Instruções de Atualização de Dados <br> Alunos e Olimpíadas</h3>
        <ol>
            <li>
                Na barra lateral à esquerda, você encontrará duas opções de atualização para diferentes bancos de dados:
                <ul>
                    <li>
                        <strong>Alunos e Olimpíadas</strong>: refere-se aos bancos de dados que contêm informações relacionadas a ambos, como gênero, LinkedIn, escola, cidade, medalha, série, entre outras.
                        <br>Para escolher essa opção, clique nela e a página do formulário de atualização será aberta em seguida.
                    </li>
                </ul>
            </li>
            <li>
                Em primeiro lugar, escolha qual banco de dados você deseja modificar:
                <ul>
                    <li><strong>Alunos</strong>: para modificar gênero, LinkedIn e bio do LinkedIn.</li>
                    <li><strong>Olimpíadas</strong>: para modificar escola, cidade, estado, medalha, série, ano, entre outros.</li>
                </ul>
            </li>
            <li>
                Preencha o campo com o nome completo do aluno. Caso ocorra algum erro de digitação, serão sugeridos 3 nomes que mais se assemelham ao digitado.
            </li>
            <li>
                Selecione o campo que deseja editar nos dados do aluno. Para modificar mais de um campo, basta fazer um de cada vez. Exemplo:
                <ul>
                    <li>
                        Para editar tanto o gênero quanto o LinkedIn do aluno:
                        <ul>
                            <li>Após digitar o nome completo e o aluno ser encontrado, escolha o campo "Gênero" para editar e insira o novo valor.</li>
                            <li>Clique em “Atualizar aluno”. Uma mensagem confirmando o sucesso da operação aparecerá.</li>
                            <li>Em seguida, selecione o campo "LinkedIn", insira o novo valor e clique novamente em “Atualizar aluno”.</li>
                        </ul>
                    </li>
                </ul>
            </li>
            <li>
                Ao finalizar todas as operações, clique em “Salvar” para que as alterações sejam registradas no banco de dados.
            </li>
        </ol>
    """, unsafe_allow_html=True)


head()


