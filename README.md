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
      <a href="#ferramentas-do-plugin">Ferramentas do Plugin</a>
      <ul>
        <li><a href="#consultar-base-do-incra">Consultar base do INCRA</a></li>
      </ul>
      <ul>
        <li><a href="#csv-do-incra-para-camada-pointz">CSV do INCRA para camada PointZ</a></li>
      </ul>
      <ul>
        <li><a href="#alimentar-camada-vértice">Alimentar camada vértice</a></li>
      </ul>
      <ul>
        <li><a href="#baixar-planilha-ods-do-sigef">Baixar planilha ODS do SIGEF</a></li>
      </ul>
      <ul>
        <li><a href="#gerar-txt-para-planilha-ods">Gerar TXT para Planilha ODS</a></li>
      </ul>
      </li>
      <li>
      <a href="#banco-de-dados-georural">Banco de Dados GeoRural</a>
      <ul>
        <li><a href="#classe-vértice">Classe Vértice</a></li>
      </ul>
      <ul>
        <li><a href="#classe-limite">Classe Limite</a></li>
      </ul>
      <ul>
        <li><a href="#classe-parcela">Classe Parcela</a></li>
      </ul>
    <li>
      <a href="#como-contribuir-aprendendo-mais">Como contribuir aprendendo mais</a>
    </li>
    <li>
      <a href="#colaboradores">Colaboradores</a>
    </li>
    <li>
      <a href="#autores">Autores</a>
    </li>
  </ol>
</details>


## Ferramentas do Plugin


### Consultar base do INCRA
Conecta a base de dados do INCRA e carrega camada de imóveis a partir de um retângulo selecionado pelo usuário. Também é possível baixar dados dos imóveis certificados nos formatos CSV e SHP, obtendo-se mais informações complementares.
<div align="center">
    
https://user-images.githubusercontent.com/88212377/161190002-e3f211bd-a337-4f4a-9632-25ff67b07eb1.mp4
    
</div>

### CSV do INCRA para camada PointZ
Esta ferramenta transforma um arquivo CSV de vértices do INCRA em uma camada do tipo PointZ.
<div align="center">
    
https://user-images.githubusercontent.com/88212377/161395789-9c55d2d3-3e60-4a2e-92b9-a16a204a87c5.mp4
    
</div>

### Alimentar camada vértice
Esta ferramenta carrega as feições selecionadas de uma camada de pontos para dentro da camada vértices do banco de dados GeoRural.
<div align="center">
    
https://user-images.githubusercontent.com/88212377/161395699-088309e5-d25b-4745-926e-0edddc37b091.mp4
    
</div>

### Baixar planilha ODS do SIGEF
Gera uma planilha ODS vazia para preenchimento com os dados gerados no TXT.
<div align="center">
    
https://user-images.githubusercontent.com/88212377/161395839-00643672-4ff0-4336-aba4-6edcd1459612.mp4
    
</div>

### Gerar TXT para Planilha ODS
Cria um arquivo de Texto (TXT) com todas os dados necessários para preencher a planilha ODS do SIGEF.
<div align="center">
    
https://user-images.githubusercontent.com/88212377/161395898-a09d962e-33a8-4da9-a3b2-c9f06eb5b403.mp4
    
</div>



## Banco de Dados GeoRural


### Classe Vértice
É todo ponto onde a linha limítrofe do imóvel muda de direção ou onde existe interseção desta linha com qualquer outra linha limítrofe de imóveis contíguos ou servidões de passagem (INCRA, 2010).
<div align="center">
<p class="MsoNormal" style="text-align: center;"
 align="center">Tabela 1: Atributos
da camada v&eacute;rtice<o:p></o:p></p>
<div align="center">
<table class="MsoNormalTable" style="" border="0"
 cellpadding="0">
  <tbody>
    <tr style="">
      <td
 style="padding: 0cm 7.5pt; background: rgb(221, 221, 221) none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><b><span
 style="background: rgb(221, 221, 221) none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;"><b>Item</b>&nbsp;</span></b><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: rgb(221, 221, 221) none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; text-align: center; line-height: normal;"
 align="center"><b><span
 style="background: rgb(221, 221, 221) none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">Nome&nbsp;</span></b><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: rgb(221, 221, 221) none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; text-align: center; line-height: normal;"
 align="center"><b><span
 style="background: rgb(221, 221, 221) none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">Tipo&nbsp;</span></b><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: rgb(221, 221, 221) none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; text-align: center; line-height: normal;"
 align="center"><b><span
 style="background: rgb(221, 221, 221) none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">Dom&iacute;nio</span></b><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
    </tr>
    <tr style="">
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; text-align: center; line-height: normal;"
 align="center"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">1</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">sigma_x&nbsp;</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">REAL&nbsp;</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; text-align: center; line-height: normal;"
 align="center"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">-</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
    </tr>
    <tr style="">
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; text-align: center; line-height: normal;"
 align="center"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">2</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">sigma_y&nbsp;</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">REAL&nbsp;</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; text-align: center; line-height: normal;"
 align="center"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">-</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
    </tr>
    <tr style="">
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; text-align: center; line-height: normal;"
 align="center"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">3</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">sigma_z&nbsp;</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">REAL&nbsp;</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; text-align: center; line-height: normal;"
 align="center"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">-</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
    </tr>
    <tr style="">
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; text-align: center; line-height: normal;"
 align="center"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">4</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">indice&nbsp;</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">MEDIUMINT&nbsp;</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; text-align: center; line-height: normal;"
 align="center"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">-</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
    </tr>
    <tr style="">
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; text-align: center; line-height: normal;"
 align="center"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">5</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">metodo_pos&nbsp;</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">TEXT(4)&nbsp;</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; text-align: center; line-height: normal;"
 align="center"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">PG1,
PG2, PG3, PG4, PG5, PG6, PG7, PG8, PG9, PT1, PT2, PT3, PT4, PT5, PT6,
PT7, PT8, PA1, PA2, PS1, PS2, PS3, PS4</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
    </tr>
    <tr style="">
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; text-align: center; line-height: normal;"
 align="center"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">6</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">tipo_verti&nbsp;</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">TEXT(4)&nbsp;</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; text-align: center; line-height: normal;"
 align="center"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">M,
P, V</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
    </tr>
    <tr style="">
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; text-align: center; line-height: normal;"
 align="center"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">7</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">vertice&nbsp;</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">TEXT(12)&nbsp;</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; text-align: center; line-height: normal;"
 align="center"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">-</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
    </tr>
    <tr style="">
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; text-align: center; line-height: normal;"
 align="center"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">8</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">qrcode&nbsp;</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">TEXT(40)&nbsp;</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; text-align: center; line-height: normal;"
 align="center"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">-</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
    </tr>
  </tbody>
</table>
</div>
<p class="MsoNormal"><o:p>&nbsp;</o:p></p>
</div>

### Classe Limite
Os limites são linhas que definem as confrontações, seja pelo tipo de confrontação ou pelo próprio confrontante.
<div align="center">
<p class="MsoNormal" style="text-align: center;"
 align="center">Tabela 2: Atributos
da camada limite<o:p></o:p></p>
<div align="center">
<table class="MsoNormalTable" style="" border="0"
 cellpadding="0">
  <tbody>
    <tr style="">
      <td
 style="padding: 0cm 7.5pt; background: rgb(221, 221, 221) none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; text-align: center; line-height: normal;"
 align="center"><b><span
 style="background: rgb(221, 221, 221) none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">Item</span></b><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: rgb(221, 221, 221) none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; text-align: center; line-height: normal;"
 align="center"><b><span
 style="background: rgb(221, 221, 221) none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">Nome&nbsp;</span></b><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: rgb(221, 221, 221) none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; text-align: center; line-height: normal;"
 align="center"><b><span
 style="background: rgb(221, 221, 221) none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">Tipo&nbsp;</span></b><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: rgb(221, 221, 221) none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; text-align: center; line-height: normal;"
 align="center"><b><span
 style="background: rgb(221, 221, 221) none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">Dom&iacute;nio&nbsp;</span></b><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
    </tr>
    <tr style="">
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; text-align: center; line-height: normal;"
 align="center"><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black;">1</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">tipo&nbsp;</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">TEXT(4)&nbsp;</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; text-align: center; line-height: normal;"
 align="center"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">LA1,
LA2, LA3, LA4, LA5, LA6, LA7, LN1, LN2, LN3, LN4, LN5, LN6</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
    </tr>
    <tr style="">
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; text-align: center; line-height: normal;"
 align="center"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">2</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">confrontan&nbsp;</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">TEXT(254)&nbsp;</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; text-align: center; line-height: normal;"
 align="center"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">-</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
    </tr>
    <tr style="">
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; text-align: center; line-height: normal;"
 align="center"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">3</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">cns&nbsp;</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">TEXT(200)&nbsp;</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; text-align: center; line-height: normal;"
 align="center"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">-</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
    </tr>
    <tr style="">
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; text-align: center; line-height: normal;"
 align="center"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">4</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">matricula&nbsp;</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">TEXT(100)&nbsp;</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; text-align: center; line-height: normal;"
 align="center"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">-</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
    </tr>
    <tr style="">
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; text-align: center; line-height: normal;"
 align="center"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">5</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">qrcode&nbsp;</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">TEXT(40)&nbsp;</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; text-align: center; line-height: normal;"
 align="center"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">-</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
    </tr>
  </tbody>
</table>
</div>
<p class="MsoNormal"><o:p>&nbsp;</o:p></p>
</div>

### Classe Parcela
Representação planimétrica do imóvel levantado através de uma geometria do tipo polígono.
<div align="center">
<p class="MsoNormal" style="text-align: center;"
 align="center">Tabela 3: Atributos
da camada parcela<o:p></o:p></p>
<div align="center">
<table class="MsoNormalTable" style="" border="0"
 cellpadding="0">
  <tbody>
    <tr style="">
      <td
 style="padding: 0cm 7.5pt; background: rgb(221, 221, 221) none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><b><span
 style="background: rgb(221, 221, 221) none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">Item&nbsp;</span></b><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: rgb(221, 221, 221) none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; text-align: center; line-height: normal;"
 align="center"><b><span
 style="background: rgb(221, 221, 221) none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">Nome&nbsp;</span></b><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: rgb(221, 221, 221) none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; text-align: center; line-height: normal;"
 align="center"><b><span
 style="background: rgb(221, 221, 221) none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">Tipo&nbsp;</span></b><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: rgb(221, 221, 221) none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; text-align: center; line-height: normal;"
 align="center"><b><span
 style="background: rgb(221, 221, 221) none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">Dom&iacute;nio&nbsp;</span></b><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
    </tr>
    <tr style="">
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; text-align: center; line-height: normal;"
 align="center"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">1</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">nome&nbsp;</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">TEXT(254)&nbsp;</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">&nbsp;</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
    </tr>
    <tr style="">
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; text-align: center; line-height: normal;"
 align="center"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">2</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">nat_serv&nbsp;</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">MEDIUMINT&nbsp;</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">1
&ndash; Particular</span><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;"><o:p></o:p></span></p>
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black;">2
&ndash; Contrato com Adm P&uacute;blica</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
    </tr>
    <tr style="">
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; text-align: center; line-height: normal;"
 align="center"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">3</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">pessoa&nbsp;</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">MEDIUMINT&nbsp;</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">1
&ndash; F&iacute;sica</span><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;"><o:p></o:p></span></p>
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black;">2
&ndash; Jur&iacute;dica</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
    </tr>
    <tr style="">
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; text-align: center; line-height: normal;"
 align="center"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">4</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">cpf_cnpj&nbsp;</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">TEXT(20)&nbsp;</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; text-align: center; line-height: normal;"
 align="center"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">-</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
    </tr>
    <tr style="">
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; text-align: center; line-height: normal;"
 align="center"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">5</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">denominacao&nbsp;</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">TEXT&nbsp;</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; text-align: center; line-height: normal;"
 align="center"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">-</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
    </tr>
    <tr style="">
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; text-align: center; line-height: normal;"
 align="center"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">6</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">situacao&nbsp;</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">MEDIUMINT&nbsp;</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; text-align: center; line-height: normal;"
 align="center"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">-</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
    </tr>
    <tr style="">
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; text-align: center; line-height: normal;"
 align="center"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">7</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">natureza&nbsp;</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">MEDIUMINT&nbsp;</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black;">1
- Im&oacute;vel Registrado</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black;">2
- &Aacute;rea Titulada n&atilde;o Registrada</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black;">3
- &Aacute;rea n&atilde;o Titulada</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black;">1
- Assentamento</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black;">2
- Assentamento Parcela</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black;">3
- Estrada</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black;">4
- Ferrovia</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black;">5
- Floresta P&uacute;blica</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black;">6
- Gleba P&uacute;blica</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black;">7
- Particular</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black;">8
- Per&iacute;metro Urbano</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black;">9
- Terra Ind&iacute;gena</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black;">10
- Terreno de Marinha</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black;">11
- Terreno Marginal</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black;">12
- Territ&oacute;rio Quilombola</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black;">13
- Unidade de Conserva&ccedil;&atilde;o</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
    </tr>
    <tr style="">
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; text-align: center; line-height: normal;"
 align="center"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">8</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">sncr&nbsp;</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">TEXT(20)&nbsp;</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; text-align: center; line-height: normal;"
 align="center"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">-</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
    </tr>
    <tr style="">
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; text-align: center; line-height: normal;"
 align="center"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">9</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">matricula&nbsp;</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">TEXT(50)&nbsp;</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; text-align: center; line-height: normal;"
 align="center"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">-</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
    </tr>
    <tr style="">
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; text-align: center; line-height: normal;"
 align="center"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">10</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">cod_cartorio&nbsp;</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">TEXT(30)&nbsp;</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; text-align: center; line-height: normal;"
 align="center"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">-</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
    </tr>
    <tr style="">
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; text-align: center; line-height: normal;"
 align="center"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">11</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">data&nbsp;</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">DATE&nbsp;</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; text-align: center; line-height: normal;"
 align="center"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">-</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
    </tr>
    <tr style="">
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; text-align: center; line-height: normal;"
 align="center"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">12</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">qrcode&nbsp;</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">TEXT(40)&nbsp;</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; text-align: center; line-height: normal;"
 align="center"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">-</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
    </tr>
    <tr style="">
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; text-align: center; line-height: normal;"
 align="center"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">13</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">municipio&nbsp;</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">TEXT&nbsp;</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; text-align: center; line-height: normal;"
 align="center"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">Munic&iacute;pios
do Brasil (IBGE)</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
    </tr>
    <tr style="">
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; text-align: center; line-height: normal;"
 align="center"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">14</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">uf&nbsp;</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; line-height: normal;"><span
 style="background: whitesmoke none repeat scroll 0%; font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">TEXT&nbsp;</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
      <td
 style="padding: 0cm 7.5pt; background: whitesmoke none repeat scroll 0%; -moz-background-clip: initial; -moz-background-origin: initial; -moz-background-inline-policy: initial;">
      <p class="MsoNormal"
 style="margin-bottom: 0cm; text-align: center; line-height: normal;"
 align="center"><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif; color: black;">UFs
(IBGE)</span><span
 style="font-size: 12pt; font-family: &quot;Times New Roman&quot;,serif;"><o:p></o:p></span></p>
      </td>
    </tr>
  </tbody>
</table>
</div>
<p class="MsoNormal"><o:p>&nbsp;</o:p></p>
</div>
Observação: Também podem ser utilizadas as camadas “hist_vertice”, “hist_limite” e “hist_parcela” para armazenamento dos dados de georreferenciamento anteriores e, assim, manter o histórico de todos os trabalhos, possibilitando a consulta dos códigos anteriores, análises e relatórios de desempenho.
<br>

https://user-images.githubusercontent.com/88212377/161396633-24f01f9c-a15b-46c8-84db-c4a6acd49a27.mp4



## Como contribuir aprendendo mais
<div style="text-align: center;"><a
 href="https://go.hotmart.com/X69158193B"><img
 style="border: 2px solid ;" alt="GeoINCRA no QGIS"
 title="CURSO NA HOTMART"
 src="https://user-images.githubusercontent.com/88212377/161396191-32d9775a-d877-4eed-b8d1-61f07caf4af8.jpg"></a>
<br>
</div>
<div style="text-align: center;"><a
 style="font-weight: bold;"
 href="https://go.hotmart.com/X69158193B">CLIQUE AQUI: Georreferenciamento de Imóveis Rurais com o plugin GeoINCRA no QGIS</a></div>


## Colaboradores

<div style="text-align: center;"><a
 href="https://www.acgeoengenharia.com.br/"><img
 style="border: 2px solid ;" alt="ACGEO Engenharia"
 title="ACGEO Engenharia"
 src="https://user-images.githubusercontent.com/88212377/161191725-f37650ff-1fba-4cae-8145-af45f1c599d1.jpg"></a>
<br>
</div>


## Autores

Tiago Prudencio e
Leandro França


