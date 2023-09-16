from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Análises Educacionais', 0, 1, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

pdf = PDF()
pdf.add_page()

pdf.chapter_title('Análise da Distribuição das Instituições de Ensino por Região')

pdf.chapter_body('A análise da distribuição das instituições de ensino por região é fundamental para entender como a oferta de educação superior está distribuída geograficamente no Brasil. Nesta seção, exploraremos a quantidade de instituições de ensino em cada região do país.')
pdf.chapter_body('Ao analisar o gráfico (imagem abaixo), podemos observar que a região Sudeste concentra a maior quantidade de instituições de ensino, seguida pelas regiões Nordeste e Sul. Por outro lado, as regiões Norte e Centro-Oeste têm uma presença menor de instituições de ensino. Essa distribuição reflete a densidade populacional e a infraestrutura educacional em diferentes partes do Brasil.')
pdf.image('contagem_regioes.png', x=15, y=pdf.get_y(), w=180)
pdf.ln(115)
pdf.chapter_body('A análise da distribuição das instituições de ensino por região nos fornece insights importantes sobre a disponibilidade de oportunidades educacionais no país. É essencial considerar essa distribuição ao planejar políticas educacionais e estratégias de expansão da oferta de ensino superior.')


pdf.chapter_title('Distribuição de Cursos por Modalidade')

pdf.chapter_body('A distribuição de cursos por modalidade, seja presencial ou a distância, é um aspecto crucial da educação superior. Nesta seção, investigaremos como os cursos estão distribuídos entre essas modalidades.')
pdf.chapter_body('Ao observar o gráfico (imagem abaixo), fica evidente que a maioria dos cursos está na modalidade a distância (Educação a Distância). Isso pode refletir uma tendência crescente de cursos on-line e a flexibilidade que essa modalidade oferece aos estudantes.')
pdf.image('contagem_modalidade.png', x=15, y=pdf.get_y(), w=180)
pdf.ln(130)
pdf.chapter_body('A predominância de cursos a distância destaca a importância da educação on-line como uma alternativa viável para atender às necessidades educacionais da população, especialmente em um cenário de mudanças tecnológicas e sociais.')


pdf.chapter_title('Quantidade de Cursos por Categoria Administrativa')

pdf.chapter_body('A categoria administrativa das instituições de ensino é um fator relevante na análise do cenário educacional. Nesta seção, exploraremos a quantidade de cursos por categoria administrativa.')
pdf.chapter_body('O gráfico (imagem abaixo) mostra que a maioria dos cursos é oferecida por instituições de ensino privadas com fins lucrativos, seguidas pelas instituições públicas e privadas sem fins lucrativos. Isso reflete a diversidade de tipos de instituições de ensino no Brasil.')
pdf.image('contagem_categoria.png', x=15, y=pdf.get_y(), w=180)
pdf.ln(120)
pdf.chapter_body('A variedade de categorias administrativas das instituições de ensino demonstra a importância da colaboração público-privada na oferta de cursos e a diversidade de opções disponíveis para os estudantes.')


pdf.chapter_title('Cursos por Grau')

pdf.chapter_body('O grau dos cursos (Bacharelado, Licenciatura, Tecnológico, etc.) é um fator relevante na escolha de uma formação acadêmica. Nesta seção, exploraremos a distribuição de cursos por grau.')
pdf.chapter_body('Ao analisar o gráfico (imagem abaixo), observamos que a maioria dos cursos é de Bacharelado, seguidos por Tecnológico e Licenciatura. Essa distribuição reflete as preferências dos estudantes e as necessidades do mercado de trabalho.')
pdf.image('contagem_grau.png', x=15, y=pdf.get_y(), w=180)
pdf.ln(110)
pdf.chapter_body('A predominância de cursos de Bacharelado sugere a busca por formações mais amplas e abrangentes, enquanto os cursos Tecnológicos atendem a demandas específicas do mercado de trabalho.')


pdf.chapter_title('Distribuição de Vagas Autorizadas por Curso')

pdf.chapter_body('A distribuição de vagas autorizadas por curso é importante para entender a oferta de oportunidades educacionais. Nesta seção, analisaremos como as vagas são distribuídas entre os cursos.')
pdf.chapter_body('O gráfico (imagem abaixo) destaca a quantidade de vagas autorizadas em diferentes cursos. Isso é essencial para estudantes que desejam escolher cursos com maior disponibilidade de vagas.')
pdf.image('vagas_por_grupo.png', x=15, y=pdf.get_y(), w=180)
pdf.ln(100)
pdf.chapter_body('A análise da distribuição de vagas autorizadas ajuda a identificar cursos que têm uma oferta significativa de vagas, fornecendo informações valiosas para orientar escolhas educacionais.')


pdf.chapter_title('Cursos por Área de Conhecimento (OCDE CINE)')

pdf.chapter_body('A classificação por área de conhecimento (OCDE CINE) é relevante para analisar a diversidade de cursos disponíveis. Nesta seção, exploraremos a quantidade de cursos por área de conhecimento.')
pdf.chapter_body('O gráfico (imagem abaixo) apresenta as áreas de conhecimento mais comuns entre os cursos. Isso reflete a variedade de disciplinas acadêmicas oferecidas pelas instituições de ensino.')
pdf.add_page()
pdf.image('contagem_area_conhecimento.png', x=15, y=pdf.get_y(), w=180)
pdf.ln(110)
pdf.chapter_body('A diversidade de áreas de conhecimento disponíveis permite que os estudantes escolham cursos que correspondam aos seus interesses e objetivos de carreira.')


pdf.chapter_title('Instituições com Mais Cursos')

pdf.chapter_body('Identificar as instituições de ensino com mais cursos é importante para entender o cenário educacional. Nesta seção, analisaremos as instituições com a maior oferta de cursos.')
pdf.chapter_body('O gráfico (imagem abaixo) destaca as 10 instituições com o maior número de cursos. Isso demonstra a diversidade de opções educacionais oferecidas por essas instituições.')
pdf.add_page()
pdf.image('contagem_instituicoes.png', x=15, y=pdf.get_y(), w=180)
pdf.ln(100)
pdf.chapter_body('A presença de várias instituições com uma ampla oferta de cursos é um indicativo da importância da competição e da qualidade na educação superior.')


pdf.chapter_title('Conclusão Geral')

pdf.chapter_body('A análise do cenário educacional abordou diversos aspectos, desde a distribuição geográfica das instituições até a diversidade de cursos e modalidades oferecidas. Essas informações são valiosas para estudantes, educadores e formuladores de políticas educacionais, pois auxiliam na tomada de decisões informadas sobre o futuro da educação superior no Brasil.')
pdf.chapter_body('Nossas análises e gráficos destacaram a importância da diversidade e da acessibilidade na oferta de cursos, bem como a necessidade contínua de adaptação às demandas do mercado e às preferências dos estudantes.')

pdf.output('analises_educacionais.pdf')