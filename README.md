
# Teste-NeoWay
Coleta de dados do site dos correios
<p>Este software tem por finalidade extrair automaticamnte os CEPs das Localidades de todos os estados brasileiros atrav&eacute;s do link: <a href="http://www.buscacep.correios.com.br/sistemas/buscacep/buscaFaixaCep.cfm">http://www.buscacep.correios.com.br/sistemas/buscacep/buscaFaixaCep.cfm </a></p>
<p>e gravar em arquivos JSONL (um para cada estado) contendo os campos: "localidade", "faixa de cep" e "id".</p>
### Melhorias

Para Facilitar a testagem do código durante a implementação dividiu-se o processo em **subprocessos**, de acordo com as dependências externas necessárias.

	*O processo de teste de cada subprocesso é feito usando arquivos de entrada e saída, de forma que para testar o subprocesso B, por exemplo, pode-se usar os dados de saída do subprocesso A em sua entrada, porém não é obrigatório.*

A comunicação com o servidor é feita usando **requisições** HTTP da biblioteca requests.py.

	*Na versão anterior era utilizada a api Selenium, que usava o Browser para comunicação com o servidor, isso era demasiadamente lento e complexo.*

Por fim, Foram adicionados alguns diagramas para melhor compreensão da arquitetura e fluxo do software.

### Segmentação do Processo
 Os subprocessos foram definidos como:
 
###### Requerimento dos dados: 

São feitas requisições http para obter o conteúdo da página com os dados desejados. 

![Request_test](https://user-images.githubusercontent.com/56703046/171811746-eec1936a-2f0b-4368-85bb-5c9107919d7f.jpg)

	Arquivo principal: RequestData.py
	Arquivo de teste: test_RequestData.py
	Arquivos I/O :  nenhum /  request_response.txt*

###### Extração dos dados: 

São extraídos dados de uma string de entrada correspondente a página html que se deseja fazer a extração. Note, que nesta etapa os dados de saída ainda estão em formato xml.

![Extract_test](https://user-images.githubusercontent.com/56703046/171811690-caa4d718-ee1d-4378-b343-161438afcf93.jpg)

	Arquivo principal:ExtractData.py
	Arquivo de teste: test_ExtractData.py
	Arquivos I/O :  request_response.txt /  table_html.html (*redundancia com a extensão)

 ###### Tratamento e Escrita dos Dados: 

A partir de um conjunto de dados e metadados formatodos em xml (neste caso uma tabela <tb>), gera-se estruturas de lista de dicionários com as informações e relações correspondentes. Também é adicionado um ID para cada linha da tabela ou posição da lista. 

> Obs: *A Escrita de dados inicialmente fora definita como um subprocesso a mais, porém devido a redução de complexidade aglutinou-se os dois subprocessos em um só. *

  ![CleanData_test](https://user-images.githubusercontent.com/56703046/171811370-6bcc4905-c2ea-48bd-8b1e-4719efcd6e1a.jpeg)
  
	Arquivo principal: CleanData.py 
	Arquivo de teste: test_CleanData.py
	Arquivos I/O :  table_html.html * / any_uf.jsonl  



### Processo completo
Um Script em python (*Script_exemplo.py*) realiza os subprocessos citados até obter todas as faixas de CEPs de uma lista de UFs requeridas (no mínimo duas). 
  
![script_ex](https://user-images.githubusercontent.com/56703046/171811826-b08cdd33-54bc-4340-903c-ceb88a470847.jpg)

Portanto o arquivo de saída deve ter o seguinte formato: 

{"ID": int, "Localidade": "", "Faixa de CEP": ""} 


> Os dados são gravados na pasta "uf_files"


**Metas Cumpridas **
- Substituição do Selenium por Requests 
- Teste de funcionalidades desacopladas umas das outras 
- Nova documentaçao mais clara com diagramas 

**Metas a Cumprir**
- Criar testes automatizados com unittest 
- Debug do código com Logs (Logging.py)
- Refatorar codigo  (Orientado a Objetos)
  
  <h2>Requerimentos Para Executar</h2>
<p>Python: v = 3.64</p>
<p>pandas: v = 1.0.1,</p>
<p>beautifulsoup4: v = 4.8.2,</p>
<div>jsonlines: v = 2.0.0</div>
