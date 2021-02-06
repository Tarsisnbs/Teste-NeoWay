
# Teste-NeoWay
Coleta de dados do site dos correios
<p>Este software tem por finalidade extrair automaticamnte os CEPs das Localidades de todos os estados brasileiros atrav&eacute;s do link: <a href="http://www.buscacep.correios.com.br/sistemas/buscacep/buscaFaixaCep.cfm">http://www.buscacep.correios.com.br/sistemas/buscacep/buscaFaixaCep.cfm </a></p>
<p>e gravar em arquivos JSONL (um para cada estado) contendo os campos: "localidade", "faixa de cep" e "id".</p>
<h2>Funcionamento</h2>
<h4>O Sistema de busca do site</h4>
<p><strong>I -</strong> Os dados relativos aos CEPs s&atilde;o classificados por UFs, que s&atilde;o usadas como chaves de entrada de uma elemento do tipo "select".&nbsp;</p>
<p><strong>II -</strong> Ao clicar no bot&atilde;o relativo a busca, &eacute; exibida uma tabela com os dados categorizados em 4 colunas (Localidade, Faixa de CEP, Situa&ccedil;&atilde;o, Tipo de Faixa).</p>
<p><strong>III -</strong> Existe um limite de 50 linhas da tabela exibidas na p&aacute;gina, sendo necess&aacute;rio requerir os pr&oacute;ximos dados clicando no link de texto "<span style="color: #0000ff;"><span style="text-decoration: underline;">pr&oacute;xima</span></span>".&nbsp;</p>
<p><strong>IV -</strong> Para realizar uma busca em outra UF, basta clicar no link de texto "<span style="color: #0000ff;"><span style="text-decoration: underline;">Nova Consulta</span></span>" para repetir o processo apartir do item <strong>I</strong>.</p>
<p><strong>A Coleta de dados&nbsp;</strong></p>
<p>Para buscar os dados de todas as UFs no software, foi criada uma lista "<em>UF_list</em>" correspondente ao conjuto das chaves de entrada do elemento "select". A busca &eacute; feita indexando a "UF_list" e aplicando na entrada de "select" usando o m&eacute;todo "<em>uf_acess_data(self, uf)".</em></p>
<p>J&aacute; na tabela, s&atilde;o coletados todos os dados da tabela e armazenados na estrutura&nbsp; "<em>dataframe"</em>, caso existam mais que 50 linhas na tabela, os pr&oacute;ximos dados s&atilde;o acessados pelo link de texto "<span style="color: #0000ff;"><span style="text-decoration: underline;">pr&oacute;xima</span></span>" e armazenados em "<em>dataframe"</em> at&eacute; o respectivo link estar inativo, indicando fim dos dados.&nbsp;Para cada vez que os dados s&atilde;o gravados em "<em>dataframe",&nbsp;</em>&eacute; feito uma filtragem nas colunas, mantendo apenas "Faixa de CEP" e "Localidade". Tamb&eacute;m &eacute; gerado um ID para cada linha da tabela gravada em "<em>dataframe".&nbsp;</em>Todo este processo &eacute; implementado no m&eacute;todo "<em>uf_get_data_records(self)".</em></p>
<p>Caso o link de texto "<span style="color: #0000ff;"><span style="text-decoration: underline;">pr&oacute;xima</span></span>" estar indisp&oacute;nivel em dado momento, ap&oacute;s o registro dos dados exibidos, o software acessa o link de texto "<span style="color: #0000ff;"><span style="text-decoration: underline;">Nova Consulta</span></span>" e grava o conjunto "<em>dataframe" </em>em um arquivo JSONL com o m&eacute;todo <em>"dump_file_json(self, records, file_name)".</em></p>
<p>Ap&oacute;s gravar o arquivo, &eacute; verificado se existem elementos em "<em>UF_list</em>" a serem buscados, caso verdadeiro, o pr&oacute;ximo elemento da lista &eacute; empregado na entrada do elemento "select" da p&aacute;gina de busca, caso contr&aacute;rio, o programa &eacute; encerrado.</p>
<p>Os elementos do c&oacute;digo fonte HTML s&atilde;o acessados usando a API Selenium Python, e formatados com beautifulsoup4 e pandas. A grava&ccedil;&atilde;o do arquivo &aacute; feita usando a API jsonlines.py &nbsp;</p>
<h2>Requerimentos Para Executar</h2>
<p>Python: v = 3.64</p>
<p>APIs Python:&nbsp;</p>
<p>{pandas: v = 1.0.1,</p>
<p>beautifulsoup4: v = 4.8.2,</p>
<p>selenium: v = 3.141.0</p>
<div>
<div>jsonlines: v = 2.0.0}</div>
</div>
<p>WebDriver - Chrome: v = 89.04 (<a href="https://chromedriver.chromium.org/downloads">https://chromedriver.chromium.org/downloads</a>)</p>
<p>Obs: Os resultados podem ser verificados executando o .py e comparando os arquivos JSONL com os dados das UFs do site dos correios, (n&uacute;mero de campos correspondendo as colunas desejadas da tabela e n&uacute;mero de linhas ao n&uacute;mero de localidades)</p>
<p><strong>&nbsp;</strong></p>
