import pcbnew
import wx

board = pcbnew.GetBoard()
ds = board.GetDesignSettings()

app = wx.App(False)

# =========================
# 開始番号
# =========================
dlg_start = wx.TextEntryDialog(
    None,
    "連番の開始番号を入力してください",
    "IOピン シルク生成",
    "1"
)
if dlg_start.ShowModal() != wx.ID_OK:
    dlg_start.Destroy()
    raise SystemExit
start = int(dlg_start.GetValue())
dlg_start.Destroy()

# =========================
# 終了番号
# =========================
dlg_end = wx.TextEntryDialog(
    None,
    "連番の終了番号を入力してください",
    "IOピン シルク生成",
    str(start)
)
if dlg_end.ShowModal() != wx.ID_OK:
    dlg_end.Destroy()
    raise SystemExit
end = int(dlg_end.GetValue())
dlg_end.Destroy()

if end < start:
    wx.MessageBox("終了番号は開始番号以上にしてください", "エラー")
    raise SystemExit

labels = [str(i) for i in range(start, end + 1)]

# =========================
# 設定
# =========================
layer = pcbnew.F_SilkS
offset = pcbnew.VECTOR2I(0, pcbnew.FromMM(1.2))

# ★ KiCad 7/8/9 対応（レイヤー指定必須）
text_size = ds.GetTextSize(layer)
text_thickness = ds.GetTextThickness(layer)

# =========================
# パッド収集
# =========================
pads = []
for fp in board.GetFootprints():
    for pad in fp.Pads():
        pads.append(pad)

# 上→下、左→右
pads.sort(key=lambda p: (p.GetPosition().y, p.GetPosition().x))

# =========================
# シルク生成
# =========================
for pad, label in zip(pads, labels):
    txt = pcbnew.PCB_TEXT(board)
    txt.SetText(label)
    txt.SetLayer(layer)
    txt.SetTextSize(text_size)
    txt.SetTextThickness(text_thickness)
    txt.SetPosition(pad.GetPosition() + offset)
    board.Add(txt)

pcbnew.Refresh()
wx.MessageBox(f"{start}～{end} のシルクを生成しました", "完了")
