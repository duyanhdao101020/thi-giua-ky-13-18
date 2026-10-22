# -*- coding: utf-8 -*-
# FILE TU SINH, khong sua tay. Chay: mo CMD -> go "python " -> keo tha file nay vao CMD -> Enter.
# Tao thu muc "audio" MOI ngay tai thu muc hien tai cua CMD, khong can di chuyen vao thu muc nao.
import os, sys, subprocess, asyncio, importlib
S = __SENTENCES__
OUT = os.path.join(os.getcwd(), "audio")
VOICE, RATE = "zh-CN-XiaoxiaoNeural", "-20%"

print("Dang cai/nang cap thu vien (lan dau co the mat ~30 giay)...")
subprocess.call([sys.executable, "-m", "pip", "install", "--quiet", "--upgrade", "edge-tts", "gTTS"])
importlib.invalidate_caches()
try:
    import edge_tts
except Exception:
    edge_tts = None

def google(t, f):
    from gtts import gTTS
    gTTS(t, lang="zh-CN").save(f)

async def main():
    os.makedirs(OUT, exist_ok=True)
    print("Thu muc dau ra:", OUT, "\n")
    use_edge, fails = edge_tts is not None, 0
    for i, t in S:
        f = os.path.join(OUT, i + ".mp3")
        if os.path.exists(f) and os.path.getsize(f) > 1000:
            continue
        ok = False
        if use_edge:
            for k in range(2):
                try:
                    await edge_tts.Communicate(t, VOICE, rate=RATE).save(f); ok = True; print("OK", i); break
                except Exception as e:
                    print("Loi Microsoft", i, str(e)[:60])
            fails = 0 if ok else fails + 1
            if fails >= 2:
                use_edge = False
                print("\n>>> Microsoft tu choi (403). Chuyen sang giong du phong Google...\n")
        if not ok:
            try:
                google(t, f); ok = True; print("OK (Google)", i)
            except Exception as e:
                print("Loi Google", i, str(e)[:60])
                if os.path.exists(f): os.remove(f)
    n = len([x for x in os.listdir(OUT) if x.endswith(".mp3") and os.path.getsize(os.path.join(OUT, x)) > 1000])
    print("\nXONG: co %d/%d file MP3 trong:\n%s" % (n, len(S), OUT))
    try: os.startfile(OUT)
    except Exception: pass

asyncio.run(main())
input("\nNhan Enter de dong...")
