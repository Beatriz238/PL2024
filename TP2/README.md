# TPC2: Conversor de MD para HTML

**Data:** 2024-02-18

## Autor

- **Nome:** Beatriz Fernandes
- **Id:** A100602

## Resumo

Este TPC consistiu na realização de um pequeno programa, em python,de conversão de texto MarkDown para HTML para os elementos descritos abaixo:

+ **Cabeçalhos:** Linhas iniciadas por `#`, `##` ou `###`

    **In:** `#` Exemplo

    **Out:** `<h1>` Exemplo`</h1>`

+ **Bold:** pedaços de texto entre `**`:

    **In:** Este é um `**`exemplo`**`

    **Out:** Este é um `<b>`exemplo`</b>`

+ **Itálico:** pedaços de texto entre `*`:

    **In:** Este é um `*`exemplo`*`

    **Out:** Este é um `<i>`exemplo`</i>`

+ **Listas Numeradas:**

    **In:**
        1. Primeiro item
        2. Segundo item
        3. Terceiro item
    
    **Out:**
        `<ol>`
        `<li>Primeiro item</li>`
        `<li>Segundo item</li>`
        `<li>Terceiro item</li>`
        `</ol>`

+ **Link:** [texto](endereço URL)
    
    **In:** `[página da UC](http://www.uc.pt)`
    
    **Out:** `<a href="http://www.uc.pt">página da UC</a>`

+ **Imagem:** ![texto alternativo](path para a imagem)
    
    **In:** `![imagem dum coelho](http://www.coellho.com)`
    
    **Out:** `<img src="http://www.coellho.com" alt="imagem dum coelho"/>`

