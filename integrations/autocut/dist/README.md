# AutoCut para o FilmCraft v{{VERSION}}

Corta silêncios, acha highlights de gameplay, aplica zoom automático e importa legendas (Whisper local)
numa sequência do [FilmCraft](https://github.com/storytold/filmcraft). Motor: [AutoCut Free](https://github.com/usaginoyami/autocut-free).
Código-fonte: https://github.com/usaginoyami/filmcraft_Autocut (pasta `integrations/autocut/`).

Este pacote não inclui o FilmCraft: instale o editor pelo [site oficial do projeto](https://github.com/storytold/filmcraft/releases)
e use esta ponte com ele.

## Requisitos

- FilmCraft (desktop) instalado
- Python 3.9+ e [FFmpeg](https://ffmpeg.org) no PATH (`winget install Gyan.FFmpeg` no Windows)
- Legendas (opcional): `pip install faster-whisper`

## Uso

1. Abra o FilmCraft com o canal de controle ligado e um token novo (o mesmo token nos dois passos).

   Windows (PowerShell):
   ```powershell
   $env:FILMCRAFT_CONTROL_TOKEN = -join ((1..32) | ForEach-Object { '{0:x2}' -f (Get-Random -Maximum 256) })
   & "$env:LOCALAPPDATA\Programs\ArtCraft\FilmCraft\filmcraft.exe" --control 9876
   ```
   (se instalou em outra pasta, use o caminho do seu `filmcraft.exe`; mantenha esta janela aberta)

   Linux / macOS:
   ```sh
   export FILMCRAFT_CONTROL_TOKEN="$(python3 -c 'import secrets; print(secrets.token_hex(32))')"
   filmcraft --control 9876
   ```

2. Em **outro terminal da mesma sessão** (o token precisa estar definido nele também), rode:

   ```sh
   python filmcraft_autocut.py video.mp4 --mode silence --zoom --captions
   python filmcraft_autocut.py gameplay.mp4 --mode highlights --top 12 --before 6 --after 4
   ```

   Os arquivos `<video>_autocut.xml` e `.srt` são gravados ao lado do vídeo. A sequência `<video>_autocut`
   aparece no FilmCraft. O vídeo original não é alterado, e cada etapa é desfazível (**Edit > Undo**).

## Opções

Da ponte: `--port` (padrão 9876), `--host`, `--zoom`, `--zoom-scale 112`, `--captions`, `--lang pt`.
Do motor: `--mode silence|highlights`, `--track N` (faixa de áudio, 0 = primeira; para legendas use o
microfone), `--noise auto|-35`, `--min-silence 0.4`, `--pad 0.08`, `--top`, `--before`, `--after`,
`--model tiny|base|small|medium`, `--device cpu|cuda`.

`--animated` (legenda animada em `.mov`) não é aceito: use `--captions`.

## Limitações

- Cria uma sequência nova; não corta uma sequência que você já editou.
- Highlights usa só o volume do áudio, e o zoom é fixo e centralizado.
- Não coloque o token em argumentos de comando nem em arquivos compartilhados.

## Licença

MIT, © 2026 usaginoyami (arquivo `LICENSE`). Não é um produto oficial do FilmCraft nem da equipe ArtCraft.
