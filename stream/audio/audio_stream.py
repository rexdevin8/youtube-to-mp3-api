import math
import json
import youtube_dl


class AudioStream:
    class _Audio:
        def __init__(
                self,
                id: str,
                title: str,
                thumbnail_url: str,
                audio_url: str,
                filesize: int,
                duration: str,
                duration_in_seconds: int,
        ):
            self.id = id
            self.title = title
            self.thumbnail_url = thumbnail_url
            self.audio_url = audio_url
            self.filesize = filesize
            self.duration = duration
            self.duration_in_seconds = duration_in_seconds

        def toJSON(self) -> json:
            return json.loads(
                json.dumps(
                    self.__dict__,
                    indent=4
                )
            )

    ydl = youtube_dl.YoutubeDL()

    def __init__(
            self,
            youtube_url: str,
            ydl_opts: dict = {}
    ):
        self.youtube_url = youtube_url
        self.ydl_opts = ydl_opts

    def info(self) -> _Audio:
        best_audio_format = 2
        try:
            result = self.ydl.extract_info(self.youtube_url, download=False)
            filesize_in_bytes = result["formats"][best_audio_format]["filesize"]
            filesize = self.convert_size(filesize_in_bytes)
            audio = self._Audio(
                id=result["id"],
                title=result["title"],
                thumbnail_url=result["thumbnails"][0]["url"],
                audio_url=result["formats"][best_audio_format]["url"],
                filesize=filesize,
                duration=self.hms(result["duration"]),
                duration_in_seconds=result["duration"],
            )
            print(audio)
            return audio

        except:
            # return not valid object type, so forces throw error response
            return -1

    def convert_size(self, size_bytes) -> str:
        if size_bytes == 0:
            return "0B"
        size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
        i = int(math.floor(math.log(size_bytes, 1024)))
        p = math.pow(1024, i)
        s = round(size_bytes / p, 2)
        return "%s %s" % (s, size_name[i])

    def hms(self, value):
        hours = value // 3600
        minutes = value % 3600 // 60
        seconds = value % 3600 % 60
        return '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)
