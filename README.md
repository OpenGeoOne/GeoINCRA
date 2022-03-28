<!-- PROJECT LOGO -->
<p align="center">
    <img src="https://github.com/OpenGeoOne/GeoINCRA/blob/main/images/geoincra_logo.png" alt="Logo" width="90" height="75">
  <h3 align="center">GeoINCRA</h3>
  <p align="center">
    <b><i>Plugin do QGIS para o georreferenciamento de imóveis rurais conforme normas técnicas do Instituto Nacional de Colonização e Reforma Agrária (INCRA).</i><b>
    <br />
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Conteúdo</summary>
  <ol>
    <li>
      <a href="#Banco-de-Dados-GeoRural">Banco de Dados GeoRural</a>
      <ul>
        <li><a href="#Classe-Vértice">Classe Vértice</a></li>
      </ul>
      <ul>
        <li><a href="#limite">Classe Limite</a></li>
      </ul>
      <ul>
        <li><a href="#parcela">Classe Parcela</a></li>
      </ul>
      <li>
      <a href="#vetor">Ferramentas do Plugin</a>
      <ul>
        <li><a href="#consultar-base-do-incra">Consultar base do INCRA</a></li>
      </ul>
      <ul>
        <li><a href="#adicionar-vertices-incra">Adicionar vertices INCRA</a></li>
      </ul>
      <ul>
        <li><a href="#alimentar-camada">Alimentar camada "vértice"</a></li>
      </ul>
      <ul>
        <li><a href="#baixar-ods">Baixar planilha ODS do SIGEF</a></li>
      </ul>
      <ul>
        <li><a href="#gerar-txt">Gerar TXT para Planilha ODS</a></li>
      </ul>
      </li>
    <li>
      <a href="#vetor">Como contribuir</a>
    </li>
    <li>
      <a href="#vetor">Colaboradores</a>
    </li>
    <li>
      <a href="#vetor">Autores</a>
    </li>
  </ol>
</details>




## Banco de Dados GeoRural


### Classe Vértice
Cálculo de pontos ou linha a partir de um conjunto de azimutes e distâncias.
<div align="center">
<table style="text-align: left; width: 275px;" border="0" cellpadding="0" cellspacing="0">
  <tbody>
    <tr>
      <td><img src="https://github.com/LEOXINGU/lftools/blob/main/images/tutorial/survey_azimuth_distance.jpg"></td>
    </tr>
  </tbody>
</table>
</div>

### Classe Limite
Esta ferramenta calcula as coordenadas (X,Y,Z) de um ponto a partir de medições de azimute e ângulo zenital observados de duas ou mais estações de coordenadas conhecidas utilizando o Método de Interseção à Vante ajustado pelas Distâncias Mínimas.
<div align="center">
<table style="text-align: left; width: 275px;" border="0" cellpadding="0" cellspacing="0">
  <tbody>
    <tr>
      <td><img src="https://github.com/LEOXINGU/lftools/blob/main/images/tutorial/survey_3D_coord.jpg"></td>
    </tr>
  </tbody>
</table>
</div>

### Classe Parcela
Este algoritmo realiza o ajustamento de poligonal enquadrada pelo método dos mínimos quadrados, onde as observações de distâncias, ângulos e direções são ajustadas simultaneamente, fornecendo os valores mais prováveis para o conjunto de dados. Além disso, as observações podem ser rigorosamente ponderadas considerando os erros estimados e ajustados.
<div align="center">
<table style="text-align: left; width: 275px;" border="0" cellpadding="0" cellspacing="0">
  <tbody>
    <tr>
      <td><img src="https://github.com/LEOXINGU/lftools/blob/main/images/tutorial/survey_traverse.jpg"></td>
    </tr>
  </tbody>
</table>
</div>




## Ferramentas do Plugin


### Consultar base do INCRA
Gera as linhas de testada das parcelas a partir dos polígonos dos lotes.
<div align="center">
<table style="text-align: left; width: 275px;" border="0" cellpadding="0" cellspacing="0">
  <tbody>
    <tr>
      <td><img src="https://github.com/LEOXINGU/lftools/blob/main/images/tutorial/cadastre_frontlotline.jpg"></td>
    </tr>
  </tbody>
</table>
</div>

### Adicionar vertices INCRA
Esta ferramenta preenche um atributo numérico seguindo um critério geográfico, por exemplo de norte para sul e oeste para leste.</br>Obs.: Este algoritmo utiliza o centroide da feição para ordenar geograficamente.
<div align="center">
<table style="text-align: left; width: 275px;" border="0" cellpadding="0" cellspacing="0">
  <tbody>
    <tr>
      <td><img src="https://github.com/LEOXINGU/lftools/blob/main/images/tutorial/cadastre_geonumbering.jpg"></td>
    </tr>
  </tbody>
</table>
</div>

### Alimentar camada "vértice"
Esta ferramenta preenche um atributo numérico seguindo um critério geográfico, por exemplo de norte para sul e oeste para leste.</br>Obs.: Este algoritmo utiliza o centroide da feição para ordenar geograficamente.
<div align="center">
<table style="text-align: left; width: 275px;" border="0" cellpadding="0" cellspacing="0">
  <tbody>
    <tr>
      <td><img src="https://github.com/LEOXINGU/lftools/blob/main/images/tutorial/cadastre_geonumbering.jpg"></td>
    </tr>
  </tbody>
</table>
</div>

### Baixar planilha ODS do SIGEF
Esta ferramenta preenche um atributo numérico seguindo um critério geográfico, por exemplo de norte para sul e oeste para leste.</br>Obs.: Este algoritmo utiliza o centroide da feição para ordenar geograficamente.
<div align="center">
<table style="text-align: left; width: 275px;" border="0" cellpadding="0" cellspacing="0">
  <tbody>
    <tr>
      <td><img src="https://github.com/LEOXINGU/lftools/blob/main/images/tutorial/cadastre_geonumbering.jpg"></td>
    </tr>
  </tbody>
</table>
</div>

### Gerar TXT para Planilha ODS
Esta ferramenta preenche um atributo numérico seguindo um critério geográfico, por exemplo de norte para sul e oeste para leste.</br>Obs.: Este algoritmo utiliza o centroide da feição para ordenar geograficamente.
<div align="center">
<table style="text-align: left; width: 275px;" border="0" cellpadding="0" cellspacing="0">
  <tbody>
    <tr>
      <td><img src="https://github.com/LEOXINGU/lftools/blob/main/images/tutorial/cadastre_geonumbering.jpg"></td>
    </tr>
  </tbody>
</table>
</div>



## Como contribuir

CURSO HOTMART


## Colaboradores

ACGEO Engenharia


## Autores

Thiago Prudêncio e
Leandro França


