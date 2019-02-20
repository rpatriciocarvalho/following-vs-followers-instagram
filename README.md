# Following vs Fallowers (instagram)

Esse pequeno script compara a lista de pessoas que você segue no instagram com a lista dos seus seguidores. Retorna então aqueles que você segue mas que não lhe seguiram de volta.

## Instruções breves

Como a API do Instagram está sendo aos poucos desativada para perfis comuns, devemos então fazer essa raspagem manualmente.

Há duas variáveis importantes: `seguidores` e `seguindo`. Nelas devem conter a lista de pessoas que são seus seguidores e quem você segue respectivamente. Para tal sigamos os seguintes passos:

* Acessar o perfil em `https://www.instagram.com/seu_perfil`
* Clicar em `Seguidores` e rolar a lista até o final para carregar todos eles (sim, é chato)
* Abrir as ferramentas de desenvolvedor do seu navegador e copiar todo o conteúdo **dentro** da tag `<ul class="jSC57  _6xe7A">`
* Colar o respectivo conteúdo na variável `seguidores`
* Repetir o procedimento para a lista de pessoas que estão lhe seguindo, variável `seguindo`

## Implementação futura

* Automatizar o processo de obtenção dos dados.
