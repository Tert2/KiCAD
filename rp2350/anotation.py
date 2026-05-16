import pcbnew
import re
from collections import defaultdict

board = pcbnew.GetBoard()

# フットプリント一覧取得
footprints = list(board.GetFootprints())

# (Y, X) でソート（上→下、左→右）
def fp_pos_key(fp):
    pos = fp.GetPosition()
    return (pos.y, pos.x)

footprints.sort(key=fp_pos_key)

# 部品種別ごとにまとめる
groups = defaultdict(list)

for fp in footprints:
    ref = fp.GetReference()
    m = re.match(r"([A-Za-z]+)", ref)
    if m:
        prefix = m.group(1)
    else:
        prefix = "U"  # 念のため
    groups[prefix].append(fp)

# 再アノテーション実行
for prefix, fps in groups.items():
    count = 1
    for fp in fps:
        new_ref = f"{prefix}{count}"
        fp.SetReference(new_ref)
        count += 1

# 画面更新
pcbnew.Refresh()

print("再アノテーション完了（PCB側）")
