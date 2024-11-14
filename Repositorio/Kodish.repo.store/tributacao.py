import xbmcgui

def main():
    preco_str = xbmcgui.Dialog().input('[COLOR yellow]Digite o Valor em Dólares Americanos [/COLOR]', '', type=xbmcgui.INPUT_ALPHANUM)
    preco_rs = xbmcgui.Dialog().input('[COLOR yellow]Digite a Cotação do Dolar para Real   [/COLOR]', '', type=xbmcgui.INPUT_ALPHANUM)

    try:
        preco = float(preco_str)
        cotacao = float(preco_rs)
    except ValueError:
        xbmcgui.Dialog().ok('[B][COLOR red]Erro[/COLOR][/B]', 'Por favor, insira um número válido.')
        return

    if preco <= 50:
        trib = (preco * 1.17) * 1.20
        ctrib = trib * cotacao
        xbmcgui.Dialog().ok('[B][COLOR white]Resultado[/COLOR][/B] R$', str(ctrib))
    else:
        trib1 = (50 * 1.17) * 1.20
        trib2 = ((preco - 50)* 1.17) * 1.60
        trib3 = trib1 + trib2
        ctrib = trib3 * cotacao
        xbmcgui.Dialog().ok('[B][COLOR white]Resultado[/COLOR][/B] R$', str(ctrib))
        
        
