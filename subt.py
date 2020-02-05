import os
import sys
import subprocess as sp
import pysrt

from moviepy.tools import subprocess_call
from moviepy.config import get_setting
from moviepy.video import *


"""extracting video subclips and their audio"""
def ffmpeg_extract_subclip(filename, t1, t2, targetname=None):
    """ makes a new video file playing video file ``filename`` between
        the times ``t1`` and ``t2``. """
    name,ext = os.path.splitext(filename)
    if not targetname:
        T1, T2 = [int(1000*t) for t in [t1, t2]]
        targetname = name+ "%sSUB%d_%d.%s"(name, T1, T2, ext)
    
    cmd = [get_setting("FFMPEG_BINARY"),"-y",
      "-i", filename,
      "-ss", "%0.2f"%t1,
      "-t", "%0.2f"%(t2-t1),
      "-vcodec", "copy", "-acodec", "copy", targetname]
    
    subprocess_call(cmd)

def ffmpeg_extract_audio(inputfile,output,bitrate=3000,fps=44100):
    """ extract the sound from a video file and save it in ``output`` """
    cmd = [get_setting("FFMPEG_BINARY"), "-y", "-i", inputfile, "-ab", "%dk"%bitrate,
         "-ar", "%d"%fps, output]
    subprocess_call(cmd)



"""path of subtitle file"""
sub = pysrt.open("sub.srt") 

"""start = (sub[33].start.to_time())
end =  (sub[33].end.to_time())
startsec = float(start.hour) * 3600 + float(start.minute) * 60 + float(start.microsecond)/1000000 + float(start.second)
endsec = float(end.hour) * 3600 + float(end.minute) * 60 + float(end.microsecond)/1000000 + float(end.second)
print startsec
print endsec
print len(sub)


ffmpeg_extract_subclip("Dexter.mp4", startsec, 95.0, targetname="trim"+str(33)+".mp4")"""



""" this one is working, cpnverting start and end time to float seconds"""
"""ffmpeg_extract_subclip(path of file, startsecond, endsecond, sink file)"""
"""TestCommentUpdated"""
for i in range(1,4):
  start = (sub[i].start.to_time())
  end =  (sub[i].end.to_time())
  startsec = float(start.hour) * 3600 + float(start.minute) * 60 + float(start.microsecond)/1000000 + float(start.second)
  endsec = float(end.hour) * 3600 + float(end.minute) * 60 + float(end.microsecond)/1000000 + float(end.second)
  ffmpeg_extract_subclip("Dexter.mp4", startsec, endsec, targetname="trim"+str(i)+".mp4")             
  ffmpeg_extract_audio("trim"+str(i)+".mp4", "audio"+str(i)+".mp3", bitrate=3000, fps=44100)


"""j = 0
for i in sub
  if i == 8: break
  start = sub[i].start.to_time()
  end = sub[i].end.to_time()
  ffmpeg_extract_subclip("Dexter.mkv", start, end, targetname="trim"+str(j)+".mp4")
  ffmpeg_extract_audio("trim"+str(j)+".mp4", "audio"+str(i)+".mp3", bitrate=3000, fps=44100)
  j+=1
"""

