## AutoCut para o FilmCraft v{{VERSION}}

Ponte que liga o motor do [AutoCut Free](https://github.com/usaginoyami/autocut-free)
ao editor [FilmCraft](https://github.com/storytold/filmcraft).

### O que faz
- **Corta silêncios** com limiar automático ou manual
- **Highlights de gameplay** pelos picos de áudio
- **Zoom automático**: alterna a escala entre 100% e 112% a cada corte
- **Legendas** com Whisper local (offline), importadas como trilha de legendas
- Mantém todas as faixas de áudio do arquivo
- Cria uma sequência nova; o vídeo original não é alterado e cada etapa é desfazível

### Como usar
Baixe `autocut-filmcraft-v{{VERSION}}.zip`, extraia e siga o `README.md` do pacote. Resumo: abra o FilmCraft com
`--control 9876` e um `FILMCRAFT_CONTROL_TOKEN`, depois rode
`python filmcraft_autocut.py video.mp4 --mode silence --zoom --captions`.

### Requisitos
FilmCraft instalado, Python 3.9+, FFmpeg no PATH e, para legendas, `faster-whisper`.

### Observações
- Este release **não inclui o FilmCraft**; use o editor original.
- Testado contra o motor de importação do FilmCraft (CLI headless) e contra um servidor de controle simulado;
  ainda não exercitado ponta a ponta com a janela do app aberta.
- Windows: o caminho de `filmcraft.exe` no README é o padrão do instalador e pode variar.

Licença MIT. Projeto independente, sem relação oficial com o FilmCraft ou a equipe ArtCraft.
