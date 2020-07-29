[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://dashboard.heroku.com/new?template=https://github.com/yasinkbas/youtube-to-mp3-api)


### Example Request
**Url**: [**your-heroku-app-name**].herokuapp.com/?url=[**your-youtube-url**]
<br>**Example**: https://youtube-to-mp3-api.herokuapp.com/?url=https://www.youtube.com/watch?v=hn3wJ1_1Zsg

####Output

```bash
{
  "id": "b6WNdcZpDhQ",
  "title": "Billie Eilish - when the party's over (Audio)",
  "thumbnail_url": "https://i.ytimg.com/vi/b6WNdcZpDhQ/hqdefault.jpg?sqp=-oaymwEYCKgBEF5IVfKriqkDCwgBFQAAiEIYAXAB&rs=AOn4CLCmliYITRb3drEr5JmBRk1naUc5lQ",
  "audio_url": "https://r2---sn-aigl6nl7.googlevideo.com/videoplayback?expire=1596073927&ei=Z9MhX-CGHY_SxN8PyO-N8AE&ip=34.244.65.212&id=o-AN-u5i48OWLs9oYmnJuTqKEEOujE1kfX8XW5fbiXbiCR&itag=140&source=youtube&requiressl=yes&mh=7J&mm=31%2C26&mn=sn-aigl6nl7%2Csn-4g5e6nsy&ms=au%2Conr&mv=u&mvi=2&pl=24&gcr=ie&vprv=1&mime=audio%2Fmp4&gir=yes&clen=3162603&dur=195.372&lmt=1575722267605206&mt=1596052067&fvip=2&keepalive=yes&fexp=23883098&c=WEB&txp=5431432&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cgcr%2Cvprv%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl&lsig=AG3C_xAwRQIhANplnF59hHQaDtxgVhjCWREmwOoLXUPN7qSIxsU1f8yYAiBExN4cMIGYJ5RGeWBhKF1z54yXA_-qPpfgwnQjsvC9ig%3D%3D&sig=AOq0QJ8wRQIhAOmEKllOhExeRRiwGT27Vo00l_dPkiIY9OywooAHdt9fAiAZ76wjABaMUKygO3NbIC6eOZVU3mCyuW3h_vU9WbNr1w==&ratebypass=yes",
  "filesize": "3.02 MB",
  "duration": "00:03:15",
  "duration_in_seconds": 195
}
```

####Important

 This project just built for fun and based on [youtube-dl](https://github.com/ytdl-org/youtube-dl). This means if you get error like `Bad Request` or mp3 file does not work, probably the problem is caused by youtube-dl see: [issues](https://github.com/ytdl-org/youtube-dl/issues)